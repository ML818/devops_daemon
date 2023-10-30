## This is written by chatgpt, just testing.

import psutil
import time

def monitor_resource_utilization():
    while True:
        # Get CPU utilization
        cpu_percent = psutil.cpu_percent(interval=1)
        print(f"CPU Utilization: {cpu_percent}%")

        # Get memory utilization
        memory = psutil.virtual_memory()
        memory_percent = memory.percent
        print(f"Memory Utilization: {memory_percent}%")

        # Get disk utilization
        disk = psutil.disk_usage('/')
        disk_percent = disk.percent
        print(f"Disk Utilization: {disk_percent}%")

        print("-------------------------------")

        time.sleep(1)

monitor_resource_utilization()