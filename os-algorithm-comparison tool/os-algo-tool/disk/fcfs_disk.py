def fcfs_disk(requests, head):
    seek_time = 0
    current = head
    order = [head]
    
    for req in requests:
        seek_time += abs(req - current)
        current = req
        order.append(current)
    
    return seek_time, order