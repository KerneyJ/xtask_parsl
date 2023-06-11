#!../analysis/bin/python3
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

from matplotlib.scale import LogScale

# sns.set(font_scale=5)
sns.set_theme(style="whitegrid")
figsize=(12.8,6.4)

GRANULARITY_YLABEL = "Throughput(tasks/second)"

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

    cdfk_direx_runtime = [0.9177794694900513,0.7923081636428833,0.7211169958114624,0.7381311416625976,0.7386274337768555,0.7844016313552856,0.8391645669937133,0.8448013305664063]
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

def granularity_cdfkdirex():
    f, ax = plt.subplots(nrows=1, ncols=1, figsize=figsize)

    cdfkdirex_0us = [1.5317886590957641,1.1461533546447753,1.0257321119308471,1.0085374593734742,1.065446376800537,1.0874726533889771,1.1242356300354004,1.1761406898498534]
    #cdfkdirex_1us = [1.357242226600647,1.0301915645599364,1.0291496753692626,1.0768460035324097,1.0442428827285766,1.0092048645019531,1.093170166015625,1.1154373407363891]
    cdfkdirex_10us = [2.2140042781829834,1.3623889207839965,1.0318618059158324,1.0525174617767334,1.1366793155670165,1.1619214296340943,1.2294798612594604,1.2394426822662354]
    #cdfkdirex_100us = [1.7466087818145752,1.158806276321411,1.0471296072006226,1.0524781227111817,1.0551241874694823,0.9883117914199829,1.0413472652435303,1.128321933746338]
    cdfkdirex_1000us = [12.359384560585022,6.375921702384948,3.42776300907135,1.9504756450653076,1.9993041276931762,2.0269531488418577,2.0802396535873413,2.0948133945465086]
    cdfkdirex_10000us = [103.71087141036988,51.8652984380722,26.116928601264952,13.285402727127074,13.299086117744446,13.311230850219726,13.331144523620605,13.36794536113739]

    cdfkdirex_tot = cdfkdirex_0us + cdfkdirex_10us + cdfkdirex_1000us + cdfkdirex_10000us

    cdfkdirex_throughput = [10000 / t for t in cdfkdirex_tot]
    cdfkdirex_gran = 8*["0us"] + 8*["10us"] + 8*["1ms"] + 8*["10ms"]
    nworkers=4*[1,2,4,8,16,32,64,128]
    df = pd.DataFrame({GRANULARITY_YLABEL: cdfkdirex_throughput, "Workers": nworkers, "Granularity": cdfkdirex_gran})
    sns.lineplot(data=df, x="Workers", y=GRANULARITY_YLABEL, hue="Granularity", marker="o", ax=ax)

    ax.set_xscale(LogScale(1, base=2))
    ax.set_yscale(LogScale(2, base=2))
    ax.set_xticks(nworkers)
    ax.set_yticks([128, 256, 512, 1024, 2048, 4096, 8192], fontsize=9834)
    ax.get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
    ax.get_yaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())

    #plt.tick_params(axis='both', which='major', labelsize=14)
    #plt.legend(title='Company', fontsize=20)
    #plt.xlabel('Date', fontsize=16);
    #plt.ylabel('Sales', fontsize=16);
    #plt.title('Sales Data', fontsize=20)

    f.suptitle("Throughput of CDFK DIREX at Different Granularities")
    f.savefig("granularity_cdfkdirex.png")

