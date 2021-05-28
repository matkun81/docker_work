import allure
import docker
import pytest

from api.docker_api import DockerApi
from tests.test_data import DOCKER_CONTAINER


#
#
# @pytest.fixture(scope="function")
# def create_container():
#     with allure.step("creating image"):
#         client = DockerApi.create_docker_client()
#         yield client
#     with allure.step("stop containers"):
#         DockerApi.stop_all_docker_containers(client)


class TestDocker:
    def test_docker(self):
        client = docker.from_env()
        image = client.images.pull("ubuntu")
        print(image.id)
        container = client.containers.create('ubuntu',
                                             command="/bin/bash",
                                             tty=True,
                                             stdin_open=True,
                                             auto_remove=False)
        print(container.id)
        container.start()
        console_log = container.exec_run("apt update")
        print(console_log)
        console_log = container.exec_run("apt install -y python3")
        print(console_log)
        console_log = container.exec_run("python3 --version")
        print(console_log)
        console_log = container.exec_run("apt install -y git")
        print(console_log)
        console_log = container.exec_run("git --version")
        print(console_log)
        console_log = container.exec_run("mkdir -v /home/docker_task")
        print(console_log)
        console_log = container.exec_run("cd /home/docker_task")
        print(console_log)
        console_log = container.exec_run("git clone https://github.com/matkun81/get_current_ip_script.git")
        print(console_log)
        console_log = container.exec_run("cd get_current_ip_script")
        print(console_log)
        console_log = container.exec_run("python ip_addres_util.py")
        print(console_log)
        container.stop()
        container.remove()
