#convert to dictionary
def file_dict():
    file_path=os.path.join("mydir","file.txt")
    data_dict={}
    with open(file_path,"r") as f:
        for lines in f:
            if ':' in lines:
                key,value=lines.strip().split(':',1)
                #line.strip() removes whitespace and the newline \n.
                #split(':', 1) splits the line into two parts only at the first colon:
                data_dict[key]=value
    print(data_dict)
