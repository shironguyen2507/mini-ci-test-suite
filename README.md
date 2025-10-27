# mini-ci-test-suite

Source code testing &amp; automation (Mini CI + Test Suite using GitHub Actions)

### Cấu trúc thư mục

.
├─ src/
│ └─ app/
│ └─ math_ops.py # mã nguồn mẫu để test
├─ tests/
│ ├─ conftest.py # thêm src vào sys.path (tránh lỗi import)
│ └─ test_math_ops.py # 2 bài test đầu tiên
├─ requirements.txt # công cụ dev/test
└─ (đã có) .gitignore, README.md
