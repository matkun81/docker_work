import docker

from utils.logger_util import Logger
from utils.terminall_command_utill import TerminalCommandException


class ContainerApi:
    def __init__(self, container):
        self.container = container

    def start(self):
        Logger.info(f"Container started: {self.container.name}\n"
                    f"Container status - {self.container.status}\n")
        self.container.start()

    def stop(self):
        self.container.stop()
        Logger.info(f"Container stop: {self.container.name}\n")

    def execute_command(self, command):
        command_execute_is_success = 0
        log = self.container.exec_run(command)
        Logger.info(f"Terminal command executed :{log.output}")
        if log.exit_code != command_execute_is_success:
            Logger.error(f"Terminal command was not executed!\n Check {log.output}")
            raise TerminalCommandException("Wrong command!")
        return log.output


class DockerClient:
    def __init__(self):
        self.client = docker.from_env()

    def create_container(self, name_image, command="/bin/bash", tty=True, stdin_open=True, auto_remove=True):
        image = self.client.images.pull(name_image)
        Logger.info(f"image id : {image.id}")
        container = self.client.containers.create(name_image,
                                                  command=command,
                                                  tty=tty,
                                                  stdin_open=stdin_open,
                                                  auto_remove=auto_remove)
        Logger.info(f"Container id : {container.id}")
        return ContainerApi(container)

    def stop_all_docker_containers(self):
        Logger.info("Stop all containers")
        for container in self.client.containers.list():
            container.stop()

    def remove_container(self, container, docker_name):
        Logger.info(f"deleting container")
        self.client.images.remove(image=docker_name, force=True)
        Logger.info(f"container status - {container.status}\n")

    def get_list_images(self):
        Logger.info(f"List images: {self.client.images.list()}")
