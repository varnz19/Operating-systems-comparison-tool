# Operating System Algorithm Comparison Tool

## Project Overview
This project is an Operating System Algorithm Comparison Tool that implements and analyzes multiple operating system algorithms within a unified framework. The system allows users to input the same data and compare how different algorithms perform based on standard metrics such as waiting time, turnaround time, page faults, and seek time.

The goal of this project is to provide both practical implementation and analytical understanding of core operating system concepts.

---

##  Features
- Compare multiple OS algorithms using common input
- Interactive web interface using Streamlit
- Graphical visualization of results
- Easy-to-use and demo-friendly design

---

## ⚙️ Algorithms Implemented

### 🔹 CPU Scheduling
- First Come First Serve (FCFS)
- Shortest Job First (SJF)
- Round Robin (RR)
- Priority Scheduling

### 🔹 Page Replacement
- FIFO (First In First Out)
- LRU (Least Recently Used)

### 🔹 Disk Scheduling
- FCFS
- SSTF (Shortest Seek Time First)
- SCAN (Elevator Algorithm)

### 🔹 Memory Allocation
- First Fit
- Best Fit

---

## 🛠️ Technologies Used
- Python
- Streamlit (for UI)
- Matplotlib (for graphs)

---

## ▶️ How to Run the Project

### 1. Navigate to the project folder
```bash
cd os-algo-tool
```
###2. Install required libraries
```bash
pip3 install streamlit matplotlib
```
###3. Run the application
```bash
python3 -m streamlit run app.py
```
###4. Open in browser
(If it does not open automatically, go to:)
```bash 
http://localhost:8501
```
