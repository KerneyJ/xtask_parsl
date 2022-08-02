# script to do analysis
# Experiments 151-170 are no ops 500 - 10000
# Experiments 171-190 are fib 1-20
import os
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from parselog import make_wkrtbl, make_statstbl, calc_thrghpt, merge_tsklst, parse_dir, parse_task, parse_stats


def analyze_laptop_benchmark():
    # Parse the directory
    dirtbl = parse_dir("benchmarks/laptop_benchmark", ["htex"])
    throughput = []
    experiments = []
    for log, wkrdirs in dirtbl.items():
        for wkrdir in wkrdirs: # in the directory benchmark, a dictionary that has only one wkrdir
            wkrtbl = make_wkrtbl(wkrdir)
            total_tsklst = []
            for wkr, path in wkrtbl.items():
                with open(path) as wkr_file:
                    worker_tsklst = parse_task(wkr_file)
                    if not worker_tsklst:
                        continue
                    total_tsklst.append(worker_tsklst)

            total_tsklst = merge_tsklst(total_tsklst) # turn total_tsklst from a list of task list to a list of all the task done
            throughput.append(calc_thrghpt(total_tsklst))
            experiments.append(int(log[:3]))

    # create and organize the dataframe
    df = pd.DataFrame({"Throughput": throughput}, index=experiments)
    df = df.sort_index()
    df["type"] = ["no_op" for _ in range(20)] + ["fib" for _ in range(20)]
    df["n"] = [i for i in range(500, 10001, 500)] + [i for i in range(1, 21, 1)]
    noop_df = df[:20]
    fib_df = df[20:]

    # plot the data
    f, (fib_ax, noop_ax) = plt.subplots(nrows=1, ncols=2, figsize=(12.8,6.4))

    sns.scatterplot(data=fib_df, x="n", y="Throughput", ax=fib_ax)
    sns.scatterplot(data=noop_df, x="n", y="Throughput", ax=noop_ax)
    plt.savefig("analysis/laptop_benchmark.png")

def analyze_experiments(exp, cnfgs):
    dirtbl = parse_dir(f"benchmarks/{exp}", cnfgs)
    throughput = []
    experiments = []
    statsdfs = {}

    # parse the files and make dataframes
    for log, wkrdirs in dirtbl.items():
        total_tsklst = []
        for wkrdir in wkrdirs: # in the directory benchmark, a dictionary that has only one wkrdir 
            *_, block_id, node_id = wkrdir.split("/")
            wkrtbl = make_wkrtbl(wkrdir)
            statstbl = make_statstbl(wkrdir)
            for stats_name, path in statstbl.items():
                try:
                    data = parse_stats(path)
                    columns = data[0]
                    data = data[1:]
                    data = [[row[0]] + [float(row[i]) for i in range(1, 4)] + [row[4], row[5]] for row in data]
                    df = pd.DataFrame(data=data, columns=columns)
                    statsdfs.update({f"{log}_{block_id}_{node_id}_{stats_name}": (df, log, block_id, node_id, stats_name)})
                except Exception as e:
                    print(f"Ran into execption {type(e)}: {e} parsing {stats_name}_{log}")
            for wkr, path in wkrtbl.items():
                with open(path) as wkr_file:
                    worker_tsklst = parse_task(wkr_file)
                    if not worker_tsklst:
                        continue
                    total_tsklst.append(worker_tsklst)

        total_tsklst = merge_tsklst(total_tsklst) # turn total_tsklst from a list of task list to a list of all the task done
        throughput.append(calc_thrghpt(total_tsklst))
        experiments.append(int(log[:3]))
    # Graph the data

    # The code below creates graphs using the profiling data
    for _, (df, log, block_id, node_id, name) in statsdfs.items():
        tottime = sum(df.loc[:, "tottime"])
        df["tottime"] = df["tottime"].apply(lambda x: x / tottime)
        df.sort_values(by="tottime")
        df = df[0:15]
        f, ax = plt.subplots(nrows=1, ncols=1, figsize=(12.8,6.4))
        sns.barplot(data=df, x="filename:lineno(function)", y="tottime", ax=ax)
        plt.xticks(rotation=-10, fontsize="xx-small", fontstretch=100)
        if not os.path.isdir(f"analysis/{exp}/{log}/{block_id}"):
            os.makedirs(f"analysis/{exp}/{log}/{block_id}")
        plt.savefig(f"analysis/{exp}/{log}/{block_id}/{node_id}_{name}.png")
        plt.close(f)
    # The code below creates graphs using the throughput data
    df = pd.DataFrame({"Throughput": throughput}, index=experiments)
    df = df.sort_index()
    df["type"] = ["no_op" for _ in range(5)] + ["fib" for _ in range(5)]
    df["n"] = [1000, 5000, 10000, 50000, 100000] + [5, 10, 15, 20, 25]
    noop_df = df[:10]
    fib_df = df[10:]

    # plot the data
    f, (fib_ax, noop_ax) = plt.subplots(nrows=1, ncols=2, figsize=(12.8,6.4))

    sns.scatterplot(data=fib_df, x="n", y="Throughput", ax=fib_ax)
    sns.scatterplot(data=noop_df, x="n", y="Throughput", ax=noop_ax)
    plt.savefig(f"analysis/{exp}/{exp}.png")
    plt.close(f)

def analyze_profdir(cnfg_name):
    statstbl = [(f"prof/{cnfg_name}/", stats) for stats in os.listdir(f"prof/{cnfg_name}") if ".pstats" in stats]
    for directory, path in statstbl:
        data = parse_stats(directory+path, sortby="tottime")
        columns = data[0]
        data = data[1:]
        data = [[row[0]] + [float(row[i]) for i in range(1, 4)] + [row[4], row[5]] for row in data]
        df = pd.DataFrame(data=data, columns=columns)
        df = df[0:15]
        f, ax = plt.subplots(nrows=1, ncols=1, figsize=(12.8, 6.4))
        sns.barplot(data=df, x="filename:lineno(function)", y="tottime", ax=ax)
        plt.xticks(rotation=-10, fontsize="xx-small", fontstretch=100)
        name, _ = path.split(".")
        plt.savefig(f"{directory}{name}.png")
        plt.close(f)

if __name__ == "__main__":
    #analyze_laptop_benchmark()
    # analyze_experiments("experiment5", ["htex_1cpw_48w"])
    from multiprocessing import Process
    experiments = ["htex_exp1", "htex_exp2", "htex_exp3", "htex_exp4", "htex_exp5", "htex_exp6", "htex_exp7","htex_exp8"]
    for exp in experiments:
         analyze_profdir(exp)
    exp_cnfg = [
            ("experiment1", ["htex_1cpw_48w"]),
            ("experiment2", ["htex_1cpw_96w"]),
            ("experiment3", ["htex_1cpw_144w"]),
            ("experiment4", ["htex_1cpw_192w"]),
            #("experiment5", ["htex_1cpw_48w"]),
            #("experiment6", ["htex_1cpw_96w"]),
            #("experiment7", ["htex_1cpw_144w"]),
            #("experiment8", ["htex_1cpw_192w"]),
    ]
    print("done creating prof images")
    processes = []
    for exp, cnfg in exp_cnfg:
        p = Process(name=exp, target=analyze_experiments, args=(exp, cnfg,))
        p.start()
        processes.append(p)
    
    while processes:
        p = processes.pop(0)
        if not p.is_alive():
            p.join()
            print(f"analysis of {p.name} has terminated")
        else:
            processes.append(p)
