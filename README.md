# โปรเจกต์ Discord Bot

โปรเจกต์นี้เป็น Discord bot ที่ออกแบบมาเพื่อโต้ตอบกับเซิร์ฟเวอร์ Discord โดยใช้คำสั่งและฟังก์ชันต่าง ๆ คู่มือนี้อธิบายวิธีการตั้งค่า การรันบอท และการใช้งาน Docker

## ข้อกำหนดเบื้องต้น

- **Python** (เวอร์ชัน 3.12 ขึ้นไป)
- **Pip**: สำหรับติดตั้งแพ็กเกจ Python ที่จำเป็น
- **Docker** (ทางเลือก): สำหรับการใช้งานในคอนเทนเนอร์

## วิธีการตั้งค่า

1. **โคลนโปรเจกต์** (ถ้ายังไม่ได้โคลน):

   ```bash
   git clone https://github.com/kornthiwa/discord.git
   cd discord
   ```

2. **สร้างและเปิดใช้งาน virtual environment**:

   ```bash
   # สร้าง virtual environment
   python -m venv .venv

   # เปิดใช้งาน virtual environment
   # สำหรับ Windows:
   .venv\Scripts\activate

   # สำหรับ MacOS/Linux:
   source .venv/bin/activate

   # ปิดการใช้งาน virtual environment เมื่อเสร็จสิ้น:
   deactivate
   ```

3. **ติดตั้ง dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **สร้างไฟล์ .env**:

   ```env
   DISCORD_TOKEN=YOUR_DISCORD_BOT_TOKEN
   ```

5. **รันโปรแกรม**:

   ```bash
   # รันโดยตรงด้วย Python
   python bot.py
   ```

6. **การใช้งานด้วย Docker**:

   ```bash
   # สร้าง Docker image
   docker build -t discord-bot .

   # รัน Docker container
   docker run --env-file .env discord-bot
   ```

7. **การใช้งานด้วย setup.bat (สำหรับ Windows)**:

   ```bash
   # รันไฟล์ setup.bat เพื่อตั้งค่าสภาพแวดล้อมอัตโนมัติ
   setup.bat
   # หรือ
   .\setup.bat
   ```

   ไฟล์ setup.bat จะทำการ:
   - สร้าง virtual environment
   - เปิดใช้งาน virtual environment
   - ติดตั้ง dependencies ที่จำเป็นทั้งหมด
   - รันบอทโดยอัตโนมัติ

## การใช้งานคำสั่งพื้นฐาน

- `/help` - แสดงคำสั่งทั้งหมดที่ใช้ได้
- `/ping` - ทดสอบการเชื่อมต่อของบอท


discord/
│
├── discord/            # โฟลเดอร์หลักของโปรเจค
│   ├── __init__.py     # ทำให้โฟลเดอร์นี้เป็น package
│   ├── bot.py          # ไฟล์หลักสำหรับบอท Discord
│   ├── commands/       # โฟลเดอร์สำหรับเก็บคำสั่งต่างๆ
│   │   ├── __init__.py
│   │   ├── command1.py
│   │   └── command2.py
│   ├── events/         # โฟลเดอร์สำหรับเก็บ event handlers
│   │   ├── __init__.py
│   │   ├── on_ready.py
│   │   └── on_message.py
│   └── utils/          # โฟลเดอร์สำหรับเก็บ utilities หรือ helper functions
│       ├── __init__.py
│       └── helpers.py
│
├── tests/              # โฟลเดอร์สำหรับเก็บ unit tests
│   ├── __init__.py
│   ├── test_bot.py
│   └── ...
│
├── docs/               # เอกสารประกอบโปรเจค
│   └── ...
│
├── scripts/            # สคริปต์ที่ใช้ในการจัดการโปรเจค
│   └── ...
│
├── requirements.txt    # รายการ dependencies ของโปรเจค
├── setup.py            # สคริปต์สำหรับการติดตั้งโปรเจค
├── README.md           # คำอธิบายโปรเจค
└── .gitignore          # ไฟล์ที่ไม่ต้องการให้ git ติดตาม 
