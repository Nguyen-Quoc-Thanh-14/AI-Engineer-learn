# PR02.01–PR02.02: Bài lab C extension thật (CPython 3.15.2)

Bài lab kèm chương PR02, không thay thế các nội dung hiện có. Module \`course_math\` dùng \`Py_TARGET_ABI3T = 0x30f0000\`, module slots của ABI mới, không duy trì trạng thái Python có thể thay đổi ở mức toàn cục và xuất một hàm \`cube_checked\`.

**Mục tiêu:** xây dựng một C extension có thể import trên CPython 3.15.2 thường và free-threaded bằng *cùng một file nhị phân* \`.abi3t.so\` từ build thường; xác minh GIL không bật lại, phép tính số nguyên rất lớn không gây tràn C integer, đầu vào sai kiểu báo TypeError.

**Giới hạn:** bài lab được kiểm thử trên Linux; chưa có bằng chứng Windows, GPU hoặc extension khác. Kiểm thử việc không bật GIL không bảo đảm mọi thư viện C khác thread-safe. Cần rà soát thêm ownership, object lifetime, lock strategy với trạng thái mutable.

**Nguồn chuẩn:** https://docs.python.org/3/howto/abi3t-migration.html
