from parsl.config import Config
from parsl.executors import HighThroughputExecutor #, XQExecutor
from parsl.providers import LocalProvider
from parsl.launchers import SingleNodeLauncher

htex_1w   = Config(
    executors=[HighThroughputExecutor(
        cores_per_worker=1,
        label="htex_1cpw_1w",
        managed=True,
        worker_debug=False,
        max_workers=1,
        provider=LocalProvider(
            init_blocks=1,
            launcher=SingleNodeLauncher(debug=True, fail_on_any=False),
            max_blocks=1,
            min_blocks=1,
            nodes_per_block=1,
        ),
    )],
    run_dir="runinfo",
)


htex_test = Config(
    executors=[HighThroughputExecutor(
        cores_per_worker=1,
        label="htex_1cpw_4w",
        managed=True,
        worker_debug=True,
        max_workers=4,
        provider=LocalProvider(
            init_blocks=1,
            launcher=SingleNodeLauncher(debug=True, fail_on_any=False),
            max_blocks=1,
            min_blocks=1,
            nodes_per_block=1,
        ),
    )],
    run_dir="runinfo",
)
"""
xq_exp1 = Config(
    executors=[XQExecutor(
        max_workers=1,
    )],
    run_dir="runinfo"
)

xq_exp2 = Config(
    executors=[XQExecutor(
        max_workers=2,
    )],
    run_dir="runinfo"
)

xq_exp3 = Config(
    executors=[XQExecutor(
        max_workers=4,
    )],
    run_dir="runinfo"
)

xq_exp4 = Config(
    executors=[XQExecutor(
        max_workers=8,
    )],
    run_dir="runinfo"
)

xq_exp5 = Config(
    executors=[XQExecutor(
        max_workers=16,
    )],
    run_dir="runinfo"
)

xq_exp6 = Config(
    executors=[XQExecutor(
        max_workers=32,
    )],
    run_dir="runinfo"
)

xq_exp7 = Config(
    executors=[XQExecutor(
        max_workers=64,
    )],
    run_dir="runinfo"
)

xq_exp8 = Config(
    executors=[XQExecutor(
        max_workers=128,
    )],
    run_dir="runinfo"
)
"""
htex_exp1w = Config(
    executors=[HighThroughputExecutor(
        cores_per_worker=1,
        max_workers=1,
        provider=LocalProvider(
            init_blocks=1,
            launcher=SingleNodeLauncher(debug=True, fail_on_any=False),
            max_blocks=1,
            min_blocks=1,
        ),
    )],
    run_dir="runinfo"
)

htex_exp2w = Config(
    executors=[HighThroughputExecutor(
        cores_per_worker=1,
        max_workers=2,
        provider=LocalProvider(
            init_blocks=1,
            launcher=SingleNodeLauncher(debug=True, fail_on_any=False),
            max_blocks=1,
            min_blocks=1,
        ),
    )],
    run_dir="runinfo"
)

htex_exp4w = Config(
    executors=[HighThroughputExecutor(
        cores_per_worker=1,
        max_workers=4,
        provider=LocalProvider(
            init_blocks=1,
            launcher=SingleNodeLauncher(debug=True, fail_on_any=False),
            max_blocks=1,
            min_blocks=1,
        ),
    )],
    run_dir="runinfo"
)

htex_exp8w = Config(
    executors=[HighThroughputExecutor(
        cores_per_worker=1,
        max_workers=8,
        provider=LocalProvider(
            init_blocks=1,
            launcher=SingleNodeLauncher(debug=True, fail_on_any=False),
            max_blocks=1,
            min_blocks=1,
        ),
    )],
    run_dir="runinfo"
)

htex_exp16w = Config(
    executors=[HighThroughputExecutor(
        cores_per_worker=1,
        max_workers=16,
        provider=LocalProvider(
            init_blocks=1,
            launcher=SingleNodeLauncher(debug=True, fail_on_any=False),
            max_blocks=1,
            min_blocks=1,
        ),
    )],
    run_dir="runinfo"
)

htex_exp32w = Config(
    executors=[HighThroughputExecutor(
        cores_per_worker=1,
        max_workers=32,
        provider=LocalProvider(
            init_blocks=1,
            launcher=SingleNodeLauncher(debug=True, fail_on_any=False),
            max_blocks=1,
            min_blocks=1,
        ),
    )],
    run_dir="runinfo"
)

htex_exp64w = Config(
    executors=[HighThroughputExecutor(
        cores_per_worker=1,
        max_workers=64,
        provider=LocalProvider(
            init_blocks=1,
            launcher=SingleNodeLauncher(debug=True, fail_on_any=False),
            max_blocks=1,
            min_blocks=1,
        ),
    )],
    run_dir="runinfo"
)

htex_exp128w = Config(
    executors=[HighThroughputExecutor(
        cores_per_worker=1,
        max_workers=128,
        provider=LocalProvider(
            init_blocks=1,
            launcher=SingleNodeLauncher(debug=True, fail_on_any=False),
            max_blocks=1,
            min_blocks=1,
        ),
    )],
    run_dir="runinfo"
)

