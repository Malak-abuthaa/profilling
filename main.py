from Profiler import Profiler

if __name__ == '__main__':
    with Profiler():
        for i in range(100000):
            print(i)
