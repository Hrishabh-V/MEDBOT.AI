import requests
import time

print("Recommendation system starts...")

# List to store the previous news articles
previous_articles = []

def get_health_articles(api_key, keyword, bot, user_chat_id):
    global previous_articles

    url = "https://newsapi.org/v2/top-headlines"
    params = {
        "apiKey": api_key,
        "q": "health",
        "category": "health",
        "language": "en",
        "pageSize": 100
    }

    response = requests.get(url, params=params)
    data = response.json()

    if response.status_code == 200:
        articles = data.get("articles", [])
        new_articles_list = []
        # Replace "your_keyword" with your desired keyword
        for article in articles:
            title = article.get("title", "")
            link = article.get("url", "")
            if keyword.lower() in title.lower():
                new_articles_list.append({"title": title, "link": link})

        for article in new_articles_list:
            if article not in previous_articles:
                title = article["title"]
                link = article["link"]
                bot.send_message(user_chat_id, f"Title: {title}")
                bot.send_message(user_chat_id, f"Link: {link}")
                previous_articles.append(article)
                print(previous_articles)
                # Sleep for 2 minutes before sending the next article
                time.sleep(120)
    else:
        print("Error occurred while fetching articles.")

# Replace 'YOUR_API_KEY' with your actual News API key
def main():
    api_key = 'YOUR_API_KEY'
    keyword = 'health'  # Replace with your desired keyword
    bot = None  # Replace with your bot instance
    user_chat_id = 'USER_CHAT_ID'  # Replace with user's chat ID
    get_health_articles(api_key, keyword, bot, user_chat_id)

if __name__ == "__main__":
    main()
