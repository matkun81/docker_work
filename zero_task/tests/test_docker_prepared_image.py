from utils.terminall_command_utill import UbuntuTerminalCommand
from utils.terminal_string_util import TerminalUtil


class TestDocker:
    def test_docker(self, configure_container_prepared):
        container = configure_container_prepared
        ip_address_from_terminal = container.execute_command(UbuntuTerminalCommand.GET_IP_ADDRESS)
        ip_address = TerminalUtil.get_ip_address(ip_address_from_terminal)
        assert TerminalUtil.check_is_ip_address(ip_address), "not correct format ip address"
