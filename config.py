from parsl.config import Config
from parsl.executors import HighThroughputExecutor
from parsl.providers import LocalProvider
from parsl.launchers import SingleNodeLauncher

htex1 = Config(
    executors=[HighThroughputExecutor(
        cores_per_worker=1,
        label="htex_1cpw_8w",
        managed=True,
        max_workers=8,
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

htex2 = Config(
    executors=[HighThroughputExecutor(
        cores_per_worker=8,
        label="htex_8cpw_1w",
        managed=True,
        max_workers=1,
        provider=LocalProvider(
            init_blocks=1,
            launcher=SingleNodeLauncher(debug=True, fail_on_any=False),
            max_blocks=1,
            min_blocks=1,
            nodes_per_block=1,
        ),
    )],
    run_dir="runinfo"
)

CONFIGS = {"htex1": htex1, "htex2": htex2}
