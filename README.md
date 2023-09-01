# raw_string
Tổng hợp thao tác với string cực kỳ hữu dụng

Regex phổ biến

\w+: để nối các từ

\d: khớp các chữ số 

\s: khớp với dấu space, .

.*: phù hợp với tất cả ký tự

+or*: lấy đi sự lặp lại của các chữ số đơn lẻ hoặc toàn bộ mẫu 

\S: không phải là khoảng trắng

[a-e]: nhóm ký tự   

[A-Za-z]: full từ A - z

[0 - 9]: tự hiểu

[A-Za-z\-\.]+: 'My-website.com

(a-z): 'a-z'

(\s+l,): ","

## 1 số method:

> split: chia nhỏ

> findall: tìm kiếm 

> search:

> match: kết hợp 

Sử dụng phương thức ngoặc 

Để định nghĩa 1 group sử dụng dấu ngoặc đơn () 

Xác định ký tự rõ ràng sử dụng dấu []

## Ví dụ:

re.split('\s+', "split and space") 

--> ["split", "and", "space"]

# nltk library: nature language toolkit

sử dụng phương thức: word_tokenize để chia nhỏ 1 chuỗi thành các mã thông báo

sent_tokenize: Chia tài liệu thành các câu riêng lẻ


