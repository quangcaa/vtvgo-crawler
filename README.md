# VTVgo Crawler

Dự án này cho phép **trích xuất liên kết video** từ một trang danh mục trên VTVgo, lấy **link stream dạng `.m3u8`**, và
**tải về dưới dạng video `.mp4`**.

---

## Tính năng

- Crawl toàn bộ liên kết video từ một chuyên mục trên VTVgo
- Tự động trích xuất link `.m3u8`
- Tải video bằng `ffmpeg`
- Hỗ trợ tùy chỉnh thư mục lưu video

---

## Cài đặt

### 1. Tải

```bash
git clone https://github.com/quangcaa/vtvgo-crawler.git
cd vtvgo-crawler
```

### 2. Tạo môi trường ảo

```
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
.venv\Scripts\activate     # Windows
```

### 3. Cài đặt thư viện

```bash
pip install -r requirements.txt
```

### 4. Cài đặt ffmpeg và thêm vào PATH để tải video

```
https://www.gyan.dev/ffmpeg/builds/#release-builds
```

---

## Cách sử dụng
```
python main.py                                 # default
python main.py --url URL --output dir/to/save  # custom URL and output
```
