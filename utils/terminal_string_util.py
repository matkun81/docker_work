import re

from regular_exspressions import IP_ADDRESS_REG_EXP
from utils.logger_util import Logger


class TerminalUtil:
    @staticmethod
    def get_ip_address(ip_from_terminal, count_symbol_from_start=2, count_symbol_from_end=4):
        ip_address = str(ip_from_terminal)
        return ip_address[count_symbol_from_start:-count_symbol_from_end]

    @staticmethod
    def ip_address_is_correct(string):
        Logger.info(f" Ip address : {string}")
        Logger.info("Check the ip address")
        return re.match(IP_ADDRESS_REG_EXP, string)
