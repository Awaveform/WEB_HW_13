import chardet

# file_path = 'D:/crackstation.txt/realuniq.lst'
file_path = 'D:/crackstation-human-only.txt/realhuman_phill.txt'

# # Determine the file encoding by reading the first 100 KB
# chunk_size = 102400  # 100 KB
# with open(file_path, 'rb') as raw_file:
#     result = chardet.detect(raw_file.read(chunk_size))
#     file_encoding = result['encoding']
#
# # Read the first line using 'latin-1' encoding
# with open(file_path, 'r', encoding='latin-1', errors='replace') as file:
#     first_line = file.readline()
#     print(first_line)

with open(file_path, 'r', encoding='utf-8') as file:
    first_line = file.readline()
    print(first_line)
