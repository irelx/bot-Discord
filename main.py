import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
discord.Intents.default()
load_dotenv()

TOKEN = os.getenv("TOKEN")

if TOKEN is None:
    print("TOKEN is missing. Please check your .env file.")
    exit()

# กำหนด Intents ให้บอท
intents = discord.Intents.default()
intents.message_content = True  # เปิดใช้งานการเข้าถึงเนื้อหาข้อความ
bot = commands.Bot(command_prefix="!", intents=intents)
# สร้าง Client (บอท)
client = discord.Client(intents=intents)

# เมื่อบอทพร้อมใช้งาน
@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

# เมื่อบอทได้รับข้อความ
@client.event
async def on_message(message):
    # ถ้าข้อความไม่มาจากบอทเอง
    if message.author == client.user:
        return

    # ตัวอย่างตอบกลับเมื่อมีข้อความ "setting adhello"
    if message.content.lower() == '!setting ad':
        await message.channel.send('# @everyone นี้คือคั้งค่า แอนดรอย คลิกเพื่อดูตั้งค่า https://drive.google.com/drive/folders/1Y-D9llHMl8k49F8JTIWsDqIWaQAgGIBm?usp=sharing ขอบคุณที่ไว้วางใจเราโปรดรีวิวที่ห้อง>>https://discord.com/channels/1336730374490820700/1345707058619482144 ')

    # ตัวอย่างตอบกลับข้อความ "setting pc"
    elif message.content.lower() == '!setting pc':
        await message.channel.send('# @everyone นี้คือตั้งค่าของคอม คลิกเพื่อดูตั้งค่า https://drive.google.com/drive/folders/1a-AtnMfQ8umVT47y6EgoZyPahKbGBE4b?usp=sharing ขอบคุณที่ไว้วางใจเราโปรดรีวิวที่ห้อง>>https://discord.com/channels/1336730374490820700/1345707058619482144')

    # ตัวอย่างตอบกลับข้อความ "ขึ้นสตีมละ"
    elif message.content.lower() == 'ขึ้นสตีมละ':
        await message.channel.send('# @everyone ขึ้นสตรีมละเข้ามากดใจให้ทีหาเสี่ยเปย์อยู่นะ >>ช่อง https://www.tiktok.com/@irelx44?lang=th-TH')

    # ตัวอย่างตอบกลับข้อความ "ซีอยู่ไหม"
    elif message.content.lower() == 'ซื้อของ':
        await message.channel.send('# @here มี แอนดรอย ios pc (เลือกแล้วพิมแค่นั้นเช่น "pc") เป็นตั้งค่าของเกมไม่เกี่ยวกับไฟล์เกม')

    # ตัวอย่างตอบกลับข้อความ "ซีอยู่ไหม"
    elif message.content.lower() == 'มีตั้งค่า':
        await message.channel.send('# เอาของอะไรดีครับ')

    # ตัวอย่างตอบกลับข้อความ "ซีอยู่ไหม"
    elif message.content.lower() == 'มีตั้งค่าiosไหม':
        await message.channel.send('# มีครับ 30บาท')

            # ตัวอย่างตอบกลับข้อความ "ซีอยู่ไหม"
    elif message.content.lower() == 'มีตั้งค่าแอนดรอยไหมครับ':
        await message.channel.send('# มีครับ ราคา 100 ')

            # ตัวอย่างตอบกลับข้อความ "ซีอยู่ไหม"
    elif message.content.lower() == 'มีตั้งค่าแอนดรอยไหม':  
        await message.channel.send('# มีครับ 30บาท ')
        
            # ตัวอย่างตอบกลับข้อความ "ซีอยู่ไหม"
    elif message.content.lower() == 'pc':
        await message.channel.send('# -100 บาท โอนเงิน>>https://discord.com/channels/1336730374490820700/1345784818536808448 ซื้อยศ pc จะได้ยศมาแล้วจะเห็นห้อง https://discord.com/channels/1336730374490820700/1345879820592087080 ')
        
            # ตัวอย่างตอบกลับข้อความ "ซีอยู่ไหม"
    elif message.content.lower() == 'ios':
        await message.channel.send('# -50บาท โอนเงิน>>https://discord.com/channels/1336730374490820700/1345784818536808448 ซื้อยศ IOS จะได้ยศมาแล้วจะเห็นห้อง https://discord.com/channels/1336730374490820700/1345882853304701050 ')
        
            # ตัวอย่างตอบกลับข้อความ "ซีอยู่ไหม"
    elif message.content.lower() == 'แอนดรอย':
        await message.channel.send('# -30บาท โอนเงิน>>https://discord.com/channels/1336730374490820700/1345784818536808448 ซื้อยศ android จะได้ยศมาแล้วจะเห็นห้อง https://discord.com/channels/1336730374490820700/1345882598726959207 ')
        
            # ตัวอย่างตอบกลับข้อความ "ซีอยู่ไหม"
    elif message.content.lower() == 'ไปละ':
        await message.channel.send('# มึงจะไปไหนมาโดเนทให้ไอซีก่อน')
        
            # ตัวอย่างตอบกลับข้อความ "ซีอยู่ไหม"
    elif message.content.lower() == 'ลีค':
        await message.channel.send('@everyone คนไหนที่เป็นลีคหรือมียศให้เข้าห้องพูดคุยมารอนะครับมีซ้อม')
        
            # ตัวอย่างตอบกลับข้อความ "ซีอยู่ไหม"
    elif message.content.lower() == 'เหงา':
        await message.channel.send('เหงาใช่ไหมลองหาแฟนดูนะ')
        
            # ตัวอย่างตอบกลับข้อความ "ซีอยู่ไหม"
    elif message.content.lower() == 'จะหายังไง':
        await message.channel.send('ก็ลองหาคู่ในOME ดู')
        
            # ตัวอย่างตอบกลับข้อความ "ซีอยู่ไหม"
    elif message.content.lower() == 'โดเนทยังไง':
        await message.channel.send(' https://ezdn.app/Tully -ลิ้งโดเนทตอนสตรีม ')
        
            # ตัวอย่างตอบกลับข้อความ "ซีอยู่ไหม"
    elif message.content.lower() == 'ซื้อตั้งค่ายังไง':
        await message.channel.send('# https://discord.com/channels/1336730374490820700/1340606490582454304 <<ห้องนี้>> -เปิดห้องแล้วพิม(ซื้อของ)')
        
            # ตัวอย่างตอบกลับข้อความ "ซีอยู่ไหม"
    elif message.content.lower() == 'รวมลิ้ง':
        await message.channel.send('# -โดเนทhttps://ezdn.app/Tully ><-Discord https://discord.gg/5AD9PRbfPb ><-Tiktok https://www.tiktok.com/@irelx44?lang=th-TH')
        
            # ตัวอย่างตอบกลับข้อความ "ซีอยู่ไหม"
    elif message.content.lower() == 'เวลาสตรีมทั้งหมด':
        await message.channel.send('# @here 12.00-14.00 18.00-23.00')
        
            # ตัวอย่างตอบกลับข้อความ "ซีอยู่ไหม"
    elif message.content.lower() == 'สมัคVIPยังไง':
        await message.channel.send('https://discord.com/channels/1336730374490820700/1345784818536808448 ซื้อVIPห้องนี้ หลังจกาซื้อแล้วจะได้ยศมา https://discord.com/channels/1336730374490820700/1340606490582454304 มาเปิดห้องแล้วพิมว่า ซื้อVแล้วครับ (พิมคำอื่นบอทจะไม่ตอบ)')
        
            # ตัวอย่างตอบกลับข้อความ "ซีอยู่ไหม"
    elif message.content.lower() == 'ซื้อVแล้วครับ':
        await message.channel.send('เรียบร้อยครับโปรดส่งIDเกม และแคปหน้าเกมมาในแชทนี้ พร้อมบอกชื่ออยากให้ตั้ง ขอบคุณที่ใช้บริการ >>https://discord.com/channels/1336730374490820700/1345707058619482144 ฝาก+1ด้วยนะครับ ')

    # เพิ่มคำสั่งใหม่ที่คุณต้องการ เช่น "time"
    elif message.content.lower() == 'time':
        from datetime import datetime
        now = datetime.now()
        await message.channel.send(f'เวลาปัจจุบัน: {now.strftime("%H:%M:%S")}')

    # เพิ่มคำสั่งใหม่ที่คุณต้องการ เช่น "hello_owner" (เฉพาะเจ้าของบอท)
    elif message.content.lower() == 'hello bot':
        if message.author.id == 848169677585907723:  # เปลี่ยน YOUR_USER_ID เป็น ID ของเจ้าของบอท
            await message.channel.send('สวัสดีเจ้าของบอท')
        else:
            await message.channel.send('คุณไม่มีสิทธิ์ใช้คำสั่งนี้!')

@bot.command()
async def hello(ctx):
    await ctx.send("สวัสดีครับ!")

bot.run(TOKEN)
