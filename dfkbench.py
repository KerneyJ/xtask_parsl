#!../forkenv/bin/python
import time
from parsl.dataflow.dflow import DataFlowKernel
from parsl.config import Config
from parsl.executors import HighThroughputExecutor, XQExecutor
from parsl import python_app

xq_exp4 = Config(
    executors=[XQExecutor(
        max_workers=8,
    )],
    run_dir="runinfo"
)

dfk = DataFlowKernel(config=xq_exp4)

@python_app(data_flow_kernel=dfk)
def no_op():
    import time
    time.sleep(0)
    return None

def noop(n):
    results = []
    for _ in range(n):
        results.append(no_op())

    # out = [r.result() for r in results]

start = time.perf_counter()
noop(50000)
end = time.perf_counter()

print(f"Time: {end - start}")
