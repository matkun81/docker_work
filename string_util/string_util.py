class StringUtil:
    @staticmethod
    def get_command_for_console(string):
        return string.split()

    @staticmethod
    def get_ip_address(output_from_console):
        word_before_ip = 'via'
        word_after_ip = 'dev'
        index_start_ip = output_from_console.rfind(word_before_ip)
        index_end_ip = output_from_console.find(word_after_ip)
        return output_from_console[index_start_ip+len(word_before_ip):index_end_ip-1]
