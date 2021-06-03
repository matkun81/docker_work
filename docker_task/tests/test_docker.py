from ubuntu_api.data_for_ubuntu_terminal_work import GitCommandTerminal, PythonCommandTerminal
from ubuntu_api.terminal_util.terminal_util import TerminalUtil


class TestDocker:
    def test_docker(self, configure_container):
        container = configure_container
        container.execute_command(GitCommandTerminal.CLONE_REPOSITORY)
        ip_address_from_terminal = container.execute_command(PythonCommandTerminal.EXECUTE_PYTHON_FILE)
        ip_address = TerminalUtil.get_ip_address(ip_address_from_terminal, count_symbol_from_start=2,
                                                 count_symbol_from_end=3)
        assert TerminalUtil.check_is_ip_address(ip_address), "not correct format ip address"
