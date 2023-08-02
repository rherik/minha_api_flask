import tweepy
import configparser
import pandas as pd
from time import sleep


class MeuTwitter:
    def __init__(self, api, user="saobrisinha", mensagem='Teste padrão'):
        self.api = api
        self.user = user
        self.message = mensagem

    def twita(self, image_path=None):
        try:
            if image_path:
                self.api.update_status_with_media(self.message, image_path)
            else:
                self.api.update_status(self.message)
                print(f"~{self.message}~ twittado com sucesso!")
        except Exception as e:
            print(f"Erro {e} ao postar tweet.")

    def delete_tweet(self):
        try:
            tweets = self.api.user_timeline()  # Obtém os últimos 20 tweets do usuário
            for tweet in tweets:
                if tweet.text == self.message:
                    tweet_id = tweet.id_str                
                    self.api.destroy_status(tweet_id)
                    print(f"Tweet deletado: {tweet.text}")
                    break
        except Exception as e:
            print(f"Não foi possível deletar o tweet: ~{tweet.text}~ Erro: {e}")

    def show_tt_terminal(self, home=False):
        if home == False: 
            user_tweets = self.api.user_timeline(screen_name=self.user, count=100, tweet_mode='extended')          
            print(f"O total de tweets é: {len(user_tweets)}")
            for tweet in user_tweets:
                sleep(5)
                print(tweet.full_text, tweet.created_at.date())
        else:
            home_user_tweets = self.api.home_timeline(count=1, tweet_mode='extended')   
            print(f"O total de tweets é: {len(home_user_tweets)}")
            for tweet in home_user_tweets:
                sleep(5)
                print(tweet.user.screen_name," - ", tweet.full_text, tweet.created_at.date())


    def twita_and_delete(self):
        user_tweets = tweepy.Cursor(self.api.user_timeline, self.screen_name, count=100, tweet_mode='extended')          
        for n in range(5):
            sleep(1)
            self.twita(api, f"{self.message} {n+1}º")

        sleep(10)
        for tweet in user_tweets:
            if self.message in tweet.full_text:
                #reforçar medida de segurança. Implementar Try e Loop
                certeza = input(
                    f"O tweet ~{tweet.full_text}~ será excluído. Tem certeza que deseja excluí-lo?(s/n)")
                sleep(1)
                if certeza == n or certeza == '':
                    print(f"{tweet.full_text} mantido na sua conta.")
                else:
                    self.delete_tweet(api, tweet_id=tweet.id,
                                 tweet_text=tweet.full_text)
                    print(f"{tweet.full_text} excluido.")

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

    def get_hastags(self, keyword, limit):
        tweets = tweepy.Cursor(api.search_tweets, q=keyword, count=100, tweet_mode='extended').items(limit)
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
        config.read('twikeys.ini')
        auth = tweepy.OAuthHandler(
            config['twitter']['api_key'], config['twitter']['api_key_secret'])
        auth.set_access_token(
            config['twitter']['access_token'], config['twitter']['access_token_secret'])
        return tweepy.API(auth)

    api_herik = api()
    herik = MeuTwitter(api_herik, "saobrisinha")
    herik.show_tt_terminal(home=True)
