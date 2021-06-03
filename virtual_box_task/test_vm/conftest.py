import time

import allure
import pytest
import virtualbox

from virtual_box_task.ssh_api.ssh_api import SshApi
from virtual_box_task.vm_config.vm_config import Machine, TIME_OUT_FOR_DOWNLOAD_OS


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

        client = SshApi.create_connection(Machine.HOST, Machine.USER_NAME, Machine.PASSWORD,
                                          Machine.PORT_SSH)
    yield client

    with allure.step("power down Virtual Box"):
        SshApi.close_connection(client)
        session_in_vm.console.power_down()
