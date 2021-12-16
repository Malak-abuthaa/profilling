from Profiler import Profiler


@Profiler()
def any_function_to_test():
    arr = []
    for i in range(100000):
        print(i)
        arr.append(i)


any_function_to_test()
