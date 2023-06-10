import re

result = re.search(r"like", "Huy like it") # r là rawstring


print(result)

print(re.search(r"^x", "xenon")) # ^ đánh dấu vị trí bắt đầu của chuỗi
print(re.search(r"p.ng" , "penguin")) # . là chỉ các phần tử bất kỳ trong .
print(re.search(r"p.ng", "Pangaea", re.IGNORECASE)) # tìm kiếm không phân biệt chữ hoa chữ thường

print(re.search(r"[Pp]ython", "Python"))# [có thể chữ trong đây]
print(re.search(r"[a-z]way", "The end of the highway")) # 1 ký tự trong [a-z]
print(re.search("cloud[a-zA-Z0-9]", "cloudy"))
print(re.search("cloud[a-zA-Z0-9]", "cloud9"))

# tạo mẫu tìm kiếm không phải chữ cái
print(re.search(r"^a -zA-Z", "This is a sentence with spaces."))

print(re.search(r"cat|dog", "I like cats.")) # Tìm kiếm có 1 trong 2

print(re.search(r"Py.*n", "Pygmailion")) # .* là từ đấy đến toàn bộ

print(re.search(r"Py.*n", "Python Programming")) # nó chỉ lấy đến n
print(re.search(r"Py[a-z]*n", "Python Programming")) # .* là từ đấy đến toàn bộ

print(re.search(r"o+l+", "goldfish")) # chỉ tìm những cái có o có l phải liên tiếp
print(re.search(r"p?each", "To each their own"))
print(re.search(r"p?each", "I like peaches")) # ch

print(re.search(r"\.com", "mydomain.com"))
print(re.search(r"\w*"," This is an example"))
# s để khớp các ký tự khoảng trắng
# b cho danh giới giữa từ và 1 vài ký tự khác

print(re.search(r"^A.*a$", "Azerbaija"))
# bắt đầu bằng A và kết thúc bằng a
# $ là ký tự kết thúc

pattern = r"^[a-zA-Z_][a-zA-Z0-9_]*$"
print(re.search(pattern, "_this_is_a_valid_varible_name"))
print(re.search(pattern, "2my_wahy")) # số ở đầu thì ko hợp

# kiểm tra tên 1 sinh viên có họ , tên
a =  re.search(r"^(\w*), (\w*)$", "Lovelace, Ada")
print(a)

print(a.group())
print(a[0])
print(a[1])
print(a[2])

print(f"{a[2]} {a[1]} ")

def rearrange_name(name ):
    a = re.search(r"([\w .-]*), ([\w .-]*)$", name)
    if a == None:
        return name
    return "{} {}".format(a[2], a[1])

rearrange_name("Lovelace, Ada")
rearrange_name("Hopper, Grace M.")

print(re.search(r"[a-zA-Z]{5}", "a ghost")) # tìm những từ nào có 5 từ đầu tiên

# sử dụng chức năng findall
print(re.findall(r"[a-zA-Z]{5}", "a scary ghost appeared")) # tìm tất cả từ có 5 từ đầu tiên và lấy ra 5 chữ cái đó

# khớp tất cả các từ có 5 chữ cái chỉ có duy nhất 5 chữ cái trong từ
# like this: trong như này
print(re.findall(r"\b[a-zA-Z]{5}\b", "A scary ghost appeared"))

# mở rộng giới hạn số từ
# ví dụ từ 5 - 10 words 
print(re.findall(r"\w{5,10}", "I really like strawberries"))

# từ 5 từ trở lên chú ý là ko đc để space trong ""
print(re.findall(r"\w{5,}", "I really like strawberries"))

# từ chữ s đến 20 ký tự 
print(re.findall(r"s\w{,20}", "i really like strawberries"))



