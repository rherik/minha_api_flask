import tweepy
import configparser
import pandas as pd
from time import sleep

def api():
    config = configparser.ConfigParser()
    config.read('twikeys.ini')
    auth = tweepy.OAuthHandler(config['twitter']['api_key'], config['twitter']['api_key_secret'])
    auth.set_access_token(config['twitter']['access_token'], config['twitter']['access_token_secret'])
    return tweepy.API(auth)

def twita(api: tweepy.API, message: str, image_path=None):
    try:
        if image_path:
            api.update_status_with_media(message, image_path)
        else:
            api.update_status(message)
        print(f'Tweeted "{message}" successfully!')
    except Exception as e:
        print(f"Erro {e} ao postar tweet.")
        
def saves_user_tweets(api: tweepy.API, user, limit, termo=None):
    tweets = tweepy.Cursor(api.user_timeline, screen_name=user, count=100, tweet_mode='extended').items(limit)
    # tweets = api.user_timeline(screen_name=user, count=limit, tweet_mode='extended')
    columns = [' Data ', '  Tweet ']
    data = []
    if termo != None:
        for tweet in tweets:
            if termo in tweet.full_text or termo.capitalize() in tweet.full_text:
                data.append([tweet.created_at, tweet.full_text])
                # twita(api, f"@{user} tuitou sobre {termo}")

    else:
        for tweet in tweets:
            data.append([tweet.created_at, tweet.full_text])
    df = pd.DataFrame(data, columns=columns)
    return df
    
def get_hastags(api: tweepy.API, keyword, limit):
    tweets = tweepy.Cursor(api.search_tweets, q=keyword, count=100, tweet_mode='extended').items(limit)
    columns = [' User ', '   Tweet ']
    data = []
    for tweet in tweets:
        data.append([tweet.user.screen_name, tweet.full_text])
    df = pd.DataFrame(data, columns=columns)
    return df

def save_csv(dados):
    dados.to_csv('tweets.csv')
    
def show_tweets():
    with open('tweets.csv', 'r') as file:
        for n in file:
            print(n)

def delete_tweet(api, tweet_id, tweet_text):
    try:
        api.destroy_status(tweet_id)
        print("Deleted tweet: ", tweet_text)
    except:
        print("Could not delete tweet: ", tweet_text)

if __name__ == '__main__':
    texto_exemplo = ''
    api = api()
    # save_csv(get_user_tweets(api, 'saobrisinha', 10))
    user_tweets = tweepy.Cursor(api.user_timeline, screen_name='saobrisinha', count=100, tweet_mode='extended').items(10)
    for n in range(5):
        sleep(1)
        twita(api, f"{texto_exemplo} {n+1}º")

    sleep(10)
    for tweet in user_tweets:
        #print(tweet.full_text)
        if f"{texto_exemplo}" in tweet.full_text:
            sleep(1)
            delete_tweet(api, tweet_id=tweet.id, tweet_text=tweet.full_text)
        # else:
        #     print(f"Tweet {tweet.full_text}, de id{tweet.id} mantido.")
    # for n in range(5):
    #     twita(api, message=f'Tweet de teste {n+1}º')
