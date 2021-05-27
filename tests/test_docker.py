import allure
import pytest

from api.docker_api import DockerApi
from tests.test_data import DOCKER_CONTAINER


@pytest.fixture(scope="function")
def create_container():
    with allure.step("creating image"):
        client = DockerApi.create_docker_client()
        yield client
    with allure.step("stop containers"):
        DockerApi.stop_all_docker_containers(client)


class TestDocker:
    def test_docker(self, create_container):
        with allure.step("testing"):
            print(DockerApi.get_ip_from_docker_container(create_container, DOCKER_CONTAINER))
