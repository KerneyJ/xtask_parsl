# script to do analysis
# Experiments 151-170 are no ops 500 - 10000
# Experiments 171-190 are fib 1-20
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

def analyze_experiments():
    dirtbl = parse_dir("benchmarks/bench-prof-test", ["htex_1cpw_8w"])
    throughput = []
    experiments = []
    statsdfs = {}
    for log, wkrdirs in dirtbl.items():
        for wkrdir in wkrdirs: # in the directory benchmark, a dictionary that has only one wkrdir 
            wkrtbl = make_wkrtbl(wkrdir)
            statstbl = make_statstbl(wkrdir)
            for stats_name, path in statstbl.items():
                try:
                    data = parse_stats(path)
                    columns = data[0]
                    data = data[1:]
                    data = [[row[0]] + [float(row[i]) for i in range(1, 4)] + [row[4], row[5]] for row in data]
                    df = pd.DataFrame(data=data, columns=columns)
                    statsdfs.update({f"{stats_name}_{log}": df})
                except Exception as e:
                    print(f"{stats_name}_{log}: {e}")
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

    example = statsdfs["worker_3_017_htex_1cpw_8w"] # worker 3, experiment 17, config htex 1 core per worker 8 workers
    tottime = sum(example.loc[:, "tottime"])
    example["tottime"] = example["tottime"].apply(lambda x: x / tottime)
    example = example[0:10]
    f, ax = plt.subplots(nrows=1, ncols=1, figsize=(12.8,6.4))
    ax.margins(x=1,y=1)
    sns.barplot(data=example, x="filename:lineno(function)", y="tottime", ax=ax)
    plt.xticks(rotation=-10, fontsize="xx-small", fontstretch=100)
    plt.savefig("analysis/profile_example.png")

if __name__ == "__main__":
    # analyze_laptop_benchmark()
    analyze_bench_prof_test()
