def round_robin(processes, quantum):
    n = len(processes)
    
    remaining_bt = [p[2] for p in processes]
    waiting_time = [0] * n
    turnaround_time = [0] * n
    
    time = 0
    
    while True:
        done = True
        
        for i in range(n):
            if remaining_bt[i] > 0:
                done = False
                
                if remaining_bt[i] > quantum:
                    time += quantum
                    remaining_bt[i] -= quantum
                else:
                    time += remaining_bt[i]
                    waiting_time[i] = time - processes[i][2]
                    remaining_bt[i] = 0
        
        if done:
            break
    
    for i in range(n):
        turnaround_time[i] = processes[i][2] + waiting_time[i]
    
    return sum(waiting_time)/n, sum(turnaround_time)/n