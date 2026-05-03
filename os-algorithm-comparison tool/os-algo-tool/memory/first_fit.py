def first_fit(blocks, processes):
    allocation = [-1] * len(processes)
    blocks_copy = blocks.copy()
    
    for i in range(len(processes)):
        for j in range(len(blocks_copy)):
            if blocks_copy[j] >= processes[i]:
                allocation[i] = j
                blocks_copy[j] -= processes[i]
                break
    
    return allocation