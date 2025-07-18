import subprocess


def download_from_m3u8(m3u8_url, output_path):
    command = [
        "ffmpeg",
        "-i", m3u8_url,
        "-c", "copy",
        "-bsf:a", "aac_adtstoasc",
        output_path
    ]
    subprocess.run(command)
