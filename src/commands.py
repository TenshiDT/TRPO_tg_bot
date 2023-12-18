def start(update, context):
    update.message.reply_text("Привет! Я бот для отслеживания погоды. Чтобы начать, введите /set_city")

def set_city(update, context):
    update.message.reply_text("Введите название города:")
    context.user_data['waiting_for_city'] = True

def today(update, context):
    user_id = update.message.from_user.id
    city = user_city.get(user_id)
    if not city:
        update.message.reply_text("Вы не выбрали город. Введите /set_city чтобы выбрать город.")
        return
    update.message.reply_text(get_weather(city, 'today'))

def tomorrow(update, context):
    user_id = update.message.from_user.id
    city = user_city.get(user_id)
    if not city:
        update.message.reply_text("Вы не выбрали город. Введите /set_city чтобы выбрать город.")
        return
    update.message.reply_text(get_weather(city, 'tomorrow'))

def week(update, context):
    user_id = update.message.from_user.id
    city = user_city.get(user_id)
    if not city:
        update.message.reply_text("Вы не выбрали город. Введите /set_city чтобы выбрать город.")
        return
    update.message.reply_text(get_weather(city, 'week'))

def month(update, context):
    user_id = update.message.from_user.id
    city = user_city.get(user_id)
    if not city:
        update.message.reply_text("Вы не выбрали город. Введите /set_city чтобы выбрать город.")
        return
    update.message.reply_text(get_weather(city, 'month'))

def change_city(update, context):
    update.message.reply_text("Введите новое название города:")
    context.user_data['waiting_for_city'] = True

def notification(update, context):
    user_id = update.message.from_user.id
    city = user_city.get(user_id)
    if not city:
        update.message.reply_text("Вы не выбрали город. Введите /set_city чтобы выбрать город.")
        return
    forecast = get_weather(city, 'tomorrow')
    update.message.reply_text(f"Оповещение установлено!\n{forecast}")
