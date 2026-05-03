def sstf(requests, head):
    requests = requests.copy()
    seek_time = 0
    current = head
    order = [head]
    
    while requests:
        closest = min(requests, key=lambda x: abs(x - current))
        seek_time += abs(closest - current)
        current = closest
        order.append(current)
        requests.remove(closest)
    
    return seek_time, order