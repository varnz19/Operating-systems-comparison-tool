def best_fit(blocks, processes):
    allocation = [-1] * len(processes)
    blocks_copy = blocks.copy()
    
    for i in range(len(processes)):
        best_idx = -1
        
        for j in range(len(blocks_copy)):
            if blocks_copy[j] >= processes[i]:
                if best_idx == -1 or blocks_copy[j] < blocks_copy[best_idx]:
                    best_idx = j
        
        if best_idx != -1:
            allocation[i] = best_idx
            blocks_copy[best_idx] -= processes[i]
    
    return allocation