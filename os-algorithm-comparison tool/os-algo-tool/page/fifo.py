def fifo(pages, capacity):
    frame = []
    faults = 0
    
    for page in pages:
        if page not in frame:
            faults += 1
            
            if len(frame) < capacity:
                frame.append(page)
            else:
                frame.pop(0)
                frame.append(page)
    
    return faults