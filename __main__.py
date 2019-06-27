import psutil
import json
from datetime import datetime
from time import sleep
import os

ospath = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(ospath, 'config.json'), 'r') as f:
    config = json.load(f)
    output = config.get("output")
    interval = int(config.get("interval"))


class SystemInfo:
    """Class for system monitoring"""
    snapshot_count = 0

    def display_stats():
        SystemInfo.snapshot_count += 1
        snapshot = SystemInfo.snapshot_count
        date = str(datetime.strftime(datetime.now(), "%m/%d/%Y, %H:%M:%S"))
        cpu = str(psutil.cpu_percent(interval=1))
        memory = str(psutil.disk_usage('/'))
        virtmem = str(psutil.virtual_memory())
        io = str(psutil.disk_io_counters())
        net = str(psutil.net_io_counters())
        return "SNAPSHOT %s: " \
               "TIMESTAMP %s: " \
               "Overall cpu load - %s %%; " \
               "Overall disk memory usage (bytes) - %s; " \
               "Overall virtual memory (bytes) - %s; " \
               "IO info - %s; " \
               "Network info - %s " \
               % (snapshot,
                   date,
                   cpu,
                   memory,
                   virtmem,
                   io,
                   net)

    def write_to_json(output_json):
        with open('output.json', 'a') as fjson:
            fjson.write(str(json.dumps(output_json, indent=4)) + '\n')

    def write_to_txt(output_txt):
        with open('output.txt', 'a') as txt:
            txt.write(output_txt + '\n')


if output == 'json':
    while True:
        SystemInfo.write_to_json(SystemInfo.display_stats())
        sleep(interval)
elif output == 'txt':
    while True:
        SystemInfo.write_to_txt(SystemInfo.display_stats())
        sleep(interval)
