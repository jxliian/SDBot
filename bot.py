import discord
import os
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("TOKEN")

intents = discord.Intents.default()
intents.members = True  # Para detectar nuevos usuarios

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Bot conectado como {bot.user}")

# Comando para expulsar usuarios
@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason="No especificado"):
    await member.kick(reason=reason)
    await ctx.send(f"👢 {member.mention} fue expulsado. Razón: {reason}")

# Comando para banear usuarios
@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason="No especificado"):
    await member.ban(reason=reason)
    await ctx.send(f"🔨 {member.mention} fue baneado. Razón: {reason}")

bot.run(TOKEN)
