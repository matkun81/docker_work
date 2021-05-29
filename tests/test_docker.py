from tests.data_for_ubuntu_terminal_work import GitCommandTerminal, PythonCommandTerminal


class TestDocker:
    def test_docker(self, configure_container):
        container = configure_container
        container.execute_command(GitCommandTerminal.CLONE_REPOSITORY)
        container.execute_command(PythonCommandTerminal.EXECUTE_PYTHON_FILE)
