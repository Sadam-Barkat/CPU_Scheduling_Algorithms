import time
import os

def fcfs():
    burst_time = []  # Changed from np.array([]) to an empty list
    arival_time = []
    completion_times = []  # Changed from np.array([]) to an empty list
    waiting_time = []  # Changed from np.array([0]) to a list
    turnaround_time = []
    current_time = 0
    color = 90

    cap = int(input("Enter the number of processes: "))
    for i in range(cap):
        at = int(input(f"Enter the arival time for p{i + 1}: "))
        bt = int(input(f"Enter the burst time for p{i + 1}: "))
        arival_time.append(at)
        burst_time.append(bt)  # Use append to add to the list

    os.system("cls")

    ct = 0
    for i in range(cap):
        ct = max(ct, arival_time[i]) + burst_time[i]
        completion_times.append(ct)
    tat = 0
    for i in range(cap):
        tat = completion_times[i] - arival_time[i]
        turnaround_time.append(tat)
    wt = 0
    for i in range(cap):
        wt = turnaround_time[i] - burst_time[i]
        waiting_time.append(wt)

    print("\n***************(FIRST COME FIRST SERVER ALGORITHM)*************\n")

    print(f"\n{'Process':<9}{'A.T':<10}{'B.T':<10}{'C.T':<10}{'TAT':<10}{'W.T':<10}")
    for i in range(cap):
        print(
            f"p{i + 1:<8}{arival_time[i]:<10}{burst_time[i]:<10}{completion_times[i]:<10}{turnaround_time[i]:<10}{waiting_time[i]:<10}")

    print("Average Turnaround Time :", sum(turnaround_time)/len(turnaround_time))
    print("Average Waiting Time :", sum(waiting_time)/len(waiting_time))

    for i in range(cap):
        print(f"P{i + 1}", end=" " * int(burst_time[i] - 1), flush=True)
        time.sleep(0.25)
    print()
    for i in range(cap):
        print("|", end="")
        for _ in range(int(burst_time[i])):
            print(f"\033[{color}m*\033[0m", end="", flush=True)
            time.sleep(0.25)
        color += 1
        if color == 97:
            color = 30
    print("|")

    print(min(arival_time), end="", flush=True)
    for i in range(cap):
        if completion_times[i] < 10:
            time.sleep(0.5)
            print(" " * (burst_time[i] - 1), completion_times[i], end="", flush=True)
        else:
            time.sleep(0.5)
            print(" " * (burst_time[i] - 2), completion_times[i], end="", flush=True)
    print()

#=======================================================================================================================
from collections import deque

