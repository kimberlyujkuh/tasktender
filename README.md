# TaskTender

TaskTender is a Python-based utility designed to assist in managing and prioritizing system tasks to optimize performance on Windows. It leverages the `psutil` library to interact with system processes and provides functionalities to list, prioritize, and terminate tasks.

## Features

- **List Tasks**: Retrieve and display current system tasks along with their CPU and memory usage.
- **Prioritize Task**: Elevate the priority of a specified task to high, ensuring better allocation of CPU resources.
- **Kill Task**: Terminate a specified task by its name.

## Requirements

- Python 3.x
- `psutil` library

You can install the required library using pip:

```bash
pip install psutil
```

## Usage

1. Clone or download this repository.

2. Run the `tasktender.py` script:

```bash
python tasktender.py
```

3. The script will list all current tasks. You can modify the script to specify the task names you want to prioritize or kill by changing the `prioritize_task` and `kill_task` function calls with actual process names.

## Important Notes

- The script requires administrative privileges to change task priorities and terminate system tasks. Run your console as an administrator when executing this script.
- Be cautious when terminating tasks, as doing so may affect system stability or close important applications.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.