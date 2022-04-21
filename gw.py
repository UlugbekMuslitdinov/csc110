name = str(input("Enter filename: "))

try:
    f = open(name, 'r')
    print(len(f.read()))
    f.close()
except FileNotFoundError:
    print("File not found")
