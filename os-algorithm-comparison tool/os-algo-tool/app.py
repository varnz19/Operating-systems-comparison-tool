import streamlit as st

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


st.title("OS Algorithm Comparison Tool")

module = st.sidebar.selectbox(
    "Select Module",
    ["CPU Scheduling", "Page Replacement", "Disk Scheduling", "Memory Allocation"]
)

# ================= CPU =================
if module == "CPU Scheduling":
    st.header("CPU Scheduling")

    processes = []
    processes_pr = []

    for i in range(4):
        at = st.number_input(f"P{i+1} Arrival Time", key=f"at{i}")
        bt = st.number_input(f"P{i+1} Burst Time", key=f"bt{i}")
        pr = st.number_input(f"P{i+1} Priority", key=f"pr{i}")

        processes.append((i+1, at, bt))
        processes_pr.append((i+1, at, bt, pr))

    q = st.number_input("Time Quantum")

    if st.button("Run CPU"):
        fcfs_wt, fcfs_tat, gantt = fcfs(processes)
        sjf_wt, sjf_tat = sjf(processes)
        rr_wt, rr_tat = round_robin(processes, q)
        pr_wt, pr_tat = priority_scheduling(processes_pr)

        st.subheader("Results")
        st.write(f"FCFS → WT: {fcfs_wt:.2f}, TAT: {fcfs_tat:.2f}")
        st.write(f"SJF → WT: {sjf_wt:.2f}, TAT: {sjf_tat:.2f}")
        st.write(f"RR → WT: {rr_wt:.2f}, TAT: {rr_tat:.2f}")
        st.write(f"Priority → WT: {pr_wt:.2f}, TAT: {pr_tat:.2f}")

        fig1 = plot_bar(
            "CPU Waiting Time",
            ['FCFS','SJF','RR','Priority'],
            [fcfs_wt, sjf_wt, rr_wt, pr_wt],
            "Time"
        )
        st.pyplot(fig1)

        fig2 = plot_gantt(gantt)
        st.pyplot(fig2)


# ================= PAGE =================
elif module == "Page Replacement":
    st.header("Page Replacement")

    pages = st.text_input("Reference String (space separated)")
    frames = st.number_input("Number of Frames")

    if st.button("Run Page"):
        pages = list(map(int, pages.split()))
        f = fifo(pages, frames)
        l = lru(pages, frames)

        st.subheader("Results")
        st.write(f"FIFO → {f} faults")
        st.write(f"LRU → {l} faults")

        fig = plot_bar("Page Faults", ['FIFO','LRU'], [f, l], "Faults")
        st.pyplot(fig)


# ================= DISK =================
elif module == "Disk Scheduling":
    st.header("Disk Scheduling")

    req = st.text_input("Requests (space separated)")
    head = st.number_input("Head Position")
    size = st.number_input("Disk Size")

    if st.button("Run Disk"):
        req = list(map(int, req.split()))
        f, _ = fcfs_disk(req, head)
        s, _ = sstf(req, head)
        sc, _ = scan(req, head, size)

        st.subheader("Results")
        st.write(f"FCFS → {f}")
        st.write(f"SSTF → {s}")
        st.write(f"SCAN → {sc}")

        fig = plot_bar(
            "Disk Scheduling",
            ['FCFS','SSTF','SCAN'],
            [f, s, sc],
            "Seek Time"
        )
        st.pyplot(fig)


# ================= MEMORY =================
elif module == "Memory Allocation":
    st.header("Memory Allocation")

    blocks = st.text_input("Blocks (space separated)")
    procs = st.text_input("Processes (space separated)")

    if st.button("Run Memory"):
        blocks = list(map(int, blocks.split()))
        procs = list(map(int, procs.split()))

        ff = first_fit(blocks, procs)
        bf = best_fit(blocks, procs)

        st.subheader("Results")
        st.write("First Fit:", ff)
        st.write("Best Fit:", bf)

        ff_fail = ff.count(-1)
        bf_fail = bf.count(-1)

        fig = plot_bar(
            "Memory Allocation",
            ['First Fit','Best Fit'],
            [ff_fail, bf_fail],
            "Failures"
        )
        st.pyplot(fig)