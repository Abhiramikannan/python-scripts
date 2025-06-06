#disk

import shutil,os,re
path=os.path.abspath(".")
usage=shutil.disk_usage(path)
print(usage)

#cpu percentage

cpu=psutil.cpu_percent(interval=1) #wait for 1 sec
print(cpu)  #inside venv try//pip install psutil

# #memory usage
memory=psutil.virtual_memory()
print(memory)
print(f"Total memory,{memory.total /1024**3:.2f} GB")
print(f"available,{memory.available /1024**3:.2f} GB")

#network statistics
net=psutil.net_io_counters()
print(net)
