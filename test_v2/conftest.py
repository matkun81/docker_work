import allure
import pytest

from api.docker_api import ContainerApi
from api.docker_api_utils import DockerApiUtils
from ubuntu_api.data_for_ubuntu_terminal_work import DOCKER_IMAGE


@pytest.fixture(scope="class")
def configure_container():
    with allure.step("creating image"):
        image = DockerApiUtils.create_image(DOCKER_IMAGE)
        container = ContainerApi(image)
        container.start()
    yield container
    with allure.step("stop containers"):
        container.stop()
        DockerApiUtils.get_list_images()
