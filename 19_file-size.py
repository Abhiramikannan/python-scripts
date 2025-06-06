import os
file_path=os.path.abspath(".")
for f in os.listdir(file_path):
        fp=os.path.join(file_path,f)
        size=os.path.getsize(fp)
        print(fp," :size  is: ",size)

#os.system("du -h")
