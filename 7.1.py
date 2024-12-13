input_file = open('D:/a.txt', 'r')

for line in input_file:
    s = ""
    i = len(line) - 1
    while i >= 0:
        s = s + line[i]
        i = i - 1
    print(s)

input_file.close()
