import discord
from discord.ext import commands
from functions import gen_pass

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

scamtype = {
    "pix": "Evite transferir dinheiro para desconhecidos. Confira o destinatário e desconfie de pedidos urgentes de pagamento.",
    "whatsapp": "Nunca compartilhe códigos de verificação. Desconfie de mensagens suspeitas e confirme a identidade de quem solicita dinheiro.",
    "jogos": "Evite baixar jogos e APKs de fontes desconhecidas. Não compartilhe sua conta e desconfie de ofertas muito vantajosas.",
    "lojas": "Verifique a reputação da loja, confira o endereço do site e desconfie de preços muito abaixo do mercado."
}


@bot.event
async def on_ready():
    print(f"Estamos logados como {bot.user}")


@bot.command()
async def scam(ctx, *, scam_type: str = ""):
    scam_type = scam_type.lower().strip()

    if scam_type in scamtype:
        await ctx.send(
            f"**Prevenção contra golpes: {scam_type.title()}**\n"
            f"{scamtype[scam_type]}"
        )
    else:
        await ctx.send(
            "Tipo de golpe não reconhecido.\n"
            "Escolha entre: Pix, WhatsApp, Jogos ou Lojas."
        )


@bot.command()
async def senha(ctx, pass_length: int):
    if pass_length < 8 or pass_length > 64:
        await ctx.send("Escolha um tamanho entre 8 e 64 caracteres.")
        return

    password = gen_pass(pass_length)

    await ctx.author.send(
        f"Sua senha gerada é: `{password}`"
    )

    await ctx.send("Enviei sua senha por mensagem privada.")


bot.run("seutokenaq")
