def file_read_from_head(fname, nlines):
    from itertools import islice
    with open(fname) as f:
        for line in islice(f, nlines):
            print(line.strip())

file_read_from_head('D:/a.txt', 2)
