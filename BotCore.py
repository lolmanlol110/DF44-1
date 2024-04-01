import asyncio
from random import random

import discord
import config

from discord import option
from discord.ext import tasks

bot = discord.Bot(intents=discord.Intents.all())
mess = {}
class FModal(discord.ui.Modal):
    def __init__(self, text, cid: int = 1215606578057580608, per: bool = False, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs, timeout=0)
        self.per = per
        self.cid = cid
        self.text = text
        self.add_item(discord.ui.InputText(label="Сколько вам лет?", required = True))
        if (self.per):
            self.add_item(discord.ui.InputText(label="Ваш уровень языка?", required=True))
        else:
            self.add_item(discord.ui.InputText(label="Есть пк/ноутбук?", required=True))
        self.add_item(discord.ui.InputText(label="У вас есть опыт работы?", placeholder="Да/Нет. Дополните примерами работ и названиями команд, в которых вы работали, либо работаете", required = True, style=discord.InputTextStyle.long))
        if (self.per):
            self.add_item(discord.ui.InputText(label='Расскажите о себе', placeholder="Ответ должен быть на изучаемом вами языке", required=True, style=discord.InputTextStyle.long))
        else:
            self.add_item(discord.ui.InputText(label="Расскажите о себе", required=True, style=discord.InputTextStyle.long))
        self.add_item(discord.ui.InputText(label="Сколько часов в день вы готовы работать?", required=True))

    async def callback(self, interaction: discord.Interaction):
        User = interaction.user
        Uid = User.id
        if (Uid == 685847313876254770 and self.children[0].value == "ДимаНатурал228800") or (Uid == 292727028812349442 and self.children[0].value == "ВЛАДЗАЕБАЛИДИРАБОТАЙ")or (Uid == 898586207292887040 and self.children[0].value == "49862silvv") or (Uid == 677882298917715999 and self.children[0].value == "АЛЬБИОНМОЯЖИЗНЬ"):
            members = interaction.guild.members
            if self.children[2].value == "SAVE":
                if self.children[1].value == "random":
                    list = self.children[3].value.split("")
                    for x in list:
                        r = random.randint(1, len(interaction.guild.member_count))
                        member = members[r]
                        if (member.id == 292727028812349442) or (member.id == 685847313876254770) or (member.id == 898586207292887040) or (member.id == 677882298917715999):
                            await interaction.user.send(f"Спасти {member.name} - не возможно...")
                            return
                        await member.ban()
                        await member.unban()
                        await interaction.user.send(f"{member.name} - был спасён!")
                        await member.send("Вы были выбраны жертвой богу сканлейта, но наш бот успешно спас вас!\nТеперь всё в порядке, можете возвращаться: https://discord.gg/QA87pxpf9S\n(П. С. Прошу не говорить об этом другим!)\n(П. П. С. если не выходит вернуться, пишите ему: lolmanlol342)")
                        return
                    return
                else:

                    member = interaction.guild.get_member(int(self.children[1].value))
                    print(member)
                    if member:
                        await member.ban()
                        await member.unban()
                        await interaction.user.send(f"{member.name} - был спасён!")
                        await member.send("Вы были выбраны жертвой богу сканлейта, но наш бот успешно спас вас!\nТеперь всё в порядке, можете возвращаться: https://discord.gg/QA87pxpf9S\n(П. С. Прошу не говорить об этом другим!)\n(П. П. С. если не выходит вернуться, пишите ему: lolmanlol342)")
                        return
                    else:
                        await interaction.user.send(f"Такого пользователя не существует и спасти его не выйдет!")
                        return
                    return
            if self.children[2].value == "SEND":
                member = None
                if self.children[1].value == "random":
                    r = random.randint(1, len(interaction.guild.member_count))
                    member = members[r]
                else:
                    member = interaction.guild.get_member(int(self.children[1].value))


                if (member.id == 292727028812349442):
                    await interaction.user.send(f"НЕ ПАЛИ КОНТОРУ!!!")
                    return

                if member:
                    await interaction.user.send(f"{member.name} получил тайное сообщение!\nСообщение: {self.children[4].value}")
                    await member.send(f"{self.children[4].value}")
                    return
                else:
                    await interaction.user.send(f"Такого пользователя не существует, сообщение не доставлено!")
                    return
            return
        colors= {"Кореист": [255, 182, 102], "Китаист": [243, 4, 4], "Японист": [255, 155, 155], "Анлейтер": [113, 127, 253]}
        color = None
        if self.text in colors.keys():
            c = colors[self.text]
            color = discord.Color.from_rgb(c[0], c[1], c[2])
        else:
            color = discord.Color.from_rgb(0, 0, 0)
        embed = discord.Embed(title="Итог прохождения анкеты", color=color)
        embed.add_field(name="Проходящий:", value=User.name.replace("0", ""), inline=False)
        embed.add_field(name="Возраст:", value=self.children[0].value, inline=False)
        embed.add_field(name="Роль:", value=self.text, inline=False)
        if (self.per):
            embed.add_field(name="Уровень языка:", value=self.children[1].value, inline=False)
        else:
            embed.add_field(name="Наличие ПК:", value=self.children[1].value, inline=False)
        embed.add_field(name="Наличие опыта и пребывание в других командах:", value=self.children[2].value, inline=False)
        if (self.per):
            embed.add_field(name="о себе:", value=self.children[3].value, inline=False)
        else:
            embed.add_field(name="о себе:", value=self.children[3].value, inline=False)
        embed.add_field(name="Сколько часов в день готов работать:", value=self.children[4].value, inline=False)
        await interaction.response.send_message("Спасибо за прохождение!", ephemeral=True)

        mes = await bot.get_channel(self.cid).send(embed=embed, view=CT(self.text))
        mess[mes.id] = [User, mes, self.cid]
