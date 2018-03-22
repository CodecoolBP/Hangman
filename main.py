def read_from_file(filename):
    file = open(filename)
    cont = file.readlines()
    for line in cont:
        print(line.strip("\n"))

