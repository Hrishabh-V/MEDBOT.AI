
import telebot
import mysql.connector

def share_location(chat_id):
    
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="pythondatas"
    )
    # Initialize the Telegram bot
    TOK = ''
    bot = telebot.TeleBot(TOK)
    
    
    cursor = db.cursor()
    sql = "SELECT * FROM user_location WHERE chat_id = %s"
    val = (chat_id,)
    cursor.execute(sql, val)
    result = cursor.fetchone()
    
    if result is None:
            # If the user is not in the database, ask them to share their location
            markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
            button = telebot.types.KeyboardButton('Share Location', request_location=True)
            markup.add(button)
            bot.send_message(chat_id, "Please share your location", reply_markup=markup)
            

    else:
                            # If the user is already in the database, send a message thanking them for sharing their location
                markup = telebot.types.ReplyKeyboardRemove()
                bot.send_message(chat_id, "If you want to share your location again, use the /start command.", reply_markup=markup)


    @bot.message_handler(func=lambda message: message.content_type == 'location')
    def handle_location(message):
                # Get the user's chat ID and location
                chat_id = message.chat.id
                lat = message.location.latitude
                lon = message.location.longitude
                
                # Check if the user's chat ID is already in the database
                cursor = db.cursor()
                sql = "SELECT * FROM user_location WHERE chat_id = %s"
                val = (chat_id,)
                cursor.execute(sql, val)
                result = cursor.fetchone()

                if result is None:
                    # If the user is not in the database, store their location and send a message thanking them for sharing their location
                    cursor = db.cursor()
                    sql = "INSERT INTO user_location (chat_id, latitude, longitude) VALUES (%s, %s, %s)"
                    val = (chat_id, lat, lon)
                    cursor.execute(sql, val)
                    db.commit()
                    bot.send_message(chat_id, f"Thank you for sharing your location! This will help us provide personalized recommendations for you based on your current location.")
                else:
                    # If the user is already in the database, update their location and send a message thanking them for sharing their updated location
                    cursor = db.cursor()
                    sql = "UPDATE user_location SET latitude = %s, longitude = %s WHERE chat_id = %s"
                    val = (lat, lon, chat_id)
                    cursor.execute(sql, val)
                    db.commit()
                    bot.send_message(chat_id, f"Thank you for sharing your updated location! This will help us provide personalized recommendations for you based on your current location.")

                # Remove the location request button
                markup = telebot.types.ReplyKeyboardRemove()
                bot.send_message(chat_id, "If you want to share your location again, use the /start command.", reply_markup=markup)
                db.close()           