def granularity_pdfkhtex():
    f, ax = plt.subplots(nrows=1, ncols=1, figsize=figsize)
    pdfkhtex_0us = [208.56073191165925,104.15164544582368,52.234071254730225,26.408666682243346,13.421913957595825,6.915656852722168, 3.7138410568237306, 2.0781458139419557]
    pdfkhtex_10us = [207.95815584659576,104.0417453289032,52.20868666172028,26.371598625183104,13.435020303726196,6.920794987678528,3.722451400756836,2.08894145488739]
    pdfkhtex_1000us = [208.93325073719024,104.5724549293518,52.44926130771637,26.460202550888063,13.460071396827697,6.91746289730072,3.7199410438537597,2.085188293457031]
    pdfkhtex_10000us = [209.156539273262,115.5913720369339,70.67908318042755,41.716539072990415,21.653223848342897,10.853071260452271,5.676747894287109,3.1015659093856813]
    pdfkhtex_tot = pdfkhtex_0us + pdfkhtex_10us + pdfkhtex_1000us + pdfkhtex_10000us
    pdfkhtex_throughput = [10000 / t for t in pdfkhtex_tot]
    pdfkhtex_gran = 8*["0us"] + 8*["10us"] + 8*["1ms"] + 8*["10ms"]
    nworkers=4*[1,2,4,8,16,32,64,128]
    df = pd.DataFrame({GRANULARITY_YLABEL: pdfkhtex_throughput, "Workers": nworkers, "Granularity": pdfkhtex_gran})
    sns.lineplot(data=df, x="Workers", y=GRANULARITY_YLABEL, hue="Granularity", marker="o", ax=ax)

    ax.set_xscale(LogScale(1, base=2))
    ax.set_yscale(LogScale(2, base=2))
    ax.set_xticks(nworkers)
    ax.set_yticks([128, 256, 512, 1024, 2048, 4096, 8192])
    ax.get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
    ax.get_yaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())

    #plt.tick_params(axis='both', which='major', labelsize=14)
    #plt.legend(title='Company', fontsize=20)
    #plt.xlabel('Date', fontsize=16);
    #plt.ylabel('Sales', fontsize=16);
    #plt.title('Sales Data', fontsize=20)

    f.suptitle("Throughput of Python DFK HTEX at Different Granularities")
    f.savefig("granularity_pdfkhtex.png")

def granularity_dask():
    f, ax = plt.subplots(nrows=1, ncols=1, figsize=figsize)
    dask_0us = [14.426973226107657,14.804283958580346,15.93439830718562,16.941377475298943,20.631867305841297, 35.54196242783219, 336.97042947039006]
    dask_10us = [14.737046020850538,14.952529602963477,15.723000893276184,17.05282292049378,20.74066207744181, 34.797179472260176, 361.94480409044775]
    dask_1000us = [14.46156904976815,14.890361172612756,15.635207520239055,16.917600916232914,20.17057673074305, 34.49043252468109,349.6363507889211]
    dask_10000us = [14.618960776180028,14.94802405629307,16.089843920152635,16.978489735815675,20.287164131738244, 35.151617508381605, 341.30363035816697]

    dask_tot = dask_0us + dask_10us + dask_1000us + dask_10000us
    dask_throughput = [10000 / t for t in dask_tot]
    dask_gran = 7*["0us"] + 7*["10us"] + 7*["1ms"] + 7*["10ms"]
    nworkers=4*[1,2,4,8,16,32,64]
    df = pd.DataFrame({GRANULARITY_YLABEL: dask_throughput, "Workers": nworkers, "Granularity": dask_gran})
    sns.lineplot(data=df, x="Workers", y=GRANULARITY_YLABEL, hue="Granularity", marker="o", ax=ax)

    ax.set_xscale(LogScale(1, base=2))
    ax.set_yscale(LogScale(2, base=2))
    ax.set_xticks(nworkers)
    # ax.set_yticks([128, 256, 512, 1024, 2048, 4096, 8192])
    ax.get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
    ax.get_yaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())

    f.suptitle("Throughput of Dask at different Granularities")
    f.savefig("granularity_dask.png")

