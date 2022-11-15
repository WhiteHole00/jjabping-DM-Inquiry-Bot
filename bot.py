import discord
import time
from config import token,prefix
from discord import DMChannel

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Client_ID : {client.user.id}\nInvite_Link : https://discord.com/oauth2/authorize?client_id={client.user.id}&permissions=8&scope=bot')
    await client.change_presence(activity=discord.Streaming(name= f"문의는 여기로 DM!", url="https://www.twitch.tv/whitehole"))

@client.event
async def on_message(message):
    li = []

    if message.author == client.user:
        return
    
    if str(message.channel.type) == "private":
            await message.add_reaction('🟢')
            time.sleep(2)
            msg1 = """
            2018년 10월 18일부터 산업안전보건법에 고객응대근로자 보호조치가 시행되었습니다.
            고객응대 근로자에게 폭언, 폭행, 성희롱 등 모욕적인 언사가 있을 경우 서비스 상담은 중지되며 관련 내용은 산업안전보건법 위반 자료로 활용될 수 있습니다.
            """
            emb = discord.Embed(title="👪 고용노동부",description=msg1,color=discord.Colour.light_gray())
            await message.channel.send(embed=emb)
            await message.channel.send("https://cdn.discordapp.com/attachments/1038741912577904733/1041976321384923166/help.png")
            msg2 = f"""
            사진,파일 업로드 전송은 미지원하니 URL로 올려주시기 바랍니다.

            또, 1990자 이상의 텍스트는 지원하지 않습니다.
            해당 메시지는 24시간 자동 응답봇 서비스 입니다.
            관리자 연결중 입니다. 잠시만 기다려주세요.

            해당 봇에게는 복구키,웹패널 비밀번호 등을 보내지마세요.
            <@710437780546650143>(화이트홀미만잡#8210) 에게 보내주세요.
            """
            emb1 = discord.Embed(title="문의봇 - 화이트홀",description=msg2,color=discord.Colour.light_gray())
            await message.channel.send(embed=emb1)

            await client.get_channel(채널 아디).send(f"새로운 문의가 왔습니다!\n[{message.author.name}({message.author.id})] : {message.content}\n--------------------------")



    if message.channel.id == 채널아디 and message.author.guild_permissions.manage_messages:
        if message.content.startswith(f"{prefix}닫기"):
            try:
                user = await client.fetch_user(message.content[4:23])
                msg = message.content[23:]
            except Exception as e:
                await message.channel.send(f"명령어는 {prefix}닫기 [아이디] [답변] 형식으로 작성해주세요!.")
            await message.delete()
            await DMChannel.send(user, f"관리자 {message.author.name} : {msg}")
            await DMChannel.send(user , "https://cdn.discordapp.com/attachments/1038741912577904733/1038776316616523877/hehe.png")
            await DMChannel.send(user,embed=discord.Embed(title="문의봇 - 화홀",description="문의가 관리자에 의해 종료되었습니다.\n해당 메시지에는 답변 하지마세요.",color=discord.Colour.light_gray()))
            await message.channel.send(f"성공적으로 <@{user}>님에게 {msg} 전송을 완료 하였습니다!")




client.run(token)        
