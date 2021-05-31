import allure
import pytest

from api.docker_api import ContainerApi
from api.docker_api_utils import DockerApiUtils
from exception.exception import TerminalCommandException
from project_utils.logger import Logger
from ubuntu_api.data_for_ubuntu_terminal_work import DOCKER_IMAGE, UbuntuTerminalCommand


@pytest.fixture(scope="class")
def configure_container():
    with allure.step("creating image"):
        image = DockerApiUtils.create_image(DOCKER_IMAGE)
        container = ContainerApi(image)
        container.start()
        try:
            container.execute_command(UbuntuTerminalCommand.UPDATE_APT)
            container.execute_command(UbuntuTerminalCommand.INSTALL_PYTHON)
            container.execute_command(UbuntuTerminalCommand.INSTALL_GIT)
        except TerminalCommandException:
            Logger.error("Wrong command tr")
            container.stop()
    yield container
    with allure.step("stop containers"):
        container.stop()
        DockerApiUtils.get_list_images()
