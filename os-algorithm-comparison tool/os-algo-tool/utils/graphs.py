import matplotlib.pyplot as plt


def plot_bar(title, labels, values, ylabel):
    fig, ax = plt.subplots()
    ax.bar(labels, values)
    ax.set_title(title)
    ax.set_xlabel("Algorithms")
    ax.set_ylabel(ylabel)
    return fig


def plot_gantt(gantt):
    fig, ax = plt.subplots()

    for process, start, end in gantt:
        ax.barh(process, end - start, left=start)
        ax.text(start + (end - start)/2, process, process,
                ha='center', va='center', color='white')

    ax.set_xlabel("Time")
    ax.set_title("Gantt Chart")

    return fig