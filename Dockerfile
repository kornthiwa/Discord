# ใช้ Python 3.12 เป็น base image
FROM python:3.12

# ติดตั้ง FFmpeg
RUN apt-get update && \
    apt-get install -y --no-install-recommends ffmpeg && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# ตั้งค่า working directory
WORKDIR /app

# คัดลอกไฟล์ requirements.txt และไฟล์อื่นๆ ที่จำเป็น
COPY requirements.txt requirements.txt
COPY . .

# ติดตั้ง dependencies
RUN pip install --no-cache-dir -r requirements.txt

# สั่งให้ Docker รัน bot.py
CMD ["python", "bot.py"]
