#!../analysis/bin/python3

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

sns.set_theme(style="darkgrid")

def direct_vs_htex():
    # workload fib(25)
    f, ax = plt.subplots(nrows=1, ncols=1, figsize=(6.4,6.4))
    
    direct = [1362.217867,	1336.893224,	1325.833413,	1320.774505,	1303.661746,	1323.572751,	1321.670926,	1234.510262]
    htex = [94.78235409,	187.5222059,	361.6370001,	682.3828663,	1086.529425,	1314.838884,	1394.915254,	1383.433669]
    nworkers = [1, 2, 4, 8, 16, 32, 64, 128]
    
    df = pd.DataFrame({"Throughput(Direct)": direct, "Throughput(HTEX)": htex, "Number of Workers": nworkers})
    
    sns.lineplot(df, x="Number of Workers", y="Throughput(Direct)", marker="o", label="Direct to Worker", ax=ax)
    sns.lineplot(df, x="Number of Workers", y="Throughput(HTEX)", marker="o", label="HTEX", ax=ax)
    ax.set_ylabel("Throughput(task/second)")
    f.suptitle("Direct to Worker vs HTEX")
    
    f.savefig("direct_vs_htex.png")

def tagging():
    # workerload fib(25) 144 workers 1 manager htex
    f, ax = plt.subplots(nrows=1, ncols=1, figsize=(12.8,6.4))
    
    time = [0.0004975730979042035, 0.00017967021019606584, 0.003298958443489562, 0.00046311185306922777, 0.00010463514431810356, 0.0008826296644305596, 0.0009051202430129334]
    time = [t * 1000000 for t in time]
    component = ["executor", "exc->int", "interchange", "int->man", "manager", "man->wor", "worker"]
    
    df = pd.DataFrame({"Time(microseconds)": time, "Component": component})
    
    sns.barplot(data=df, x="Component", y="Time(microseconds)", ax=ax)
    ax.set_title("Time spent in each component")
    
    f.savefig("tagging.png")

def interchange_tagging():
    # workload fib(25) 144 workers 1 manager htex
    f, ax = plt.subplots(nrows=1, ncols=1, figsize=(6.4,6.4))
    
    time = [-4.967253071631067e-06, 0.003260314684595703, 3.3676505822228186e-05]
    time = [t * 1000000 for t in time]
    component = ["task pull", "task pull -> main", "main"]
    
    df = pd.DataFrame({"Time(microseconds)": time, "Component": component})
    sns.barplot(data=df, x="Component", y="Time(microseconds)", ax=ax)
    ax.set_title("Time spent in each component")
    
    f.savefig("interchange_tagging.png")

def print_direct_to_worker_txt()
    for i in range(5, 30, 5):
        runtime = []
        for j in [1, 2, 4, 8, 16, 32, 64, 128]:
            f = open(f"xqfib{str(i).zfill(2)}-{str(j).zfill(3)}.txt", "r")
            data = [float(line.split(' ')[-1]) for line in f]
            r = sum(data)/10
            runtime.append(r)
        print(f"fib({i}): {runtime}")
