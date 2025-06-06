#convert file contents to list
def file_list():
    file_path=os.path.join("mydir","file.txt")
    with open(file_path,"r") as f:
        read_file=f.read().splitlines()#splitlines() splits by newlines and removes them — no need to strip().
        print(read_file)