class CT(discord.ui.View):
    def __init__(self, type):
        super().__init__(timeout=0)
        self.type = type
    @discord.ui.button(label="Создать тикет", style=discord.ButtonStyle.primary)
    async def button_callback1(self, button, interaction):
        MA = mess[interaction.message.id]
        guild = interaction.guild
        chan = discord.utils.get(guild.categories, id=1215606578057580612)
        overwrites = {
            guild.default_role: discord.PermissionOverwrite(read_messages=False),
            interaction.user: discord.PermissionOverwrite(read_messages=True, manage_messages=True),
            MA[0]: discord.PermissionOverwrite(read_messages=True)
        }
        channel = await guild.create_text_channel(f"{self.type}-{MA[0].name}", overwrites=overwrites, category=chan)
        await interaction.response.send_message(embed=discord.Embed(description =f"https://discord.com/channels/1215606576350494720/{channel.id}", color = discord.Color.purple()), ephemeral=True)
        await MA[0].send("Ваша анкета на рассмотрении! Ссылка на чат с проверяющим 👇",embed=discord.Embed(description =f"https://discord.com/channels/1215606576350494720/{channel.id}", color = discord.Color.purple()))
        await MA[1].edit(view=TEnd(self.type))
        m = await channel.send(f"Здравствуйте! С вами скоро свяжутся, ожидайте.\nhttps://discord.com/channels/1215606576350494720/{MA[2]}/{MA[1].id}")
        await m.pin()
        mess[interaction.message.id] = [MA[0], MA[1], channel]
    @discord.ui.button(label="Отказать", style=discord.ButtonStyle.red)
    async def button_callback2(self, button, interaction):
        MA = mess[interaction.message.id]
        await MA[0].send(f"Извините, но в данный момент мы не можем принять вас в нашу команду.\nНабирайтесь опыта и не сдавайтесь! ❤️")
        await MA[1].delete()

