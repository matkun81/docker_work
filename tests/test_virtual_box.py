from steps import get_ip_address_vbox
from utils.terminal_string_util import TerminalUtil


class TestVirtualBox:
    def test_virtual_box_ubuntu(self, configure_virtual_box):
        client = configure_virtual_box
        ip_address = get_ip_address_vbox(client)
        assert TerminalUtil.ip_address_is_correct(ip_address), "format of ip_address is not correct"
