from extract_links import get_video_links
from crawler import get_m3u8_url
from downloader import download_from_m3u8
from tqdm import tqdm
import os
import argparse


def main():
    parser = argparse.ArgumentParser(description="Video Crawler VTVgo")
    parser.add_argument("--url",
                        default='https://vtvgo.vn/video/catalog/list/vodchannel_1132/ban-tin-thoi-su-19h-khiem-thinh-11,vodchannel_1172.html',
                        help="Category URL")
    parser.add_argument("--output", default="downloads", help="Directory to save downloaded videos")
    args = parser.parse_args()

    category_url = args.url
    output_dir = args.output

    os.makedirs(output_dir, exist_ok=True)

    # Get toàn bộ url
    video_links = get_video_links(category_url)
    print(f"🔍 TÌM THẤY {len(video_links)} VIDEO")

    for i, url in enumerate(tqdm(video_links, desc="ĐANG TẢI DANH SÁCH VIDEO")):
        print(f"\n📺 [{i + 1}/{len(video_links)}] {url}")
        m3u8_url = get_m3u8_url(url)

        if m3u8_url:
            print(m3u8_url)
            output_file = os.path.join(output_dir, f"video_{i + 1}.mp4")
            download_from_m3u8(m3u8_url, output_file)
            print(f"✅ TẢI XONG: {output_file}")
        else:
            print("❌ KHÔNG TÌM THẤY LINK M3U8")


if __name__ == "__main__":
    main()
