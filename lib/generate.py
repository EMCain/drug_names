# import whatever standard libraries
# import whatever internal packages
from src import tweet

# TODO: import your bot's text generating packages here
from .generate_advertisement import get_ad


def generate(account):
    return tweet.Tweet(
        text=get_ad(),  # replace this with a function call that generates your text
        account=account
    )
