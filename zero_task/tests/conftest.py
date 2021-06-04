import time

import allure
import pytest
import virtualbox

from config.vm_config import Machine, TIME_OUT_FOR_DOWNLOAD_OS
from utils.docker_api_utils import DockerApiUtils
from utils.logger_util import Logger
from utils.ssh_api_util import SshApiUtil
from utils.terminall_command_utill import DOCKER_IMAGE, UbuntuTerminalCommand, TerminalCommandException
from zero_task.container_api import ContainerApi


@pytest.fixture(scope="class")
def configure_container_empty_image():
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


@pytest.fixture(scope="class")
def configure_container_prepared():
    with allure.step("creating image"):
        image = DockerApiUtils.create_image(DOCKER_IMAGE)
        container = ContainerApi(image)
        container.start()

    yield container

    with allure.step("stop containers"):
        container.stop()
        DockerApiUtils.get_list_images()


@pytest.fixture(scope="class")
def configure_virtual_box():
    with allure.step("launch virtual machine"):
        vbox = virtualbox.VirtualBox()
        vbox_session = virtualbox.Session()
        vm = vbox.find_machine(Machine.NAME)
        _powered_up = False

        if vm.state < virtualbox.library.MachineState.running:
            _powered_up = True
            progress = vm.launch_vm_process(vbox_session, "headless", [])
            progress.wait_for_completion()
        session_in_vm = vm.create_session()

        time.sleep(TIME_OUT_FOR_DOWNLOAD_OS)

        client = SshApiUtil.create_connection(Machine.HOST, Machine.USER_NAME, Machine.PASSWORD,
                                              Machine.PORT_SSH)
    yield client

    with allure.step("power down Virtual Box"):
        SshApiUtil.close_connection(client)
        session_in_vm.console.power_down()
