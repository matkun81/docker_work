import re

from const.regular_exspressions import IP_ADDRESS_REG_EXP


class TerminalUtil:
    @staticmethod
    def get_ip_address(ip_from_terminal, count_symbol_from_start, count_symbol_from_end):
        ip_address = str(ip_from_terminal)
        return ip_address[count_symbol_from_start:-count_symbol_from_end]

    @staticmethod
    def check_is_ip_address(string):
        return re.match(IP_ADDRESS_REG_EXP, string)
