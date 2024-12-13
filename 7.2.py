k = open('D:/a.txt', 'r')

char, wc, lc = 0, 0, 0

for line in k:
    lc += 1
    char += len(line)
    wc += len(line.split())

print("Số ký tự là: %d\nSố từ là: %d\nSố dòng là: %d" % (char, wc, lc))

k.close()