def sjf():
    n = int(input("Enter the number of processes: "))
    arrival_times = []
    burst_times = []
    completion_times = [0] * n
    waiting_times = [0] * n
    turnaround_times = [0] * n
    gant_chart_list = []
    process_time = []
    color = 90

    # Input arrival times and burst times
    for i in range(n):
        at = int(input(f"Arrival time of P{i + 1}: "))
        bt = int(input(f"Burst time of P{i + 1}: "))
        arrival_times.append(at)
        burst_times.append(bt)

    current_time = 0
    completed = 0
    queue = deque()  # Queue to store processes ready for execution

    while completed < n:
        # Add newly arrived processes to the queue
        for i in range(n):
            if arrival_times[i] <= current_time and i not in queue and completion_times[i] == 0:
                queue.append(i)

        # If queue is not empty, sort it by burst time (shortest burst time first)
        if queue:
            # Sort by burst time, then by arrival time (in case of tie)
            queue = deque(sorted(queue, key=lambda x: (burst_times[x], arrival_times[x])))

            # Get the process with the shortest burst time
            current_process = queue.popleft()
            gant_chart_list.append(current_process + 1)

            # Execute the process for its full burst time
            current_time += burst_times[current_process]
            completion_times[current_process] = current_time
            process_time.append(current_time)
            completed += 1

        else:
            # If no process is ready, move time forward
            current_time += 1

    # Calculate turnaround and waiting times
    for i in range(n):
        turnaround_times[i] = completion_times[i] - arrival_times[i]
        waiting_times[i] = turnaround_times[i] - burst_times[i]

    # Print results
    print(f"\n{'Process':<9}{'A.T':<10}{'B.T':<10}{'C.T':<10}{'TAT':<10}{'W.T':<10}")
    for i in range(n):
        print(
            f"P{i + 1:<8}{arrival_times[i]:<10}{burst_times[i]:<10}{completion_times[i]:<10}{turnaround_times[i]:<10}{waiting_times[i]:<10}")

    # Calculate and print average turnaround and waiting times
    avg_tat = sum(turnaround_times) / n
    avg_wt = sum(waiting_times) / n
    print(f"\nAverage Turnaround Time: {avg_tat:.2f}")
    print(f"Average Waiting Time: {avg_wt:.2f}")

    # Gantt Chart Display (text-based)
    for i in range(n):
        print(f"P{gant_chart_list[i]}", end=" " * int(burst_times[i] - 1), flush=True)
        time.sleep(0.25)
    print()
    for i in range(n):
        print("|", end="")
        for _ in range(int(burst_times[i])):
            print(f"\033[{color}m*\033[0m", end="", flush=True)
            time.sleep(0.25)
        color += 1
        if color == 97:
            color = 30
    print("|")

    # Print time line for the Gantt chart
    print(min(arrival_times), end="", flush=True)
    for i in range(n):
        if process_time[i] < 10:
            time.sleep(0.5)
            print(" " * (burst_times[i] - 1), process_time[i], end="", flush=True)
        else:
            time.sleep(0.5)
            print(" " * (burst_times[i] - 2), process_time[i], end="", flush=True)
    print()

#=======================================================================================================================

from collections import deque

def pb():
    n = int(input("Enter the number of processes: "))
    arrival_times = []
    burst_times = []
    priorities = []
    completion_times = [0] * n
    waiting_times = [0] * n
    turnaround_times = [0] * n
    gant_chart_list = []
    process_time = []
    color = 90

    # Input arrival times, burst times, and priorities
    for i in range(n):
        at = int(input(f"Arrival time of P{i + 1}: "))
        bt = int(input(f"Burst time of P{i + 1}: "))
        p = int(input(f"Lower the number heigher the periorty P{i + 1}: "))
        arrival_times.append(at)
        burst_times.append(bt)
        priorities.append(p)

    current_time = 0
    completed = 0
    queue = deque()  # Queue to store processes ready for execution

    while completed < n:
        # Add newly arrived processes to the queue
        for i in range(n):
            if arrival_times[i] <= current_time and arrival_times[i] not in queue and completion_times[i] == 0:
                queue.append(arrival_times[i])

        # If queue is not empty, sort it by priority (higher priority comes first)
        if queue:
            queue = deque(sorted(queue, key=lambda x: (priorities[arrival_times.index(x)], arrival_times[arrival_times.index(x)])))

            # Get the process with the highest priority (lowest priority number)
            current_process = queue.popleft()
            gant_chart_list.append(arrival_times.index(current_process) + 1)

            # Execute the process for its full burst time
            current_time += burst_times[arrival_times.index(current_process)]
            completion_times[arrival_times.index(current_process)] = current_time
            process_time.append(current_time)
            completed += 1

        else:
            # If no process is ready, move time forward
            current_time += 1

    # Calculate turnaround and waiting times
    for i in range(n):
        turnaround_times[i] = completion_times[i] - arrival_times[i]
        waiting_times[i] = turnaround_times[i] - burst_times[i]

    # Print results
    print(f"\n{'Process':<9}{'A.T':<10}{'B.T':<10}{'C.T':<10}{'TAT':<10}{'W.T':<10}{'PE':<10}")
    for i in range(n):
        print(
            f"P{i + 1:<8}{arrival_times[i]:<10}{burst_times[i]:<10}{completion_times[i]:<10}{turnaround_times[i]:<10}{waiting_times[i]:<10}{priorities[i]:<10}")

    # Calculate and print average turnaround and waiting times
    avg_tat = sum(turnaround_times) / n
    avg_wt = sum(waiting_times) / n
    print(f"\nAverage Turnaround Time: {avg_tat:.2f}")
    print(f"Average Waiting Time: {avg_wt:.2f}")

    for i in range(n):
        print(f"P{gant_chart_list[i]}", end=" " * int(burst_times[i] - 1), flush=True)
        time.sleep(0.25)
    print()
    for i in range(n):
        print("|", end="")
        for _ in range(int(burst_times[i])):
            print(f"\033[{color}m*\033[0m", end="", flush=True)
            time.sleep(0.25)
        color += 1
        if color == 97:
            color = 30
    print("|")

    print(min(arrival_times), end="", flush=True)
    for i in range(n):
        if process_time[i] < 10:
            time.sleep(0.5)
            print(" " * (burst_times[i] - 1), process_time[i], end="", flush=True)
        else:
            time.sleep(0.5)
            print(" " * (burst_times[i] - 2), process_time[i], end="", flush=True)
    print()
