def find_longest_words(file_path):
    with open(file_path, 'r') as file:
        words = file.read().split()
    
    max_length = len(max(words, key=len))
    longest_words = [word for word in words if len(word) == max_length]
    
    return longest_words

# Đường dẫn tới tệp
file_path = 'D:/a.txt'
print("Những từ dài nhất trong văn bản là:", find_longest_words(file_path))
