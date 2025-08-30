try:
    with open("sample.txt", 'r') as text_file:
        print("Reading file content:")
        lines = text_file.readlines()
        
        for i, line in enumerate(lines, start=1):
            print(f"Line {i}: {line}", end="")

except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")