def granularity_ray():
    f, ax = plt.subplots(nrows=1, ncols=1, figsize=figsize)
    ray_0us = [5.430666340980679,2.9773381864652038,1.5158570311032236,1.3555972293019294,1.322595653682947,1.3797629032284022,1.3706705102697014,1.375115935690701]
    ray_10us = [6.220524882432073,3.3465378382243216,1.6843417956493796,1.3774099230766297,1.3353450790047645,1.3294007359072566,1.364827434718609,1.334254747722298]
    ray_1000us = [20.40687863016501,10.239490812271834,5.1341957651078705,2.4855086233466865,1.4247257123701274,1.344102220516652,1.380251538939774,1.3954690925776958]
    ray_10000us = [113.53895511645824,56.83142975699157,28.581554535962642,14.401022431068123,7.273174765426665,3.6846698691137134,1.9250256136991084,1.3559844645671546]

    ray_tot = ray_0us + ray_10us + ray_1000us + ray_10000us
    ray_throughput = [10000 / t for t in ray_tot]
    ray_gran = 8*["0us"] + 8*["10us"] + 8*["1ms"] + 8*["10ms"]
    nworkers=4*[1,2,4,8,16,32,64,128]
    df = pd.DataFrame({GRANULARITY_YLABEL: ray_throughput, "Workers": nworkers, "Granularity": ray_gran})
    sns.lineplot(data=df, x="Workers", y=GRANULARITY_YLABEL, hue="Granularity", marker="o", ax=ax)

    ax.set_xscale(LogScale(1, base=2))
    ax.set_yscale(LogScale(2, base=2))
    ax.set_xticks(nworkers)
    ax.set_yticks([128, 256, 512, 1024, 2048, 4096, 8192])
    ax.get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())
    ax.get_yaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())

    f.suptitle("Throughput of Ray at different Granularities")
    f.savefig("granularity_ray.png")

def dfk_submit():
    f, ax = plt.subplots(nrows=1, ncols=1, figsize=figsize)
    runtime = [1475.3859, 1276.6666, 11250.5704, 1856.0599, 3799.3106, 2803.4114, 7644.1589, 24585.0347, 2675.361, 1286.1205, 2980.8965, 1148.6048, 2587.0421, 1515.1941, 2844.3188, 5700.1494, 1527.8517, 1167.9203, 70757.0171]
    tot = sum(runtime)
    runtime = [r /  tot for r in runtime]
    label = ["check cleanup", "create id", "pick executor", "get label", "create task", "update task state", "create app future", "remote files -> data futures", "update task record", "add task record to DAG", "gather dependencies", "add deps to task", "check dependency stats", "create task launch lock", "create done callback", "update task state", "monitoring", "done callback deps", "invoke launch if ready"]
    df = pd.DataFrame({"Runtime(%)": runtime, "Code Block": label})
    sns.barplot(df, x="Code Block", y="Runtime(%)", ax=ax, width=.4, errorbar=None)
    ax.tick_params(axis='x', rotation=-30)
    f.suptitle("DFK Submit function")
    f.savefig("dfk_submit.png")

def dfk_lir():
    f, ax = plt.subplots(nrows=1, ncols=1, figsize=figsize)
    runtime = [1089.2303,1205.5562,1771.5325,1419.0092,3165.9544,14077.818,4605.2466]
    tot = sum(runtime)
    runtime = [r / tot for r in runtime]
    label = ["get task id", "aquire launch lock", "check status pending", "check dependency count", "unwrap futures", "invoke launch", "ensure exec_fu is Future"]

    df = pd.DataFrame({"Runtime(%)": runtime, "Code Block": label})
    sns.barplot(df, x="Code Block", y="Runtime(%)", ax=ax, width=.4)
    ax.tick_params(axis='x', rotation=-30)
    f.suptitle("DFK Launch If Ready")
    f.savefig("dfk_lir.png")

def dfk_lau():
    f, ax = plt.subplots(nrows=1, ncols=1, figsize=figsize)
    runtime = [2095.6618,2758.8234,1226.6556,1170.9044+1459.0191]
    tot = sum(runtime)
    runtime = [r / tot for r in runtime]
    label = ["get func and args", "check memoizer", "get executor", "monitoring"]
    df = pd.DataFrame({"Runtime(%)": runtime, "Code Block": label})
    sns.barplot(df, x="Code Block", y="Runtime(%)", ax=ax, width=.4)
    ax.tick_params(axis='x', rotation=-30)
    f.suptitle("DFK Launch")
    f.savefig("dfk_lau.png")

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
#cdfkdirex_vs_all()
granularity_cdfkdirex()
granularity_pdfkhtex()
granularity_dask()
granularity_ray()
#dfk_submit()
#dfk_lir()
#dfk_lau()
#pandanite()
#pbft()
#mfmc()
