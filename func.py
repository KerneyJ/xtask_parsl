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
    for n in range(n):
       results.append(no_op())

    while results:
        for i, r in enumerate(results):
            if r.done():
                results.pop(i)

if __name__ == '__main__':
    import cProfile
    import datetime
    import parsl
    import sys
    from config import CONFIGS
    USAGE = "Usage: func.py [config] [benchmark] [n] [options]"\
            "\n- where config is a parsl config from config.py"\
            "\n- benchmark is a type of benchmark fib or noop"\
            "\n- n is the number of ops or the fib number"\
            "\n- [options]:"\
            "\n\t-d [directory]: save parsl runtime information to this directory"
    def parseflags(cmdlst):
        print(cmdlst)
        for idx, arg in enumerate(cmdlst):
            print(arg)
            if arg == '-d':
                for name in CONFIGS.keys():
                    CONFIGS[name].run_dir = cmdlst[idx+1]

    if len(sys.argv) < 4:
        print(USAGE)
        exit()
    else:
        if len(sys.argv) > 4:
            print("parsing")
            parseflags(sys.argv[4:len(sys.argv)])
        print(CONFIGS[sys.argv[1]].run_dir)
        parsl.load(CONFIGS[sys.argv[1]])
        n = int(sys.argv[3])
        if sys.argv[2] == "fib":
            cProfile.run(f"fib({n}).result()", filename=f"prof/test_fib({n})_" + str(datetime.datetime.now()))
        elif sys.argv[2] == "noop":
            cProfile.run(f"noop({n})", filename=f"prof/test_noop({n})_" + str(datetime.datetime.now()))
        else:
            print(f"Benchmark type: {sys.argv[2]} non-existent")
            exit()
        print("test: ", end="")
        print(sys.argv, end=" ")
        print("done")
