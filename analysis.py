#!../analysis/bin/python3
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

from matplotlib.scale import LogScale
sns.set_theme(style="whitegrid")
figsize=(12.8,6.4)

def pandanite():
    f, ax = plt.subplots(nrows=1, ncols=1, figsize=figsize)

    bps = [0.894, 1.09, 1.2, 1.2]
    nodes = [5, 10, 20, 40]
    df = pd.DataFrame({"Nodes": nodes, "Throughput(Blocks/Second)": bps})
    sns.barplot(df, x="Nodes", y="Throughput(Blocks/Second)", ax=ax, width=.4)
    f.savefig("pandanite.png")

def pbft():
    f, ax = plt.subplots(nrows=1, ncols=1, figsize=figsize)
    latency = [123, 175, 241]
    nodes = [2, 4, 8]
    df = pd.DataFrame({"nodes": nodes, "latency(ms)": latency})
    sns.barplot(df, x="nodes", y="latency(ms)", ax=ax, width=.4)
    f.savefig("pbft.png")

def mfmc():
    f, ax = plt.subplots(nrows=1, ncols=1, figsize=figsize)
    students = [100, 200, 400, 800, 1600]
    runtime = [.432, 1.642, 5.563, 20.634, 78.146]
    df = pd.DataFrame({"Number of Students": students, "Runtime(s)": runtime})
    sns.barplot(df, x="Number of Students", y="Runtime(s)", ax=ax, width=.4)
    ax.set_title("Runtime of Optimal Assignment")
    ax.set_yscale(LogScale(1, base=10))
    f.savefig("logmfmc.png")


def nologgingthroughput():
    f, ax = plt.subplots(nrows=1, ncols=1, figsize=figsize)
    runtime = [2082.822674036026, 1038.7380170822144, 519.6603798866272, 260.74488377571106, 131.58347415924072, 66.48571419715881, 36.817787170410156, 26.448672771453857]
    throughput = [100000 / t for t in runtime]
    nworkers=[1, 2, 4, 8, 16, 32, 64, 128]
    df = pd.DataFrame({"Throughput(tasks/second)": throughput, "Number of Workers": nworkers})
    sns.lineplot(df, x="Number of Workers", y="Throughput(tasks/second)", marker="o")
    ax.set_xscale(LogScale(1, base=2))
    ax.set_yscale(LogScale(2, base=2))
    f.suptitle("Parsl no-op throughput with logging off")
    f.savefig("parsl_throughput_nologging.png")

def nologging_direct_vs_htex():
    f, ax = plt.subplots(nrows=1, ncols=1, figsize=figsize)
    druntime = [1.8335903406143188, 1.7716833353042603, 1.8989869435628255, 1.876910098393758, 1.9401285171508789, 1.967039171854655, 1.9942612012227376, 2.0535037597020467]
    hruntime = [208.69511485099792, 104.06894159317017, 52.18400287628174, 26.351411819458008, 13.301186561584473, 6.86055326461792, 3.694573163986206, 2.37636137008667]
    nworkers=[1, 2, 4, 8, 16, 32, 64, 128]
    dthroughput = [10000 / t for t in druntime]
    hthroughput = [10000 / t for t in hruntime]
    df = pd.DataFrame({"Throughput": dthroughput + hthroughput, "Workers": nworkers + nworkers, "Executor": 8 * ["DIREX"] + 8 *["HTEX"]})
    sns.lineplot(data=df, x="Workers", y="Throughput", hue="Executor", marker="o", ax=ax)
    ax.set_xscale(LogScale(1, base=2))
    ax.set_yscale(LogScale(2, base=2))
    ax.set_xticks(nworkers)
    ax.set_yticks([64, 128, 256, 512, 1024, 2048, 4096, 8192])
    ax.get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
    ax.get_yaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())

    f.suptitle("Direct to Worker vs HTEX")
    f.savefig("nolog_direct_vs_htex.png")

