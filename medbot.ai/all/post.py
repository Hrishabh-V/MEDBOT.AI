url = f"https://www.amazon.in/s?k=product for {condition}"
link_text = 'Check out this website!'
message_text = f'<a href="{url}">{link_text}</a>'
bot.send_message(message.chat.id, text=message_text, parse_mode='HTML')