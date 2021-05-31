DOCKER_IMAGE = "ubuntu"
GIT_REPOSITORY = "https://github.com/matkun81/get_current_ip_script.git"
PATH_TO_SCRIPT = "/get_current_ip_script/ip_addres_util.py"


class UbuntuTerminalCommand:
    UPDATE_APT = "apt update"
    INSTALL_PYTHON = "apt install -y python3"
    CHECK_PYTHON_VERSION = "python3 --version"
    INSTALL_GIT = "apt install -y git"
    CHECK_GIT_VERSION = "git --version"
    GET_IP_ADDRESS = "hostname -I"


class GitCommandTerminal:
    CLONE_REPOSITORY = f"git clone {GIT_REPOSITORY}"


class PythonCommandTerminal:
    EXECUTE_PYTHON_FILE = f"python3 {PATH_TO_SCRIPT}"
