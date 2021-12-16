"""
I've choose to start cacluting the time in __enter__ function not in __init__, becouse if the user cretae obj from this
class it will call the __init__ function only once, but it will __enter__ we call the object

"""
import datetime
import os
import sys
import psutil


class Profiler:
    def __init__(self):
        print("init called")
        sys.stdout.write("the Profiler Start")
        self.start_time = datetime.datetime.now()
        self.start_memory = self.get_process_memory()

    def profiler(self):

        print("Profiling  resident set size(RES): {:>8} | total program size  (VMS): {:>8} |"
                         "| time: {:>8}".format(
            self.format_bytes(self.end_memory['res'] - self.start_memory['res']),
            self.format_bytes(self.end_memory['vms'] - self.start_memory['vms']),
            str(self.end_time - self.start_time)))

    def get_process_memory(self):
        process = psutil.Process(os.getpid())
        mi = process.memory_full_info()
        return {"res": mi.rss, "vms": mi.vms}

    def format_bytes(self, bytes):
        if abs(bytes) < 1000:
            return str(bytes) + "B"
        elif abs(bytes) < 1e6:
            return str(round(bytes / 1e3, 2)) + "kB"
        elif abs(bytes) < 1e9:
            return str(round(bytes / 1e6, 2)) + "MB"
        else:
            return str(round(bytes / 1e9, 2)) + "GB"

    def __call__(self, fn, *args, **kwargs):
        print("call called")
        to_execute = fn(*args, **kwargs)
        self.end_time = datetime.datetime.now()
        self.end_memory = self.get_process_memory()
        self.profiler()
        return to_execute



class WithProfiler:

    def __enter__(self):

        sys.stdout.write("the Profiler Start")
        self.start_time = datetime.datetime.now()
        self.start_memory = self.get_process_memory()

    def __exit__(self, exc_type, exc_val, exc_tb):

        self.end_time = datetime.datetime.now()
        self.end_memory = self.get_process_memory()
        self.profiler()

    def profiler(self):

        print("Profiling  resident set size(RES): {:>8} | total program size  (VMS): {:>8} |"
                         "| time: {:>8}".format(
            self.format_bytes(self.end_memory['res'] - self.start_memory['res']),
            self.format_bytes(self.end_memory['vms'] - self.start_memory['vms']),
            str(self.end_time - self.start_time)))

    def get_process_memory(self):
        process = psutil.Process(os.getpid())
        mi = process.memory_full_info()
        return {"res": mi.rss, "vms": mi.vms}

    def format_bytes(self, bytes):
        if abs(bytes) < 1000:
            return str(bytes) + "B"
        elif abs(bytes) < 1e6:
            return str(round(bytes / 1e3, 2)) + "kB"
        elif abs(bytes) < 1e9:
            return str(round(bytes / 1e6, 2)) + "MB"
        else:
            return str(round(bytes / 1e9, 2)) + "GB"
