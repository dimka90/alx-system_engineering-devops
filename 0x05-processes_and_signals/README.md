# 0x05. Processes and Signals

This repository contains information and examples related to processes and signals in Unix-like operating systems, with a focus on Bash scripting.

## Table of Contents

1. [Introduction](#introduction)
2. [PID (Process ID)](#pid-process-id)
3. [Process Management](#process-management)
    - [Listing Processes (`ps`)](#listing-processes-ps)
    - [Finding Processes (`pgrep`)](#finding-processes-pgrep)
    - [Killing Processes (`pkill` and `kill`)](#killing-processes-pkill-and-kill)
4. [Exit Codes and `exit`](#exit-codes-and-exit)
5. [Signal Handling (`trap`)](#signal-handling-trap)
6. [Examples](#examples)
7. [References](#references)

## Introduction

Processes and signals are fundamental concepts in Unix-based operating systems. Understanding how to manage processes and handle signals is crucial for system administrators and developers. This repository provides an overview of key concepts and practical examples related to processes and signals in the context of Bash scripting.

## PID (Process ID)

A Process ID (PID) is a unique numerical identifier assigned to each running process on a Unix-like system. It is used to track and manage processes. In Bash scripting, you can access the PID of the current script using the special variable `$$`.

```bash
echo "My script's PID is $$"
```

## Process Management

### Listing Processes (`ps`)

The `ps` command is used to list information about running processes. It provides details such as PIDs, resource usage, and status.

```bash
# List all processes running on the system
ps aux
```

### Finding Processes (`pgrep`)

The `pgrep` command is used to search for processes by name and retrieve their PIDs. It is useful for finding the PID of a process when you know its name.

```bash
# Find the PID of a process by name
pgrep process_name
```

### Killing Processes (`pkill` and `kill`)

- `pkill`: The `pkill` command allows you to send signals to processes based on their names, making it easy to terminate or signal multiple processes at once.

```bash
# Terminate all processes with a specific name
pkill process_name
```

- `kill`: The `kill` command is used to send signals to processes. It can be used to gracefully terminate processes by sending a SIGTERM signal (signal number 15) or forcefully terminate them using SIGKILL (signal number 9).

```bash
# Send SIGTERM (15) to a process by PID
kill -15 PID

# Forcefully terminate a process by PID using SIGKILL (9)
kill -9 PID
```

## Exit Codes and `exit`

The `exit` command is used to exit a Bash script or shell with a specified exit status. Typically, an exit status of 0 indicates success, while non-zero values indicate failure.

```bash
# Exit a script with a success status (0)
exit 0

# Exit a script with an error status (non-zero)
exit 1
```

## Signal Handling (`trap`)

The `trap` command is used to set up signal handlers in a Bash script. Signal handlers define actions to be taken when a specific signal is received by the script. This is useful for handling signals like SIGINT (e.g., Ctrl+C) gracefully.

```bash
# Define a custom action when the script receives SIGINT (Ctrl+C)
trap 'echo "Script interrupted by user"; exit 1' SIGINT
```

## Examples

This repository provides examples and code snippets to illustrate the concepts discussed in this README. You can find these examples in the accompanying files.

## References

For further information and in-depth documentation on processes and signals, refer to the following resources:

- [GNU Core Utilities Manual - ps](https://www.gnu.org/software/coreutils/manual/coreutils.html#ps-invocation)
- [Linux man pages - kill](https://linux.die.net/man/1/kill)
- [Bash Reference Manual - Signals](https://www.gnu.org/software/bash/manual/html_node/Signals.html)
```

Feel free to modify and expand this `README.md` to suit your specific needs, and include more detailed explanations, code examples, or references as necessary.
