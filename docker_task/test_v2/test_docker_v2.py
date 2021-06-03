from ubuntu_api.data_for_ubuntu_terminal_work import UbuntuTerminalCommand
from ubuntu_api.terminal_util.terminal_util import TerminalUtil


class TestDocker:
    def test_docker(self, configure_container):
        container = configure_container
        ip_address_from_terminal = container.execute_command(UbuntuTerminalCommand.GET_IP_ADDRESS)
        ip_address = TerminalUtil.get_ip_address(ip_address_from_terminal)
        assert TerminalUtil.check_is_ip_address(ip_address), "not correct format ip address"
