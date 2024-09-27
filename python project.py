import time
import random

class VirtualMachine:
    def __init__(self, name, cpu_limit, memory_limit):
        self.name = name
        self.cpu_limit = cpu_limit
        self.memory_limit = memory_limit
        self.cpu_usage = 0
        self.memory_usage = 0

    def allocate_resources(self, cpu, memory):
        if cpu <= self.cpu_limit and memory <= self.memory_limit:
            self.cpu_usage += cpu
            self.memory_usage += memory
            print(f"Allocated {cpu} CPU and {memory} MB Memory to {self.name}.")
        else:
            print(f"Resource allocation exceeds limits for {self.name}.")

    def deallocate_resources(self, cpu, memory):
        self.cpu_usage = max(0, self.cpu_usage - cpu)
        self.memory_usage = max(0, self.memory_usage - memory)
        print(f"Deallocated {cpu} CPU and {memory} MB Memory from {self.name}.")

    def monitor_resources(self):
        print(f"Monitoring {self.name}: CPU Usage: {self.cpu_usage}/{self.cpu_limit}, "
              f"Memory Usage: {self.memory_usage}/{self.memory_limit}")
        if self.cpu_usage > self.cpu_limit * 0.8:
            self.send_alert("CPU usage exceeded 80% of the limit.")
        if self.memory_usage > self.memory_limit * 0.8:
            self.send_alert("Memory usage exceeded 80% of the limit.")

    def send_alert(self, message):
        print(f"ALERT: {message}")

class CloudResourceManager:
    def __init__(self):
        self.virtual_machines = {}

    def create_vm(self, name, cpu_limit, memory_limit):
        vm = VirtualMachine(name, cpu_limit, memory_limit)
        self.virtual_machines[name] = vm
        print(f"Created VM: {name}")

    def delete_vm(self, name):
        if name in self.virtual_machines:
            del self.virtual_machines[name]
            print(f"Deleted VM: {name}")
        else:
            print(f"VM {name} not found.")

    def monitor_all_vms(self):
        for vm in self.virtual_machines.values():
            vm.monitor_resources()

# Example usage
if __name__ == "__main__":
    manager = CloudResourceManager()
    manager.create_vm("VM1", 4, 8192)  # 4 CPUs, 8192 MB Memory
    manager.create_vm("VM2", 2, 4096)   # 2 CPUs, 4096 MB Memory

    # Simulate resource allocation
    vm1 = manager.virtual_machines["VM1"]
    vm1.allocate_resources(3, 6000)
    vm1.monitor_resources()

    # Simulate resource monitoring
    time.sleep(1)  # Simulate time delay
    manager.monitor_all_vms()

    # Deallocate resources
    vm1.deallocate_resources(1, 2000)
    manager.monitor_all_vms()

    # Delete a VM
    manager.delete_vm("VM2")
