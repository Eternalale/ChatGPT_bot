import telebot
import openai
from config import TOKEN, openAI_API

TOKEN = TOKEN

Bot = telebot.TeleBot(TOKEN)


openai.api_key = openAI_API

@Bot.message_handler(func=lambda _: True)
def start_function(message):

    response = openai.Completion.create(
  model="text-davinci-003",
  prompt=message.text,
  temperature=0.5,
  max_tokens=60,
  top_p=1.0,
  frequency_penalty=0.5,
  presence_penalty=0.0,
  stop=["You:"]
)

    Bot.send_message(text=response['choices'][0]['text'], chat_id=message.from_user.id)

if __name__ == '__main__':
    Bot.polling()


