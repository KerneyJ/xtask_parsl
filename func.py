from parsl import python_app, join_app 
from concurrent.futures import Future

@python_app
def no_op(sleeptime):
    import time
    time.sleep(sleeptime)
    return None

@python_app
def add(*args):
    accumulator = 0
    for v in args:
        accumulator += v
    return accumulator

@join_app
def fib(n):
    if n == 0:
        return add()
    elif n == 1:
        return add(1)
    else:
        return add(fib(n - 1), fib(n - 2))

def fibi(n):
    @python_app
    def add(a, b):
        return a + b
    start = time.time()
    counter = 0
    results = [0, 1]
    while counter < n - 1:
        counter += 1
        results.append(add(results[counter - 1], results[counter]))
    end = time.time()
    return start, end, results[-1].result()

# does n no ops
def noop(n, sleeptime):
    start = time.time()

    results = []
    for i in range(n):
       results.append(no_op(sleeptime))
    out = [r.result() for r in results]
    
    end = time.time()
    return start, end
# launchs a python app add function that peforms 2+2 n times
def nsums(n):
    @python_app
    def add():
        return 2 + 2
    start = time.time()
    results = []
    for i in range(n):
        results.append(add())
    out = [r.result() for r in results]
    end = time.time()
    for o in out:
        assert o == 4
    return start, end

if __name__ == '__main__':
    import datetime
    import parsl
    import os
    import gc
    import sys
    import cProfile
    import time
    import argparse
    from parsl.config import Config

    parser = argparse.ArgumentParser(
                    prog='func.py',
                    description='Test parsl with different workloads and numbers of workers')
    parser.add_argument("executor", type=str, help="htex, htexr(htex remote), xq(if defined), or wq", choices=["htex", "xq", "wq", "htexr"])
    parser.add_argument("blocks", type=int, help="number of execution blocks")
    parser.add_argument("workers", type=int, help="number of workers per block")
    parser.add_argument("benchmark", type=str, help="fib(recursive), fibi(iterative), noop, nsums", choices=["fib", "fibi", "noop", "nsums"])
    parser.add_argument("n", type=int, help="number of tasks")
    parser.add_argument("-s", "--sleep", dest="sleep_time", action="store", default=0, type=int, help="amount of time to sleep during noop in microseconds")
    parser.add_argument("-d", "--directory", dest="save_dir", action="store", default=0, type=str, help="directory to save Parsl runtime information(runinfo by default)")
    parser.add_argument("-v", "--verbose", dest="verbose", action="store_true", help="print extra runtime information")
    parser.add_argument("-p", "--profile", dest="profile", action="store_true", help="profile the submit script(i.e. DFK and Executor")
    parser.add_argument("-nogc", "--no_garbage_collector", dest="nogarbcoll", action="store_true", help="disable the garbage collection")
    args = parser.parse_args()

    cdfk = False
    try:
        import cdflow
        cdfk = True
        if args.verbose:
            print("CDFK Loaded")
    except:
        if args.verbose:
            print("CDFK Not loaded")

    start = 0
    end = 0
    result = None
    executor = None

    if args.executor == "htex":
        from parsl.executors import HighThroughputExecutor
        from parsl.providers import LocalProvider
        executor = HighThroughputExecutor(
            cores_per_worker=1,
            label=f"htex_{args.blocks}b_{args.workers}w",
            worker_debug=False,
            max_workers=args.workers,
            provider=LocalProvider(
                init_blocks=int(args.blocks),
                max_blocks=int(args.blocks),
                min_blocks=int(args.blocks),
                nodes_per_block=1,
            ),
        )
    elif args.executor == "xq":
        from parsl.executors import XQExecutor
        executor = XQExecutor(
            max_workers=int(args.workers),
        )
    elif args.executor == "wq":
        from parsl.executors import WorkQueueExecutor
        executor = WorkQueueExecutor(
            label=f"wq-parsl-app",
            port=9123,
            project_name="wq-parsl-app",
            shared_fs=False,
            full_debug=True,
        )
    elif args.executor =="htexr": # htex remote
        from parsl.executors import HighThroughputExecutor
        from parsl.providers import AdHocProvider, LocalProvider
        from parsl.channels import SSHChannel
        executor = HighThroughputExecutor(
            provider=LocalProvider(
                init_blocks=int(args.blocks),
                max_blocks=int(args.blocks),
                min_blocks=int(args.blocks),
                nodes_per_block=1,
                channel=SSHChannel(
                    hostname="64.131.114.141",
                    username="jamie",
                    key_filename="/home/jamie/.ssh/id_rsa",
                    script_dir="/mnt/lustre/script_dir",
                ),
            )
        )

    parsl.load(Config(
            executors=[executor],
            run_dir = args.save_dir if args.save_dir else "runinfo",
        )
    )
    if args.nogarbcoll:
        gc.disable()
    if args.verbose:
        init_objs = len(gc.get_objects())

    pr = cProfile.Profile()
    if args.profile:
        pr.enable()

    if args.benchmark == "fib":
        start = time.time()
        result = fib(args.n).result()
        end = time.time()
    elif args.benchmark == "noop":
        start, end = noop(args.n, args.sleep_time/1e6)
    elif args.benchmark == "nsums":
        start, end = nsums(args.n)
    elif args.benchmark == "fibi":
        start, end, result = fibi(args.n)

    if args.profile:
        pr.disable()
        pr.dump_stats(f"./prof/{args.executor}_{'cdfk_' if cdfk else ''}{args.executor}_{args.n}.prof")

    if args.verbose:
        end_objs = len(gc.get_objects())
        print("Test: ", end="")
        print(args.executor, args.blocks, args.workers, args.benchmark, args.n, end=" ")
        print(f"Result: {result}", end=" ")
        if cdfk:
            print(f"CDFK info: {cdflow.info_dfk()}", end=" ")

        print(f"Total Workers: {args.workers * args.blocks}", end=",")
        print(f"Objects created: {end_objs - init_objs}, Runtime:", end=" ")
    print(f"{end - start}")

