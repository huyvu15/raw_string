def validate_user(username, minlen):
    # thêm 1 khẳng định
    assert type(username) == str, "username must be a string"
    if minlen < 1:
        raise ValueError("minlen must be at least 1")
    if len(username) < minlen:
        return False
    if not username.isalnum():
        return False
    return True

# case error : 
# validate_user("", -1)
validate_user(" ", 1)
validate_user([" "], 1)
validate_user("yeu mai ", 1)

# assert là từ khóa xác định 1 biểu thức có điều kiện đúng
# nếu nó sai nó sẽ làm tăng thêm 1 lỗi khẳng định với thông báo chỉ định

# testing expected error

