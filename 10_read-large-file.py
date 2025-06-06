#Question: Simulate reading a very large text file (e.g., large_log.txt) by reading it in chunks of 100 bytes at a time and printing each chunk. Create a dummy large file for testing.

with open ("large_log.txt","w") as f:
    for _ in range(1000):
        f.write("this is a dummy log file\n") # writes 1000 lines 
def readfiles(file_name):
    with open("large_log.txt","r") as f:
        for i in range(10):
            chunk=f.read(100) #read 100 bytes at a tym
            print(f"'{i+1}' st chunk:")
            print(chunk)
    

readfiles("large_log.txt")
