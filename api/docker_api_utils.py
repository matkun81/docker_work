import docker

from project_utils.logger import Logger


class DockerApiUtils:
    @staticmethod
    def create_image(name_image, command="/bin/bash", tty=True, stdin_open=True, auto_remove=True):
        client = DockerApiUtils.create_docker_client()
        image = client.images.pull(name_image)
        Logger.info(image.id)
        container = client.containers.create(name_image,
                                             command=command,
                                             tty=tty,
                                             stdin_open=stdin_open,
                                             auto_remove=auto_remove)
        Logger.info(container.id)
        return container

    @staticmethod
    def stop_all_docker_containers(client):
        Logger.info("Stop all containers")
        for container in client.containers.list():
            container.stop()

    @staticmethod
    def create_docker_client():
        Logger.info("Connect to docker")
        return docker.from_env()

    @staticmethod
    def remove_container(container, docker_name):
        client = DockerApiUtils.create_docker_client()
        Logger.info(f"deleting container")
        client.images.remove(image=docker_name, force=True)
        Logger.info(f"container status - {container.status}\n")
        Logger.info(DockerApiUtils.get_list_images())

    @staticmethod
    def get_list_images():
        client = DockerApiUtils.create_docker_client()
        Logger.info(client.images.list())
