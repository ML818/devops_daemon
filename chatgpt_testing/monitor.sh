#!/bin/bash

while true; do
    # Get CPU utilization
    cpu_utilization=$(top -bn1 | grep "Cpu(s)" | awk '{print $2 + $4}')
    echo "CPU Utilization: $cpu_utilization%"

    # Get memory utilization
    memory_utilization=$(free | awk '/Mem/ {printf "%.2f", $3/$2 * 100}')
    echo "Memory Utilization: $memory_utilization%"

    # Get disk utilization
    disk_utilization=$(df -h / | awk 'NR==2 {print $5}')
    echo "Disk Utilization: $disk_utilization"

    echo "-------------------------------"

    sleep 1
done