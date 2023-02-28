#!../cdfkenv/bin/python3
import parsl
from parsl import python_app
from parsl.config import Config
from parsl.executors import HighThroughputExecutor
from parsl.app.errors import RemoteExceptionWrapper

parsl.load(Config(
    executors=[HighThroughputExecutor(
        cores_per_worker=1,
        label="cdfk_htex_test",
        worker_debug=True,
        max_workers=1,
        )],
    run_dir="runinfo"
    )
)

@python_app
def add():
    return 2 + 2

@python_app
def add_args(a, b):
    return a + b

@python_app
def add_defargs(a=2, b=2):
    return a + b

nums = [add_args(2,2),
        add_args(2,2), add_args(2,b=2), add_args(a=2,b=2),
        add_defargs(), add_defargs(2,2), add_defargs(a=2), add_defargs(b=2), add_defargs(2, b=2)]

args = ["an()", "aa(2,2)", "aa(2,b=2)", "aa(a=2,b=2)", "ad()", "ad(2,2)", "ad(a=2)", "ad(b=2)", "ad(2, b=2)"]

out = [n.result() for n in nums]
for index in range(len(out)):
    if isinstance(out[index], RemoteExceptionWrapper):
        try:
            out[index].reraise()
        except TypeError as e:
            print(args[index], str(e))
    else:
        assert out[index] == 4
        print(args[index], " passed")
