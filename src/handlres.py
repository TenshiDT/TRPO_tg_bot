def handle_text(update, context):
    user_id = update.message.from_user.id
    if 'waiting_for_city' in context.user_data and context.user_data['waiting_for_city']:
        city = update.message.text
        user_city[user_id] = city
        context.user_data['waiting_for_city'] = False
        update.message.reply_text(f"Город успешно установлен на {city.capitalize()}")
