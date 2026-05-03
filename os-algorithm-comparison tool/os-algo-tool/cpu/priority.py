def priority_scheduling(processes):
    # processes = (pid, arrival, burst, priority)
    
    processes_sorted = sorted(processes, key=lambda x: x[3])  # lower = higher priority
    
    n = len(processes_sorted)
    waiting_time = [0] * n
    turnaround_time = [0] * n
    
    turnaround_time[0] = processes_sorted[0][2]
    
    for i in range(1, n):
        waiting_time[i] = waiting_time[i-1] + processes_sorted[i-1][2]
        turnaround_time[i] = waiting_time[i] + processes_sorted[i][2]
    
    avg_wt = sum(waiting_time)/n
    avg_tat = sum(turnaround_time)/n
    
    return avg_wt, avg_tat