#=======================================================================================================================

def rr():
    arrival_times = []
    burst_times = []
    waiting_times = []
    turnaround_times = []
    queue = []
    current_time = 0
    gant_chart_list = []
    process_time = []
    color = 90
    n = int(input("Enter the number of processes: "))
    time_quantum = int(input("Enter the time quantum: "))

    for i in range(n):
        at = int(input(f"Arrival time of P{i + 1}: "))
        bt = int(input(f"Burst time of P{i + 1}: "))
        arrival_times.append(at)
        burst_times.append(bt)

    remaining_times = burst_times[:]
    completion_times = [0] * n
    for i in range(n):
        if arrival_times[i] <= current_time:
            queue.append(i)

    while queue:
        current_process = queue.pop(0)
        gant_chart_list.append(current_process + 1)

        if remaining_times[current_process] > time_quantum:
            current_time += time_quantum
            remaining_times[current_process] -= time_quantum

            process_time.append(current_time)
        else:
            current_time += remaining_times[current_process]
            remaining_times[current_process] = 0
            completion_times[current_process] = current_time

            process_time.append(current_time)

        for i in range(n):
            if arrival_times[i] <= current_time and i not in queue and remaining_times[i] > 0:
                if i != current_process:
                    queue.append(i)
        if remaining_times[current_process] > 0:
            queue.append(current_process)

    for i in range(n):
        tat = completion_times[i] - arrival_times[i]
        wt = tat - burst_times[i]
        turnaround_times.append(tat)
        waiting_times.append(wt)
    # Print results
    print(f"\n{'Process':<9}{'A.T':<10}{'B.T':<10}{'C.T':<10}{'TAT':<10}{'W.T':<10}")
    for i in range(n):
        print(f"P{i + 1:<8}{arrival_times[i]:<10}{burst_times[i]:<10}{completion_times[i]:<10}{turnaround_times[i]:<10}{waiting_times[i]:<10}")

    # Calculate and print average turnaround and waiting times
    avg_tat = sum(turnaround_times) / n
    avg_wt = sum(waiting_times) / n
    print(f"\nAverage Turnaround Time: {avg_tat:.2f}")
    print(f"Average Waiting Time: {avg_wt:.2f}")

    # Gantt Chart Display (text-based)
    for i in range(len(gant_chart_list)):
        print(f"P{gant_chart_list[i]}", end=" " * 2, flush=True)
        time.sleep(0.25)
    print()
    for i in range(len(gant_chart_list)):
        print("|", end="")
        for i in range(1):
            print(" ", f"\033[{color}m*\033[0m", end="", flush=True)
            time.sleep(0.25)
        color += 1
        if color == 97:
            color = 30
    print("|")

    # Print time line for the Gantt chart
    print(min(arrival_times), end=" ", flush=True)
    for pt in process_time:
        if pt < 10:
            time.sleep(0.5)
            print(" " * 2, pt, end="", flush=True)
        else:
            time.sleep(0.5)
            print(" " * 1, pt, end="", flush=True)
    print()


