from tweepy import OAuthHandler, API


class Account:
    def __init__(self, **kwargs):
        for item in ['CONSUMER_KEY', 'CONSUMER_SECRET', 'ACCESS_KEY', 'ACCESS_SECRET']:
            self.__setattr__(item, kwargs[item])

    def authenticate(self):
        auth = OAuthHandler(self.CONSUMER_KEY, self.CONSUMER_SECRET)
        auth.set_access_token(self.ACCESS_KEY, self.ACCESS_SECRET)
        return API(auth)


class Tweet:
    def __init__(self, account, text=None):
        self.account = account
        self.api = self.account.authenticate()
        self.text = text

    def send(self):
        self.api.update_status(self.text)

# TODO implement: classes Reply, Retweet, Quote (extending Tweet)
