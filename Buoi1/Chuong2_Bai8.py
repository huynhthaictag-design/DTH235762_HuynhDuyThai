''' Trong Python, có 3 loại lỗi chính khi lập trình:

Lỗi cú pháp (Syntax Error): Do viết sai quy tắc ngôn ngữ, ví dụ thiếu dấu hai chấm, dấu ngoặc.
Lỗi logic (Logic Error): Chương trình chạy nhưng cho kết quả sai do sai về mặt tư duy, thuật toán.
Lỗi khi chạy (Runtime Error): Xảy ra khi chương trình đang chạy, ví dụ chia cho 0, truy cập phần tử không tồn tại.
Cách bắt lỗi trong Python là dùng khối try...except:
try:
    # Đoạn mã có thể gây lỗi
    x = 10 / 0
except ZeroDivisionError:
    print("Lỗi chia cho 0!")
except Exception as e:
    print("Lỗi khác:", e)
Có thể dùng thêm finally để thực hiện đoạn mã dù có lỗi hay không:  
try:
    # Đoạn mã
except:
    # Xử lý lỗi
finally:
    # Luôn thực hiện
'''