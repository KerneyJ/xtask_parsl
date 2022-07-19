from parsl.config import Config
from parsl.executors import HighThroughputExecutor
from parsl.providers import LocalProvider
from parsl.launchers import SingleNodeLauncher

htex_test = Config(
    executors=[HighThroughputExecutor(
        cores_per_worker=1,
        label="htex_1cpw_4w",
        managed=True,
        max_workers=4,
        worker_debug=True,
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

htex_exp1 = Config(
    executors=[HighThroughputExecutor(
        cores_per_worker=1,
        label="htex_1cpw_48w",
        managed=True,
        max_workers=8,
        worker_debug=True,
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

htex_exp2 = Config(
    executors=[HighThroughputExecutor(
        cores_per_worker=1,
        label="htex_1cpw_96w",
        managed=True,
        max_workers=8,
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

htex_exp3 = Config(
    executors=[HighThroughputExecutor(
        cores_per_worker=1,
        label="htex_1cpw_144w",
        managed=True,
        max_workers=8,
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

htex_exp4 = Config(
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
CONFIGS = {"htex_test": htex_test, "htex_exp1": htex_exp1, "htex_exp2": htex_exp2, "htex_exp3": htex_exp3, "htex_exp4": htex_exp4}

if __name__ == "__main__":
    for name, cnfg in CONFIGS.items():
        print(f"{name}: {cnfg}")
