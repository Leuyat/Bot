import requests
import time

NEWS_API_KEY = 'ebe98bff01b347339e2f1bb2479d35ad'
TELEGRAM_TOKEN = '7390183888:AAEVOVS0M7usiyr0NG53F3lWr5CuMGdwnyI'
TELEGRAM_CHAT_ID = '1282339794'

def get_crypto_news(asset):
    url = f'https://newsapi.org/v2/everything?q={asset}&apiKey={NEWS_API_KEY}'
    response = requests.get(url)
    news_data = response.json()
    
    # Solo enviamos la primera noticia
    if news_data['articles']:
        first_article = news_data['articles'][0]
        title = first_article['title']
        description = first_article['description']
        url = first_article['url']
        
        message = f"📰 Noticia destacada sobre {asset}: \n\n{title}\n\n{description}\n\nLeer más: {url}"
        send_telegram_message(message)
    else:
        send_telegram_message(f"No se encontraron noticias recientes sobre {asset}.")

def send_telegram_message(message):
    url = f'https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage'
    payload = {'chat_id': TELEGRAM_CHAT_ID, 'text': message}
    requests.post(url, json=payload)

if __name__ == '__main__':
    asset = 'bitcoin'  # Cambia el activo según el que te interese
    while True:
        get_crypto_news(asset)
        time.sleep(3600)  # Busca noticias cada hora
