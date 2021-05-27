import docker

from project_utils.logger import Logger
from string_util.string_util import StringUtil
from tests.test_data import COMMAND_TO_GET_IP_ADDRESS


class DockerApi:
    @staticmethod
    def get_ip_from_docker_container(client, docker_container):
        ip_address = str(client.containers.run(docker_container,
                                               StringUtil.get_command_for_console(COMMAND_TO_GET_IP_ADDRESS)))
        Logger.info(f"after executing command in terminal got next text: {ip_address}")
        ip_address = StringUtil.get_ip_address(ip_address)
        Logger.info(f"Got ip : {ip_address}")
        return ip_address

    @staticmethod
    def stop_all_docker_containers(client):
        Logger.info("Stop all containers")
        for container in client.containers.list():
            container.stop()

    @staticmethod
    def create_docker_client():
        Logger.info("Connect to docker")
        return docker.from_env()
