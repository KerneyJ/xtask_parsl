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
def add_kwargs(a=2, b=2):
    return a + b

def print_fut_list(futs, args):
    out = [f.result() for f in futs]
    for index in range(len(out)):
        if isinstance(out[index], RemoteExceptionWrapper):
            try:
                out[index].reraise()
            except TypeError as e:
                print(args[index], str(e))
        else:
            print(f"{args[index]}: {out[index]}")
            # assert out[index] == 4
            # print(args[index], "passed")

# Test passing arguments
print("Testing argument passing")
print("an => add no arguments\n" \
        "aa => add arguments\n" \
        "ak => add keyword arguments")
nums = [add_args(2,2),
        add_args(2,2), add_args(2,b=2), add_args(a=2,b=2),
        add_kwargs(), add_kwargs(2,2), add_kwargs(a=2), add_kwargs(b=2), add_kwargs(2, b=2)]

args = ["an()", "aa(2,2)", "aa(2,b=2)", "aa(a=2,b=2)", "ak()", "ak(2,2)", "ak(a=2)", "ak(b=2)", "ak(2, b=2)"]
print_fut_list(nums, args)

print("\n\n",end='')
# Test dependencies
print("Testing dependencies")
a = add()
b = add_args(a, 3)
c = add_args(a, 4)
d = add_args(b, c)
print_fut_list([a,b,c,d], ["a", "b", "c", "d"])
