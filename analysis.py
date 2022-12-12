#!../analysis/bin/python3

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

sns.set_theme(style="darkgrid")
f, ax = plt.subplots(nrows=1, ncols=1, figsize=(6.4,6.4))

direct = [1388.534497,	1345.062024,	1334.886472,	1332.460631,	1311.024984,	1329.632341,	1252.703534,	1329.25331]
htex = [94.78235409,	187.5222059,	361.6370001,	682.3828663,	1086.529425,	1314.838884,	1394.915254,	1383.433669]
nworkers = [1, 2, 4, 8, 16, 32, 64, 128]

df = pd.DataFrame({"Direct to Workers": direct, "HTEX": htex, "Number of Workers": nworkers})

sns.lineplot(df, x="Number of Workers", y="Direct to Workers", marker="o", label="Direct to Worker", ax=ax)
sns.lineplot(df, x="Number of Workers", y="HTEX", marker="o", label="HTEX", ax=ax)
f.suptitle("Direct to Worker vs HTEX")

f.savefig("direct_vs_htex.png")
