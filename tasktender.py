import psutil
import os
import ctypes
from collections import namedtuple

# Define a namedtuple to store task information
TaskInfo = namedtuple('TaskInfo', ['pid', 'name', 'cpu_usage', 'memory_usage'])

class TaskTender:
    def __init__(self):
        self.tasks = []

    def fetch_tasks(self):
        """Fetch the list of current system tasks."""
        self.tasks.clear()
        for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
            try:
                task_info = TaskInfo(
                    pid=proc.info['pid'],
                    name=proc.info['name'],
                    cpu_usage=proc.info['cpu_percent'],
                    memory_usage=proc.info['memory_percent']
                )
                self.tasks.append(task_info)
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass

    def prioritize_task(self, task_name):
        """Set the priority of a task to high."""
        for task in self.tasks:
            if task.name == task_name:
                try:
                    p = psutil.Process(task.pid)
                    p.nice(psutil.HIGH_PRIORITY_CLASS)
                    print(f"Priority of '{task_name}' set to high.")
                except (psutil.NoSuchProcess, psutil.AccessDenied):
                    print(f"Could not change priority for '{task_name}'.")
                return
        print(f"Task '{task_name}' not found.")

    def list_tasks(self):
        """Print the list of tasks with their CPU and memory usage."""
        self.fetch_tasks()
        print(f"{'PID':<10} {'Name':<25} {'CPU%':<10} {'Memory%':<10}")
        for task in self.tasks:
            print(f"{task.pid:<10} {task.name:<25} {task.cpu_usage:<10} {task.memory_usage:<10}")

    def kill_task(self, task_name):
        """Terminate a task by name."""
        for task in self.tasks:
            if task.name == task_name:
                try:
                    p = psutil.Process(task.pid)
                    p.terminate()
                    print(f"Task '{task_name}' terminated.")
                except (psutil.NoSuchProcess, psutil.AccessDenied):
                    print(f"Could not terminate '{task_name}'.")
                return
        print(f"Task '{task_name}' not found.")

if __name__ == "__main__":
    task_tender = TaskTender()
    task_tender.list_tasks()
    task_tender.prioritize_task("example.exe")  # Replace with actual task name
    task_tender.kill_task("example.exe")        # Replace with actual task name