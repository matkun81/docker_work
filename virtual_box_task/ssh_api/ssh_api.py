import time

import paramiko
from paramiko.ssh_exception import SSHException


class SshApi:
    @staticmethod
    def create_connection(host, user_name, password, port, max_count_attempt=5, time_out=5):
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        condition = True
        attempt_count = 0
        while condition and attempt_count < max_count_attempt:
            try:
                attempt_count = attempt_count + 1
                client.connect(hostname=host, username=user_name, password=password,
                               port=port)
                condition = False
            except SSHException:
                time.sleep(time_out)
                condition = True
        return client

    @staticmethod
    def close_connection(client):
        client.close()
