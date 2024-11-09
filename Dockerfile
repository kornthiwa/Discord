# ใช้ Python 3.12 เป็น base image
FROM python:3.12

# ติดตั้ง FFmpeg
RUN apt-get update && \
    apt-get install -y ffmpeg && \
    apt-get clean

# ตั้งค่า working directory
WORKDIR /app

# คัดลอกไฟล์ requirements.txt และติดตั้ง dependencies
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# คัดลอกไฟล์อื่นๆ ที่จำเป็น
COPY . .

# สร้าง user ที่ไม่ใช่ root
RUN useradd -m myuser
USER myuser

# สั่งให้ Docker รัน bot.py
CMD ["python", "bot.py"]

# Health check (optional)
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8080 || exit 1
