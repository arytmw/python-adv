from fabric import Connection

host = '192.168.121.157'
cmd = 'df -h'

result = Connection(host).run(cmd,hide=True)
print(result.stdout)
