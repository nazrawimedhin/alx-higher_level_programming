def read_file(filename=""):
    with open("filename", encoding="utf-8", mode="r") as my_file:
        my_file = filename.read()
        print(my_file)