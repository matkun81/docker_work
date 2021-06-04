from utils.logger_util import Logger
from utils.terminall_command_utill import TerminalCommandException


class ContainerApi:
    def __init__(self, container):
        self.container = container

    def start(self):
        Logger.info(f"Container started: {self.container.name}\n"
                    f"Container status - {self.container.status}\n")
        self.container.start()

    def stop(self):
        self.container.stop()
        Logger.info(f"Container stop: {self.container.name}\n")

    def execute_command(self, command):
        command_execute_is_success = 0
        log = self.container.exec_run(command)
        Logger.info(f"Terminal command executed :{log.output}")
        if log.exit_code != command_execute_is_success:
            Logger.error(f"Terminal command was not executed!\n Check {log.output}")
            raise TerminalCommandException("Wrong command!")
        return log.output
