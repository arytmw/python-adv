from fabric import Connection
from fabric import SerialGroup

def disk_free(c):
    uname = c.run('uname -s',hide=True)
    if 'Linux' in uname.stdout:
        command = "free -h"
        return c.run(command,hide=True).stdout.strip()
    else:
        print("Linux not found in uname")


for conn in SerialGroup('192.168.121.157','192.168.121.163'):
    print(f"{conn} : {disk_free(conn)}")


#192.168.121.157 : 48%
