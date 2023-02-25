from parsl import python_app, join_app 

@python_app
def no_op():
    import time
    time.sleep(0)
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

# does n no ops
def noop(n):
    results = []
    for i in range(n):
       results.append(no_op())

    out = [r.result() for r in results]

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
    return start, end

if __name__ == '__main__':
    import datetime
    import parsl
    import os
    import sys
    import os
    import time
    from parsl.config import Config
    USAGE = "Usage: func.py [executor] [blocks] [workers] [benchmark] [n] [options]"\
            "\n- [executor]  xq, wq, or htex"\
            "\n- [blocks]    integer number of blocks"\
            "\n- [workers]   integer number of workers"\
            "\n- [benchmark] fib noop or nsums"\
            "\n- [n]         integer"\
            "\n- [options]:"\
            "\n\t-d [directory]: save parsl runtime information to this directory"
    start = 0
    end = 0
    result = None
    def parseflags(cmdlst):
        parsed_args = {}
        for idx, arg in enumerate(cmdlst):
            if arg == '-d':
                parsed_args["dir"] = cmdlst[idx+1]
        return parsed_args

    if len(sys.argv) < 6:
        print(USAGE)
        exit()
    else:
        exec_arg = sys.argv[1]
        blocks_arg = sys.argv[2]
        workers_arg = sys.argv[3]
        benchmark_arg = sys.argv[4]
        n_arg = sys.argv[5]
        parsed_args = None
        dir_arg = None

        if len(sys.argv) > 6:
            parsed_args = parseflags(sys.argv)
            if "dir" in parsed_args:
                dir_arg = parsed_args["dir"]

        # get executor
        executor = None
        if exec_arg == "htex":
            from parsl.executors import HighThroughputExecutor
            from parsl.providers import LocalProvider
            executor = HighThroughputExecutor(
                cores_per_worker=1,
                label=f"htex_{blocks_arg}b_{workers_arg}w",
                worker_debug=False,
                max_workers=int(workers_arg),
                provider=LocalProvider(
                    init_blocks=int(blocks_arg),
                    max_blocks=int(blocks_arg),
                    min_blocks=int(blocks_arg),
                    nodes_per_block=1,
                ),
            )
        elif exec_arg == "xq":
            from parsl.executors import XQExecutor
            executor = XQExecutor(
                max_workers=int(workers_arg),
            )
        elif exec_arg == "wq":
            from parsl.executors import WorkQueueExecutor
            executor = WorkQueueExecutor(
                label=f"wq-parsl-app",
                port=9123,
                project_name="wq-parsl-app",
                shared_fs=False,
                full_debug=True,
            )
        else:
            print(f"executor argument: {exec_arg} invalid")
            exit()

        parsl.load(Config(
                executors=[executor],
                run_dir = dir_arg if dir_arg else "runinfo",
            )
        )

        if benchmark_arg == "fib":
            start = time.time()
            result = fib(int(n_arg)).result()
            end = time.time()
        elif benchmark_arg == "noop":
            start = time.time()
            noop(int(n_arg))
            end = time.time()
        elif benchmark_arg == "nsums":
            start, end = nsums(int(n_arg))
        else:
            print(f"Benchmark type: {benchmark_arg} non-existent")
            exit()

        print("Test: ", end="")
        print(exec_arg, blocks_arg, workers_arg, benchmark_arg, n_arg, end=" ")
        print(f"Result: {result}", end=" ")
        print(f"Time: {end - start}")
