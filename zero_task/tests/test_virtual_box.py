from utils.terminall_command_utill import UbuntuTerminalCommand
from utils.terminal_string_util import TerminalUtil


class TestVirtualBox:
    def test_virtual_box_ubuntu(self, configure_virtual_box):
        client = configure_virtual_box
        stdin, stdout, stderr = client.exec_command(UbuntuTerminalCommand.GET_IP_ADDRESS)
        data = stdout.read() + stderr.read()
        ip_address = TerminalUtil.get_ip_address(data)
        assert TerminalUtil.check_is_ip_address(ip_address), "format of ip_address is not correct"