def nologging_cdfkthroughput():
    f, ax = plt.subplots(nrows=1, ncols=1, figsize=figsize)
    cruntime = [33.46020517349243,18.812900447845458,13.267690026760102,11.541702806949615,11.690159857273102,11.076891493797302,11.291940593719483,11.48463146686554]
    hruntime = [2082.822674036026, 1038.7380170822144, 519.6603798866272, 260.74488377571106, 131.58347415924072, 66.48571419715881, 36.817787170410156, 26.448672771453857]
    nworkers = [1,2,4,8,16,32,64,128]
    cthroughput = [100000 / n for n in cruntime]
    hthroughput = [100000 / n for n in hruntime]
    df = pd.DataFrame({"Throughput(Python DFK)": hthroughput, "Throughput(C DFK)": cthroughput, "Number of Workers": nworkers})
    sns.lineplot(df, x="Number of Workers", y="Throughput(Python DFK)", marker="o", label="Python DFK", ax=ax)
    sns.lineplot(df, x="Number of Workers", y="Throughput(C DFK)", marker="o", label="C DFK", ax=ax)
    ax.set_xscale(LogScale(1, base=2))
    ax.set_yscale(LogScale(2, base=2))
    ax.set_xticks(nworkers)
    ax.set_yticks([64, 128, 256, 512, 1024, 2048, 4096, 8192])
    ax.get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
    ax.get_yaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
    f.suptitle("Python DFK vs C DFK")
    f.savefig("nolog_pdfk_vs_cdfk.png")

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
    f, ax = plt.subplots(nrows=1, ncols=1, figsize=figsize)
    time = [8.477394580841065e-05, 3.8863635063171386e-05, 0.001304353952407837, 0.03159386081695557, 0.0002338757038116455, 5.925240516662598e-05, 0.00029827773571014407, 0.0005129362344741821]
    time = [t * 1000000 for t in time]
    component = ["dfk", "executor", "exc->int", "interchange", "int->man", "manager", "man->wor", "worker"]
    
    df = pd.DataFrame({"Time(microseconds)": time, "Component": component})
    
    sns.barplot(data=df, x="Component", y="Time(microseconds)", ax=ax)
    ax.set_title("Time spent in each component")
    ax.set_yscale("log")
    
    f.savefig("tagging.png")

def interchange_tagging():
    # workload fib(25) 144 workers 1 manager htex
    f, ax = plt.subplots(nrows=1, ncols=1, figsize=figsize)

    time = [-3.887295722961426e-06, 0.031579251980781556, 1.0721540451049805e-05]
    time = [t * 1000000 for t in time]
    component = ["task pull", "task pull -> main", "main"]
    
    df = pd.DataFrame({"Time(microseconds)": time, "Component": component})
    sns.barplot(data=df, x="Component", y="Time(microseconds)", ax=ax, width=.4)
    ax.set_title("Time spent within the Interchange")
    ax.set_yscale("log")
    f.savefig("interchange_tagging.png")

def print_direct_to_worker_txt():
    for i in range(5, 30, 5):
        runtime = []
        for j in [1, 2, 4, 8, 16, 32, 64, 128]:
            f = open(f"xqfib{str(i).zfill(2)}-{str(j).zfill(3)}.txt", "r")
            data = [float(line.split(' ')[-1]) for line in f]
            r = sum(data)/10
            runtime.append(r)
        print(f"fib({i}): {runtime}")

def cdfk_vs_pdfk_objcount():
    f, ax = plt.subplots(nrows=1, ncols=1, figsize=figsize)
    numtasks = [1, 10, 100, 1000, 10000, 100000]
    cdfk = [281.0, 1191.5, 3465.3, 26692.4, 287134.6, 2600550.7]
    pdfk = [503.0, 1241.0, 4386.1, 36811.9, 360629.2, 3600768.6]
    df = pd.DataFrame({"Number of Tasks": numtasks, "C DFK": cdfk, "Python DFK": pdfk})
    sns.lineplot(data=df, x="Number of Tasks", y="C DFK", marker="o", ax=ax)
    sns.lineplot(data=df, x="Number of Tasks", y="Python DFK", marker="o", ax=ax)

    ax.set_title("Memory footprint C DFK vs Python DFK")
    ax.set_ylabel("Number of Python Objects")
    ax.set_yscale("log")
    ax.set_xscale("log")
    f.savefig("objcount_cdfkvpdfk.png")

def gc_vs_nogc_throughput():
    f, ax = plt.subplots(nrows=1, ncols=1, figsize=figsize)
    numtasks = [1000, 10000, 100000] + [1000, 10000, 100000]
    gc = [1000 / 0.5928019762039185, 10000 / 2.4107550144195558, 100000 / 24.805594515800475]
    nogc = [1000 / 0.5894630193710327, 10000 / 2.0575541734695433, 100000 / 20.18178346157074]
    havegc = 3 * ["yes"] + 3 * ["no"]
    df = pd.DataFrame({"Number of Tasks": numtasks, "Throughput": gc + nogc, "GC Enabled": havegc})
    sns.barplot(df, x="Number of Tasks", y="Throughput", hue="GC Enabled", width=.4,ax=ax)
    f.savefig("gcvnogc_throughput.png")

