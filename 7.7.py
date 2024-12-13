def count_lines_in_file(fname):
    with open(fname, 'r') as file:
        lines = file.readlines()
    return len(lines)

# Đường dẫn tới tệp
file_path = 'D:/a.txt'
print("Số dòng trong tệp:", count_lines_in_file(file_path))
