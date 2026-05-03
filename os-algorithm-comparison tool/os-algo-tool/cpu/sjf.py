def sjf(processes):
    n = len(processes)
    processes_sorted = sorted(processes, key=lambda x: x[2])
    
    waiting_time = [0] * n
    turnaround_time = [0] * n
    
    turnaround_time[0] = processes_sorted[0][2]
    
    for i in range(1, n):
        waiting_time[i] = waiting_time[i-1] + processes_sorted[i-1][2]
        turnaround_time[i] = waiting_time[i] + processes_sorted[i][2]
    
    return sum(waiting_time)/n, sum(turnaround_time)/n