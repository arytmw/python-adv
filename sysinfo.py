import platform
import time
import subprocess
import psutil #sudo pip3.6 install psutil
import humanize #sudo pip3.6 install humanize

print("="*40, "SYSTEM INFORMATION", "="*40)
uname = platform.uname()
boot_time_timestamp = psutil.boot_time()
print(f"Name: {uname.node}")
print(f"System: {uname.system}")
print(f"Kernel: {uname.release}")
print(f"Architecture: {uname.machine}")
print(f"Boot Time: {time.ctime(boot_time_timestamp)}")

print("="*40, "CPU INFORMATION", "="*40)
cpufreq = psutil.cpu_freq()
print(f"Physical Cores: {psutil.cpu_count(logical=False)}")
print(f"Total Cores: {psutil.cpu_count(logical=True)}")
print(f"Current CPU frequency: {cpufreq.current} Mhz")
print(f"Total CPU Usage: {psutil.cpu_percent()} %")

print("="*40, "MEMORY INFORMATION", "="*40)
sysmem = psutil.virtual_memory()
print(f"Total Memory: {humanize.naturalsize(sysmem.total)}")
print(f"Available Memory: {humanize.naturalsize(sysmem.available)}")
print(f"Used Memory: {humanize.naturalsize(sysmem.used)}")
print(f"Memory Usage: {sysmem.percent} %")

print("="*40, "SWAP INFORMATION", "="*40)
swap = psutil.swap_memory()
print(f"Total Swap: {humanize.naturalsize(swap.total)}")
print(f"Available Swap: {humanize.naturalsize(swap.free)}")
print(f"Used Swap: {humanize.naturalsize(swap.used)}")
print(f"Swap Usage: {swap.percent} %")

print("="*40, "DISK INFORMATION", "="*40)
partitions = psutil.disk_partitions()
for partition in partitions:
    print(f"Device: {partition.device}")
    print(f"MountPoint: {partition.mountpoint}")
    print(f"Filesystem: {partition.fstype}")
    partition_usage = psutil.disk_usage(partition.mountpoint)
    print(f"Total Size: {humanize.naturalsize(partition_usage.total)}")
    print(f"Used Size: {humanize.naturalsize(partition_usage.used)}")
    print(f"Available Size: {humanize.naturalsize(partition_usage.free)}")
    print(f"Percentage Usage: {partition_usage.percent} %")
    print("-----------")

print("="*40, "NETWORK INFORMATION", "="*40)
if_addrs = psutil.net_if_addrs()
for interface_name, interface_addresses in if_addrs.items():
    print(f"Interface Name: {interface_name}")
    for address in interface_addresses:
       if str(address.family) == "AddressFamily.AF_INET":
            print(f"IP Address: {address.address}")
            print(f"NetMask: {address.netmask}")
            print(f"Broadcast: {address.broadcast}")
            print("---------")

print("="*40, "PROCESS INFORMATION", "="*40)
command = ['ps','-eo','pid,ppid,cmd,%mem,%cpu','--sort=-%mem','| head']
process = subprocess.Popen(command,shell=True,stdout=subprocess.PIPE)
stdout_list = process.communicate()[0]
print(stdout_list.decode())
