import cv2
import os
import subprocess
import requests

# Cấu hình GitHub
repository_url = "https://github.com/Ziiiqaztyu/gittest.git"
local_repo_path = r"E:\nothing"  # Đường dẫn lưu ảnh
image_name = "captured_image.jpg"
image_path = os.path.join(local_repo_path, image_name)

# Bước 1: Chụp ảnh và lưu vào repository local
camera = cv2.VideoCapture(0)
ret, frame = camera.read()

if ret:
    # Lưu ảnh
    cv2.imwrite(image_path, frame)
    print(f"Ảnh đã được lưu tại {image_path}")

    # Chuyển đến thư mục chứa repository
    os.chdir(local_repo_path)

    # Khởi tạo repository nếu chưa được khởi tạo
    if not os.path.exists(".git"):
        subprocess.run(["git", "init"])
        subprocess.run(["git", "remote", "add", "origin", repository_url])

    # Thực hiện các lệnh Git để đẩy ảnh lên GitHub
    subprocess.run(["git", "add", image_name])
    subprocess.run(["git", "commit", "-m", f"Add new image: {image_name}"])
    subprocess.run(["git", "push", "origin", "main"])
    print("Ảnh đã được đẩy lên GitHub.")
else:
    print("Không thể chụp ảnh từ camera.")
camera.release()

# Bước 2: Tải ảnh từ GitHub về máy khi cần
image_url = f"https://raw.githubusercontent.com/Ziiiqaztyu/gittest/main/{image_name}"
response = requests.get(image_url)

if response.status_code == 200:
    # Lưu ảnh xuống máy
    with open("downloaded_image_from_github.jpg", "wb") as file:
        file.write(response.content)
    print("Ảnh đã được tải về máy.")
else:
    print("Không thể tải ảnh từ GitHub.")
