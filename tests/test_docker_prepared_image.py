from steps import get_ip_address_in_terminal
from utils.terminal_string_util import TerminalUtil


class TestDocker:
    def test_docker(self, configure_container_prepared):
        container = configure_container_prepared
        ip_address = get_ip_address_in_terminal(container)
        assert TerminalUtil.ip_address_is_correct(ip_address), "not correct format ip address"
