'''Assignment 4 task - 1'''
try:
    text_file=open("sample.txt",'r')
    print("Reading file content:")
    line_number=len(text_file.readlines())
    text_file.seek(0)
    for line,x in zip(text_file,range(1,line_number+1)):
        print(f"Line {x}: {line}",end="")
    #print(text_file.read(}))
    text_file.close()
except (FileNotFoundError, NameError):
    print("Error: The file \'sample.txt\' was not found.")
