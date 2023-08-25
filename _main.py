import tweepy
import configparser
import pandas as pd
from time import sleep
from datetime import datetime


class MeuTwitter:
    def __init__(self, api, user="saobrisinha"):
        self.api = api
        self.user = user

    def twite(self, message="Teste padrão", image_path=None):
        try:
            if image_path:
                self.api.update_status_with_media(message, image_path)
            else:
                self.api.update_status(message)
                print(f"~{message}~ twittado com sucesso!")
        except Exception as e:
            print(f"Erro {e} ao postar tweet.")

    def delete_tweet(self, num=1):
        try:
            tweets = self.api.user_timeline(count=num)
            for tweet in tweets:
                if tweet.text == self.message:
                    tweet_id = tweet.id_str   
                    print(tweet_id)             
                    self.api.destroy_status(tweet_id)
                    print(f"Tweet deletado: {tweet.text} - {tweet_id}")
                    break
        except Exception as e:
            print(f"Não foi possível deletar o tweet: ~{tweet.text}~ Erro: {e}")

    def tweets_terminal(self, home=False, num=10):
        if home == False: 
            user_tweets = self.api.user_timeline(screen_name=self.user, count=num, tweet_mode='extended')          
            #user_info = self.api.get_user(screen_name=self.user)
            #print(f"O total de tweets é: {len(user_tweets)}. Do usuário: {user_info.screen_name}, Followers: {user_info.followers_count}, \ndescrição: {user_info.description}\n")
            for tweet in user_tweets:
                sleep(5)
                tweet_id = tweet.id_str
                print("Tweet:", tweet.full_text,"\n", "Data:", tweet.created_at.date().strftime("%d/%m/%Y"), f"Id = {tweet_id}\n\n")
        else:
            home_user_tweets = self.api.home_timeline(count=num, tweet_mode='extended')   
            user_info = self.api.get_user(screen_name=self.user)
            print(f"O total de tweets é: {len(home_user_tweets)}. Que o usuário {user_info.screen_name} segue. Followers: {user_info.followers_count}, \ndescrição: {user_info.description}\n")
            for tweet in home_user_tweets:
                sleep(5)
                tweet_id = tweet.id_str
                print("User:", tweet.user.screen_name,"\n", "Tweet:", tweet.full_text,"\n", "Data:", tweet.created_at.date().strftime("%d/%m/%Y"), f"Id = {tweet_id}\n\n")

    # REFATORAR E TESTAR!!
    def twite_and_delete(self, delete=False, num=5):
        user_tweets = tweepy.Cursor(self.api.user_timeline, screen_name=self.user)          
        for n in range(num):
            sleep(1)
            # Sobreescrever self.message ou atribuir como parametro do metodo
            self.message = f"{self.message} {n+1}º"
            self.twite(self.message)

        if delete == True:
            sleep(10)
            for tweet in user_tweets:
                if self.message in tweet.full_text:
                    #reforçar medida de segurança. Implementar Try e Loop
                    certeza = input(
                        f"O tweet ~{tweet.full_text}~ será excluído. Tem certeza que deseja excluí-lo?(s/n)")
                    sleep(1)
                    #Laço for para ter certeza de cada tweet
                    if certeza == n or certeza == '':
                        print(f"{tweet.full_text} mantido na sua conta.")
                    else:
                        self.delete_tweet(api, tweet_id=tweet.id,
                                    tweet_text=tweet.full_text)
                        print(f"{tweet.full_text} excluido.")

    def get_for_topic(self, termo='Rio de Janeiro'):
        trend_topics = self.api.search_tweets(q=termo, count=10, tweet_mode='extended')
        for tweet in trend_topics:
            sleep(2)
            tweet_data = tweet.created_at.date().strftime("%d/%m/%Y")
            print("User:", tweet.user.screen_name,"\n", "Tweet:", tweet.full_text,"\n", "Data:", tweet_data, "\n\n")


    def get_trending_topics(self):
            woeid = 455825 #id Brasil
            print("As top trends na sua localização:")    
            trends = api.get_place_trends(id = woeid, exclude = 'hashtags')
            for value in trends:
                for trend in value['trends']:
                    sleep(1)
                    print(trend['name'], ", ","Tweet volume:", trend['tweet_volume'])

    # USO DO ARQUIVO CSV:
    # Dar ao nome do arquivo o nome do usuário
    def saves_user_tweets(self, limit, termo=None):
        tweets = tweepy.Cursor(self.api.user_timeline, screen_name=self.user,
                               count=100, tweet_mode='extended').items(limit)
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

    def _get_trending_topics(self, keyword):
        tweets = tweepy.Cursor(api.search_tweets, q=keyword, count=100, tweet_mode='extended')
        columns = [' User ', '   Tweet ']
        data = []
        for tweet in tweets:
            data.append([tweet.user.screen_name, tweet.full_text])
        df = pd.DataFrame(data, columns=columns)
        return df

    def save_csv(self, user, dados):
    # save_csv(get_user_tweets(api, 'saobrisinha', 10))
        dados.to_csv('tweets.csv')

    def show_tweets_in_file(self, user):
        with open('tweets.csv', 'r') as file:
            for n in file:
                print(n)


if __name__ == '__main__':
    def api():
        config = configparser.ConfigParser()
        config.read('h_twikeys.ini')
        auth = tweepy.OAuthHandler(config['twitter']['api_key'], config['twitter']['api_key_secret'])
        auth.set_access_token(config['twitter']['access_token'], config['twitter']['access_token_secret'])
        return tweepy.API(auth)
        
    api = api()
    herik = MeuTwitter(api=api)
    herik.tweets_terminal()