def singleq_vs_multiq():
    f, ax = plt.subplots(nrows=1, ncols=1, figsize=figsize)
    nworkers = [1, 2, 4, 8, 16, 32, 64, 128]
    mqruntime = [2.484412097930908, 2.337325692176819, 2.476684904098511, 2.6450060844421386, 2.6758565664291383, 2.657198667526245, 2.6968280553817747, 2.6850218296051027]
    sqruntime = [2.1922109127044678, 1.9805155754089356, 1.846487283706665, 1.8778392553329468, 1.9182080030441284, 1.9445616722106933, 1.9980420112609862, 2.0566566228866576]
    mqthroughput = [10000 / i for i in mqruntime]
    sqthroughput = [10000 / i for i in sqruntime]
    queuetype = 8 * ["single"] + 8 * ["multi"]
    df = pd.DataFrame({"Number of Workers": nworkers + nworkers, "Throughput": sqthroughput + mqthroughput, "Queue Type": queuetype})
    sns.lineplot(df, x="Number of Workers", y="Throughput", hue="Queue Type", marker="o", ax=ax)
    ax.set_xscale(LogScale(1, base=2))
    ax.set_xticks(nworkers)
    ax.get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
    f.savefig("sqvmq_throughput.png")


def cdfkdirex_vs_all():
    f, ax = plt.subplots(nrows=1, ncols=1, figsize=figsize)

    cdfk_direx_runtime = [1.0357314348220825, 0.9358649969100952, 0.8849812507629394, 0.9049288272857666, 1.0458908081054688, 1.0767723321914673, 1.1763696432113648, 1.2288320064544678]
    cdfk_runtime = [1.113578200340271, 1.1074100494384767, 1.103058385848999, 1.1020861387252807, 1.6579477310180664, 1.138422155380249, 1.140928530693054, 1.210385251045227]
    direx_runtime = [1.8335903406143188, 1.7716833353042603, 1.8989869435628255, 1.876910098393758, 1.9401285171508789, 1.967039171854655, 1.9942612012227376, 2.0535037597020467]
    htex_runtime = [208.69511485099792, 104.06894159317017, 52.18400287628174, 26.351411819458008, 13.301186561584473, 6.86055326461792, 3.694573163986206, 2.37636137008667]
    nworkers=[1, 2, 4, 8, 16, 32, 64, 128]
    cdfk_direx_throughput = [10000 / t for t in cdfk_direx_runtime]
    cdfk_throughput = [10000 / t for t in cdfk_runtime]
    direx_throughput = [10000 / t for t in direx_runtime]
    htex_throughput = [10000 / t for t in htex_runtime]

    df = pd.DataFrame({"Throughput": cdfk_direx_throughput + cdfk_throughput + direx_throughput + htex_throughput, "Workers": 4 * nworkers, "Parsl Type": 8 * ["CDFK DIREX"] + 8 *["CDFK"] + 8 * ["DIREX"] + 8 *["Standard"]})
    sns.lineplot(data=df, x="Workers", y="Throughput", hue="Parsl Type", marker="o", ax=ax)
    ax.set_xscale(LogScale(1, base=2))
    ax.set_yscale(LogScale(2, base=2))
    ax.set_xticks(nworkers)
    ax.set_yticks([64, 128, 256, 512, 1024, 2048, 4096, 8192])
    ax.get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
    ax.get_yaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())

    f.suptitle("Throughput of CDFK DIREX compared")
    f.savefig("cdfkdirex_vs_all.png")


#f = open("dfkbench.txt", "r")
#batch = [i+1 for i in range(500)]
#throughput = [float(line) for line in f]
#df = pd.DataFrame({"Batch": batch, "Throughput(task/second)": throughput})
#f1, ax1 = plt.subplots(nrows=1, ncols=1, figsize=(6.4,6.4))
#f2, ax2 = plt.subplots(nrows=1, ncols=1, figsize=(6.4,6.4))
#
#ax2.set_ylabel("Batch")
#sns.lineplot(data=df, x="Batch", y="Throughput(task/second)", ax=ax1)
#sns.histplot(data=df, x="Throughput(task/second)", kde=True, ax=ax2)
#f1.suptitle("DFK Throughput no-op 500k")
#f2.suptitle("DFK Throughput no-op 500k")
#f1.savefig("dfkbench_line.png")
#f2.savefig("dfkbench_hist.png")
#tagging()
#interchange_tagging()
#nologgingthroughput()
#nologging_direct_vs_htex()
#nologging_cdfkthroughput()
#cdfk_vs_pdfk_objcount()
#gc_vs_nogc_throughput()
#singleq_vs_multiq()
cdfkdirex_vs_all()
#pandanite()
#pbft()
#mfmc()
