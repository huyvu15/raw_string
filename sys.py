import sys

# nếu truyền vào đây 1 file .txt nó sẽ tự dộng viết hoa chữ cái đầu của mỗi dòng

# viết hoa chưa cái đầu
for line in sys.stdin:
    print(line.strip().capitalize()) # sử dụng strip để loại bỏ \n mỗi dòng
    