from paramiko import SSHClient #pip3.6 install paramiko
from paramiko.client import AutoAddPolicy
import getpass #pip3.6 install getpass3

hostname = input("Enter  hostname or IP: ")
user_name = input("Enter username: ")
passwd = getpass.getpass("Enter password: ")
command = input("Enter command to run: ")

def ssh():
    client = SSHClient()
    client.set_missing_host_key_policy(AutoAddPolicy)
    client.connect(hostname,username=user_name,password=passwd) #port=23 key_file=/root/.ssh/id_rsa
    stdin, stdout, stderr = client.exec_command(command)
    output = stdout.read()
    print(output.decode())
    client.close()

ssh()
