def write_list_to_file(file_path, lst):
    with open(file_path, 'w') as file:
        for item in lst:
            file.write("%s\n" % item)

# Danh sách cần viết vào tệp
lst = ["Python", "Java", "C++", "JavaScript"]
file_path = 'D:/languages.txt'
write_list_to_file(file_path, lst)