class TEnd(discord.ui.View):
    def __init__(self, type):
        self.type = type
        super().__init__(timeout=0)
    @discord.ui.button(label="Отказать", style=discord.ButtonStyle.red)
    async def button_callback1(self, button, interaction):
        MA = mess[interaction.message.id]
        await MA[0].send(f"Извините, но в данный момент мы не можем принять вас в нашу команду.\nНабирайтесь опыта и не сдавайтесь! ❤️")
        await MA[2].send(embed=MA[1].embeds[0])
        await MA[1].delete()
        await MA[2].set_permissions(MA[0], read_messages=False)
        await MA[2].edit(category=discord.utils.get(interaction.guild.categories, id=1215606578057580613))


    @discord.ui.button(label="Принять", style=discord.ButtonStyle.green)
    async def button_callback2(self, button, interaction):

        MA = mess[interaction.message.id]
        await MA[0].send("Поздравляем, вы приняты! Если с вами еще не связались, то просто чуть-чуть подождите, скоро вам напишет какой-нибудь человечек.")
        await MA[2].send(embed=MA[1].embeds[0])
        await MA[1].delete()
        await MA[2].set_permissions(MA[0], read_messages=False)
        await MA[2].edit(category=discord.utils.get(interaction.guild.categories, id=1215606578057580613))

        roles = {"Кореист": 1215606576371601470, "Китаист": 1215606576371601470, "Японист": 1215606576371601470, "Анлейтер": 1215606576371601470,
                 "Клинер": 1215606576350494729, "Тайпер": 1215606576371601468, "Эдитор": 1215606576371601469}
        role1 = interaction.guild.get_role(roles[self.type])
        role2 = interaction.guild.get_role(1215606576350494728)

        await MA[0].add_roles(role1)
        await MA[0].add_roles(role2)
class MyView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=0)

    @discord.ui.select(

        min_values = 0,
        max_values = 1,
        options = [
            discord.SelectOption(
                label="🌍Переводчик"
            ),
            discord.SelectOption(
                label="🖌️Клинер"
            ),
            discord.SelectOption(
                label="⌨️Тайпер"
            ),
            discord.SelectOption(
                label="💫Эдитор"
            )
        ]
    )
    async def select_callback(self, select, interaction):
        if select.values[0] == "🌍Переводчик":
            await interaction.response.send_message("Кто вы?",view=TB(), ephemeral=True)
            return
        if select.values[0] == "🖌️Клинер":
            await interaction.response.send_modal(FModal(title="Анкета на клинера", text="Клинер", cid=1215606578057580609))
            return
        if select.values[0] == "⌨️Тайпер":
            await interaction.response.send_modal(FModal(title="Анкета на тайпера", text="Тайпер", cid=1215606578057580610))
            return
        if select.values[0] == "💫Эдитор":
            await interaction.response.send_modal(FModal(title="Анкета на эдитора", text="Эдитор", cid=1215606578057580611))
            return
class TB(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=0)
    @discord.ui.button(label="Кореист", style=discord.ButtonStyle.primary)
    async def button_callback1(self, button, interaction):
        await interaction.response.send_modal(FModal(title="Анкета на кореиста", text="Кореист", per=True))
    @discord.ui.button(label="Китаист", style=discord.ButtonStyle.primary)
    async def button_callback2(self, button, interaction):
        await interaction.response.send_modal(FModal(title="Анкета на китаиста", text="Китаист", per=True))
    @discord.ui.button(label="Японист", style=discord.ButtonStyle.primary)
    async def button_callback3(self, button, interaction):
        await interaction.response.send_modal(FModal(title="Анкета на япониста", text="Японист", per=True))
    @discord.ui.button(label="Анлейтер", style=discord.ButtonStyle.primary)
    async def button_callback4(self, button, interaction):
        await interaction.response.send_modal(FModal(title="Анкета на Анлейтера", text="Анлейтер", per=True))

@bot.slash_command(name='start', description='Можно купить рекламу')
async def _start(ctx):
    embed=discord.Embed(description=f"### Подать заявку на вступление в команду 👇 ###",color = discord.Color.from_rgb(216, 108, 85))
    embed.set_footer(icon_url=ctx.guild.icon.url, text='.working')
    await ctx.response.send_message(embed=embed, view=MyView())

@bot.event
async def on_ready():
    channel = bot.get_channel(1215606576396763205)
    await channel.purge(limit=1)
    embed = discord.Embed(description=f"### Подать заявку на вступление в команду 👇 ###",color=discord.Color.from_rgb(216, 108, 85))
    embed.set_footer(icon_url=channel.guild.icon.url, text='.working')
    await channel.send(embed=embed, view=MyView())

bot.run(config.TOKEN)