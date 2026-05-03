from cpu.fcfs import fcfs
from cpu.sjf import sjf
from cpu.rr import round_robin
from cpu.priority import priority_scheduling

from page.fifo import fifo
from page.lru import lru

from disk.fcfs_disk import fcfs_disk
from disk.sstf import sstf
from disk.scan import scan

from memory.first_fit import first_fit
from memory.best_fit import best_fit

from utils.graphs import plot_bar, plot_gantt


def cpu_module():
    print("\n--- CPU Scheduling ---")

    processes = []
    processes_pr = []

    n = int(input("Enter number of processes: "))

    for i in range(n):
        at = int(input(f"P{i+1} Arrival Time: "))
        bt = int(input(f"P{i+1} Burst Time: "))
        pr = int(input(f"P{i+1} Priority: "))

        processes.append((i+1, at, bt))
        processes_pr.append((i+1, at, bt, pr))

    q = int(input("Enter Time Quantum: "))

    fcfs_wt, fcfs_tat, gantt = fcfs(processes)
    sjf_wt, sjf_tat = sjf(processes)
    rr_wt, rr_tat = round_robin(processes, q)
    pr_wt, pr_tat = priority_scheduling(processes_pr)

    print("\nResults:")
    print(f"FCFS → WT={fcfs_wt:.2f}, TAT={fcfs_tat:.2f}")
    print(f"SJF  → WT={sjf_wt:.2f}, TAT={sjf_tat:.2f}")
    print(f"RR   → WT={rr_wt:.2f}, TAT={rr_tat:.2f}")
    print(f"Priority → WT={pr_wt:.2f}, TAT={pr_tat:.2f}")

    plot_bar("CPU Waiting Time",
             ['FCFS','SJF','RR','Priority'],
             [fcfs_wt, sjf_wt, rr_wt, pr_wt],
             "Time")

    plot_gantt(gantt)


def page_module():
    print("\n--- Page Replacement ---")

    pages = list(map(int, input("Enter reference string: ").split()))
    frames = int(input("Enter number of frames: "))

    f = fifo(pages, frames)
    l = lru(pages, frames)

    print("\nResults:")
    print(f"FIFO → {f} faults")
    print(f"LRU  → {l} faults")

    plot_bar("Page Faults", ['FIFO','LRU'], [f, l], "Faults")


def disk_module():
    print("\n--- Disk Scheduling ---")

    req = list(map(int, input("Enter requests: ").split()))
    head = int(input("Enter head position: "))
    size = int(input("Enter disk size: "))

    f, _ = fcfs_disk(req, head)
    s, _ = sstf(req, head)
    sc, _ = scan(req, head, size)

    print("\nResults:")
    print(f"FCFS → {f}")
    print(f"SSTF → {s}")
    print(f"SCAN → {sc}")

    plot_bar("Disk Scheduling", ['FCFS','SSTF','SCAN'], [f, s, sc], "Seek Time")


def memory_module():
    print("\n--- Memory Allocation ---")

    blocks = list(map(int, input("Enter blocks: ").split()))
    procs = list(map(int, input("Enter processes: ").split()))

    ff = first_fit(blocks, procs)
    bf = best_fit(blocks, procs)

    print("\nResults:")
    print("First Fit:", ff)
    print("Best Fit:", bf)

    ff_fail = ff.count(-1)
    bf_fail = bf.count(-1)

    plot_bar("Memory Allocation", ['First Fit','Best Fit'], [ff_fail, bf_fail], "Failures")


# -------- MAIN MENU --------

while True:
    print("\n====== OS Algorithm Tool ======")
    print("1. CPU Scheduling")
    print("2. Page Replacement")
    print("3. Disk Scheduling")
    print("4. Memory Allocation")
    print("5. Exit")

    ch = int(input("Enter choice: "))

    if ch == 1:
        cpu_module()
    elif ch == 2:
        page_module()
    elif ch == 3:
        disk_module()
    elif ch == 4:
        memory_module()
    elif ch == 5:
        print("Exiting...")
        break
    else:
        print("Invalid choice!")