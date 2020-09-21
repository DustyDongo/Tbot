class handler:


    def start(self, bot, context,):
        bot.message.reply_text("Hello User")


    def save_file(self, bot, context):
        file_name, text = context.args[0], " ".join(
            context.args[1:],
            )
        file = open(file_name, "w")
        res = file.write(text)
        bot.message.reply_text(str(res))
        file.close()


    def add_file(self, bot, context):
        file_name, text = context.args[0], " ".join(
            context.args[1:],
            )
        file = open(file_name, "a")
        res = file.write(text)
        bot.message.reply_text(str(res))
        file.close()


    def read_file(self, bot, context):
        file_name = context.args[0]
        with open(file_name, "r") as file:
            bot.message.reply_text(file.read())



    def message(self, bot, context):
        text = bot.message.text 
        count = len(text)
        bot.message.reply_text(str(count))