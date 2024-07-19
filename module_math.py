from pyrogram import Client, filters
from simpleeval import simple_eval
import uuid

with open("userbot.info", "r") as file:
    lines = file.readlines()
    prefix_userbot = lines[2].strip()

cinfo = f"🧮`{prefix_userbot}math`"
ccomand = " решает математические задачи"


def command_math(app):
    @app.on_message(filters.command("math", prefixes=prefix_userbot))
    def math_command(_, message):
        try:
            expression = message.text.split(maxsplit=1)[1]
            result = simple_eval(expression)
            message.reply_text(f"Результат: {result}")
        except IndexError:
            message.reply_text("Пожалуйста, введите математическое выражение после команды .math")
        except Exception as e:
            message.reply_text(f"Ошибка при вычислении выражения: {e}")


print("Модуль math загружен!")