#=======================================================================================================================

from collections import deque

def sjf_preemptive():
    n = int(input("Enter the number of processes: "))
    arrival_times = []
    burst_times = []
    remaining_times = []
    completion_times = [0] * n
    waiting_times = [0] * n
    turnaround_times = [0] * n
    gant_chart_list = []
    process_time = []
    color = 90

    # Input arrival and burst times
    for i in range(n):
        at = int(input(f"Arrival time of P{i + 1}: "))
        bt = int(input(f"Burst time of P{i + 1}: "))
        arrival_times.append(at)
        burst_times.append(bt)
        remaining_times.append(bt)

    current_time = 0
    completed = 0
    queue = deque()  # Queue to store the indices of processes

    while completed < n:
        # Add newly arrived processes to the queue (if not already in it)
        for i in range(n):
            if arrival_times[i] <= current_time and i not in queue and remaining_times[i] > 0:
                queue.append(i)

        # Sort the queue based on remaining burst time (SJF logic)
        queue = deque(sorted(queue, key=lambda x: (remaining_times[x], arrival_times[x])))

        if not queue:
            # If no processes are ready, move the time forward
            current_time += 1
            continue

        # Get the process with the shortest remaining time from the queue
        current_process = queue.popleft()
        gant_chart_list.append(arrival_times.index(arrival_times[current_process]) + 1)

        # Execute the process for 1 time unit
        remaining_times[current_process] -= 1
        current_time += 1
        process_time.append(current_time)

        # If the process finishes, calculate completion time
        if remaining_times[current_process] == 0:
            completed += 1
            completion_times[current_process] = current_time
        else:
            # Add the current process back to the queue for further execution
            queue.append(current_process)

    # Calculate turnaround and waiting times
    for i in range(n):
        turnaround_times[i] = completion_times[i] - arrival_times[i]
        waiting_times[i] = turnaround_times[i] - burst_times[i]

    # Print results
    print(f"\n{'Process':<9}{'A.T':<10}{'B.T':<10}{'C.T':<10}{'TAT':<10}{'W.T':<10}")
    for i in range(n):
        print(f"P{i + 1:<8}{arrival_times[i]:<10}{burst_times[i]:<10}{completion_times[i]:<10}{turnaround_times[i]:<10}{waiting_times[i]:<10}")

    # Calculate and print average turnaround and waiting times
    avg_tat = sum(turnaround_times) / n
    avg_wt = sum(waiting_times) / n
    print(f"\nAverage Turnaround Time: {avg_tat:.2f}")
    print(f"Average Waiting Time: {avg_wt:.2f}")

    for i in range(len(gant_chart_list)):
        print(f"P{gant_chart_list[i]}", end=" " * 2, flush=True)
        time.sleep(0.25)
    print()
    for i in range(len(gant_chart_list)):
        print("|", end="")
        for i in range(1):
            print(" ", f"\033[{color}m*\033[0m", end="", flush=True)
            time.sleep(0.25)
        color += 1
        if color == 97:
            color = 30
    print("|")

    print(min(arrival_times), end=" ", flush=True)
    for pt in process_time:
        if pt < 10:
            time.sleep(0.5)
            print(" " * 2, pt, end="", flush=True)
        else:
            time.sleep(0.5)
            print(" " * 1, pt, end="", flush=True)
    print()
#=======================================================================================================================

from collections import deque