htex_exp1 = Config(
    executors=[HighThroughputExecutor(
        cores_per_worker=1,
        label="htex_1cpw_48w",
        managed=True,
        max_workers=48,
        provider=LocalProvider(
            init_blocks=1,
            launcher=SingleNodeLauncher(debug=True, fail_on_any=False),
            max_blocks=1,
            min_blocks=1,
        ),
    )],
    run_dir="runinfo",
)

htex_exp2 = Config(
    executors=[HighThroughputExecutor(
        cores_per_worker=1,
        label="htex_1cpw_96w",
        managed=True,
        max_workers=96,
        prefetch_capacity=200,
        provider=LocalProvider(
            init_blocks=1,
            launcher=SingleNodeLauncher(debug=True, fail_on_any=False),
            max_blocks=1,
            min_blocks=1,
        ),
    )],
    run_dir="runinfo",
)

htex_exp3 = Config(
    executors=[HighThroughputExecutor(
        cores_per_worker=1,
        label="htex_1cpw_144w",
        managed=True,
        max_workers=144,
        prefetch_capacity=200,
        provider=LocalProvider(
            init_blocks=1,
            launcher=SingleNodeLauncher(debug=True, fail_on_any=False),
            max_blocks=1,
            min_blocks=1,
        ),
    )],
    run_dir="runinfo",
)

htex_exp4 = Config(
    executors=[HighThroughputExecutor(
        cores_per_worker=1,
        label="htex_1cpw_192w",
        managed=True,
        max_workers=192,
        prefetch_capacity=200,
        provider=LocalProvider(
            init_blocks=1,
            launcher=SingleNodeLauncher(debug=True, fail_on_any=False),
            max_blocks=1,
            min_blocks=1,
        ),
    )],
    run_dir="runinfo",
)

htex_exp5 = Config(
    executors=[HighThroughputExecutor(
        cores_per_worker=1,
        label="htex_1cpw_48w",
        managed=True,
        max_workers=8,
        prefetch_capacity=200,
        provider=LocalProvider(
            init_blocks=1,
            launcher=SingleNodeLauncher(debug=True, fail_on_any=False),
            max_blocks=1,
            min_blocks=1,
            nodes_per_block=6,
        ),
    )],
    run_dir="runinfo",
)

htex_exp6 = Config(
    executors=[HighThroughputExecutor(
        cores_per_worker=1,
        label="htex_1cpw_96w",
        managed=True,
        max_workers=8,
        prefetch_capacity=200,
        provider=LocalProvider(
            init_blocks=1,
            launcher=SingleNodeLauncher(debug=True, fail_on_any=False),
            max_blocks=1,
            min_blocks=1,
            nodes_per_block=12,
        ),
    )],
    run_dir="runinfo",
)

htex_exp7 = Config(
    executors=[HighThroughputExecutor(
        cores_per_worker=1,
        label="htex_1cpw_144w",
        managed=True,
        max_workers=8,
        prefetch_capacity=200,
        provider=LocalProvider(
            init_blocks=1,
            launcher=SingleNodeLauncher(debug=True, fail_on_any=False),
            max_blocks=1,
            min_blocks=1,
            nodes_per_block=18,
        ),
    )],
    run_dir="runinfo",
)

htex_exp8 = Config(
    executors=[HighThroughputExecutor(
        cores_per_worker=1,
        label="htex_1cpw_192w",
        managed=True,
        max_workers=8,
        provider=LocalProvider(
            init_blocks=1,
            launcher=SingleNodeLauncher(debug=True, fail_on_any=False),
            max_blocks=1,
            min_blocks=1,
            nodes_per_block=24,
        ),
    )],
    run_dir="runinfo",
)

CONFIGS = {
        "htex_test": htex_test,
        "htex_exp1": htex_exp1,
        "htex_exp2": htex_exp2,
        "htex_exp3": htex_exp3,
        "htex_exp4": htex_exp4,
        "htex_exp5": htex_exp5,
        "htex_exp6": htex_exp6,
        "htex_exp7": htex_exp7,
        "htex_exp8": htex_exp8,
#        "xq_exp1": xq_exp1,
#        "xq_exp2": xq_exp2,
#        "xq_exp3": xq_exp3,
#        "xq_exp4": xq_exp4,
#        "xq_exp5": xq_exp5,
#        "xq_exp6": xq_exp6,
#        "xq_exp7": xq_exp7,
#        "xq_exp8": xq_exp8,
        "htex_exp1w": htex_exp1w,
        "htex_exp2w": htex_exp2w,
        "htex_exp4w": htex_exp4w,
        "htex_exp8w": htex_exp8w,
        "htex_exp16w": htex_exp16w,
        "htex_exp32w": htex_exp32w,
        "htex_exp64w": htex_exp64w,
        "htex_exp128w": htex_exp128w,
}

if __name__ == "__main__":
    for name, cnfg in CONFIGS.items():
        print(f"{name}: {cnfg}")
