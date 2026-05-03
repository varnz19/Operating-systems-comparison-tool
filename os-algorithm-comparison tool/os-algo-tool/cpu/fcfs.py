def fcfs(processes):
    n = len(processes)
    processes_sorted = sorted(processes, key=lambda x: x[1])
    
    waiting_time = [0] * n
    turnaround_time = [0] * n
    gantt = []
    
    current_time = 0
    
    for i in range(n):
        pid, at, bt = processes_sorted[i]
        
        if current_time < at:
            current_time = at
        
        start = current_time
        end = current_time + bt
        
        gantt.append((f"P{pid}", start, end))
        
        waiting_time[i] = start - at
        turnaround_time[i] = end - at
        
        current_time = end
    
    avg_wt = sum(waiting_time)/n
    avg_tat = sum(turnaround_time)/n
    
    return avg_wt, avg_tat, gantt