def pb_preemptive():
    n = int(input("Enter the number of processes: "))
    arrival_times = []
    burst_times = []
    priorities = []
    remaining_times = []
    completion_times = [0] * n
    waiting_times = [0] * n
    turnaround_times = [0] * n
    gant_chart_list = []
    process_time = []
    color = 90

    # Input arrival, burst times, and priorities
    for i in range(n):
        at = int(input(f"Arrival time of P{i + 1}: "))
        bt = int(input(f"Burst time of P{i + 1}: "))
        pr = int(input(f"Priority of P{i + 1} (lower number = higher priority): "))
        arrival_times.append(at)
        burst_times.append(bt)
        priorities.append(pr)
        remaining_times.append(bt)

    current_time = 0
    completed = 0
    queue = deque()  # Queue to store the indices of processes

    while completed < n:
        # Add newly arrived processes to the queue (if not already in it)
        for i in range(n):
            if arrival_times[i] <= current_time and i not in queue and remaining_times[i] > 0:
                queue.append(i)

        # Sort the queue based on priority first, then remaining time, and arrival time
        queue = deque(sorted(queue, key=lambda x: (priorities[x], arrival_times[x], remaining_times[x])))

        if not queue:
            # If no processes are ready, move the time forward
            current_time += 1
            continue

        # Get the process with the highest priority (lowest priority number)
        current_process = queue.popleft()
        gant_chart_list.append(arrival_times.index(arrival_times[current_process]) + 1)

        # Execute the process for 1 time unit
        remaining_times[current_process] -= 1
        current_time += 1
        process_time.append(current_time)

        # If the process finishes, calculate completion time
        if remaining_times[current_process] == 0:
            completed += 1
            completion_times[current_process] = current_time
        else:
            # Add the current process back to the queue for further execution
            queue.append(current_process)

    # Calculate turnaround and waiting times
    for i in range(n):
        turnaround_times[i] = completion_times[i] - arrival_times[i]
        waiting_times[i] = turnaround_times[i] - burst_times[i]

    # Print results
    print(f"\n{'Process':<9}{'A.T':<10}{'B.T':<10}{'C.T':<10}{'TAT':<10}{'W.T':<10}{'PE,':<10}")
    for i in range(n):
        print(f"P{i + 1:<8}{arrival_times[i]:<10}{burst_times[i]:<10}{completion_times[i]:<10}{turnaround_times[i]:<10}{waiting_times[i]:<10}{priorities[i]:<10}")

    # Calculate and print average turnaround and waiting times
    avg_tat = sum(turnaround_times) / n
    avg_wt = sum(waiting_times) / n
    print(f"\nAverage Turnaround Time: {avg_tat:.2f}")
    print(f"Average Waiting Time: {avg_wt:.2f}")

    for i in range(len(gant_chart_list)):
        print(f"P{gant_chart_list[i]}", end=" " * 2, flush=True)
        time.sleep(0.25)
    print()
    for i in range(len(gant_chart_list)):
        print("|", end="")
        for i in range(1):
            print(" ", f"\033[{color}m*\033[0m", end="", flush=True)
            time.sleep(0.25)
        color += 1
        if color == 97:
            color = 30
    print("|")

    print(min(arrival_times), end=" ", flush=True)
    for pt in process_time:
        if pt < 10:
            time.sleep(0.5)
            print(" " * 2, pt, end="", flush=True)
        else:
            time.sleep(0.5)
            print(" " * 1, pt, end="", flush=True)
    print()
#=======================================================================================================================
print('''**********Scheduling Algorightms**********
1- FCFS
2- SJF
3- Priorty Base
4- Round Robin 
5- SJF (Premtive)
6- Priorty Base (Premtive)
''')
choice = int(input("enter the choice: "))
if choice == 1:
        fcfs()
elif choice == 2:
        sjf()
elif choice == 3:
        pb()
elif choice == 4:
        rr()
elif choice == 5:
    sjf_preemptive()
elif choice == 6:
    pb_preemptive()
elif choice == 7:
        exit(0)
else:
    print("invalid choice")


