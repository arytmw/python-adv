from paramiko import SSHClient #pip3.6 install paramiko
from paramiko.client import AutoAddPolicy
import sys

def ssh():
    client = SSHClient()
    client.set_missing_host_key_policy(AutoAddPolicy)
    client.connect(sys.argv[1],username=sys.argv[2],password=sys.argv[3]) #port=23 key_file=/root/.ssh/id_rsa
    stdin, stdout, stderr = client.exec_command(sys.argv[4])
    output = stdout.read()
    print(output.decode())
    client.close()

ssh()
