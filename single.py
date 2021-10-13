from fabric import Connection

def disk_free(c):
    uname = c.run('uname -s',hide=True)
    if 'Linux' in uname.stdout:
        command = "df -h / | tail -n1 | awk '{print $5}'"
        return c.run(command,hide=True).stdout.strip()
    else:
        print("Linux not found in uname")


print(disk_free(Connection('192.168.121.157')))
