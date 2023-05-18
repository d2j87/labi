from flask import Flask, render_template, request
from threading import Thread
import telebot
import mimetypes
# Ініціалізуємо Flask-додаток
app = Flask(__name__)
bot = telebot.TeleBot("6097111364:AAG-GqbNz7yU_14OPy1gZO5rRLHoLbVztC0")

# Ручки Flask-додатку
@app.route('/')
def home():
    return render_template('home.html')


@app.route('/send_order', methods=['POST'])
def send_order():
    # Отримуємо значення полів з даних
    pib = request.form.get('pib')
    subject = request.form.get('subject')
    university = request.form.get('university')
    course = request.form.get('course')
    contacts = request.form.get('contacts')
    task = request.form.get('task')
    attachment = request.files.get('attachment')
    deadline = request.form.get('deadline')

        # Визначення типу MIME файлу
    mime_type = attachment.mimetype
    
    # Визначення розширення на основі типу MIME
    file_extension = mimetypes.guess_extension(mime_type)
    # Формуємо текст повідомлення
    message_text = f"Деталі замовлення:\n" \
                   f"ПІБ: {pib}\n" \
                   f"Предмет: {subject}\n" \
                   f"Університет: {university}\n" \
                   f"Курс: {course}\n" \
                   f"Контакт: {contacts}\n" \
                   f"Завдання: {task}\n" \
                   f"Дедлайн: {deadline}\n" \

    # Відправляємо повідомлення в Telegram-канал
    bot.send_message('1469146538', message_text)
    bot.send_document('1469146538', attachment, caption=file_extension)
    return "Message sent successfully!"

# Запускаємо сервер Flask
def run_flask():
    app.run(debug=True, host='0.0.0.0', port='5000')

# Запускаємо Telegram-бота
def run_telebot():
    bot.polling()


# Запускаємо обидва компоненти (Flask і Telegram-бот) одночасно
if __name__ == '__main__':
    # Опціонально: ініціалізуємо Telegram-бота

    # Створюємо окремі потоки для Flask-сервера та Telegram-бота
    flask_thread = Thread(target=run_flask)
    telebot_thread = Thread(target=run_telebot)

    # Запускаємо обидва потоки
    flask_thread.start()
    telebot_thread.start()

    # Чекаємо завершення потоків
    flask_thread.join()
    telebot_thread.join()
