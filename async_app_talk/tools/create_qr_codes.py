import qrcode
from pathlib import Path

images_dir = Path("images")
images_dir.mkdir(exist_ok=True)

img = qrcode.make("https://github.com/jneines/async_app")
img_path = images_dir / "async_app_repo_qr_code.png"
img.save(img_path.as_posix())

img = qrcode.make("https://jneines.github.io/async_app_talk_pycon_de_2024/intro.html")
img_path = images_dir / "async_app_talk_qr_code.png"
img.save(img_path.as_posix())

img = qrcode.make("https://rosennxt.wd3.myworkdayjobs.com/Rosenxt/job/Lingen/Full-Stack-Python-Developer--all-genders-welcome-_JR100211")
img_path = images_dir / "job_ad.png"
img.save(img_path.as_posix())


