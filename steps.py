import allure

from utils.terminal_string_util import TerminalUtil
from utils.terminall_command_utill import PythonCommandTerminal, GitCommandTerminal, UbuntuTerminalCommand


@allure.step("get ip address from virtual box")
def get_ip_address_vbox(client):
    stdin, stdout, stderr = client.exec_command(UbuntuTerminalCommand.GET_IP_ADDRESS)
    data = stdout.read() + stderr.read()
    return TerminalUtil.get_ip_address(data)


@allure.step("get ip address from docker using python script")
def get_ip_address_using_script(container):
    container.execute_command(GitCommandTerminal.CLONE_REPOSITORY)
    ip_address_from_terminal = container.execute_command(PythonCommandTerminal.EXECUTE_PYTHON_FILE)
    return TerminalUtil.get_ip_address(ip_address_from_terminal, count_symbol_from_start=2,
                                       count_symbol_from_end=3)


@allure.step("get ip address from docker using terminal")
def get_ip_address_in_terminal(container):
    ip_address_from_terminal = container.execute_command(UbuntuTerminalCommand.GET_IP_ADDRESS)
    return TerminalUtil.get_ip_address(ip_address_from_terminal)
