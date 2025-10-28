import sys
from pathlib import Path

# Thêm đường dẫn /src vào sys.path để `from app...` hoạt động trên mọi OS/IDE
ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))
