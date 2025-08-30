try:
    with open("output.txt", "w") as file:
        text = input("Enter text to write to the file: ")
        file.write(text)
        print("Data successfully written to output.txt")

    with open("output.txt", "a") as file:
        text = input("Enter additional text to append: ")
        file.write("\n"+text)

    with open("output.txt", "r") as file:
        print("Final content of output.txt:")
        print(file.read(),end="\n")

except Exception as e:
    print(f"Error: {e}")
