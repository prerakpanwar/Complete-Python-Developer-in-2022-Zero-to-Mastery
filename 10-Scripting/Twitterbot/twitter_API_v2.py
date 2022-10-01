# pip install tweepy
import tweepy

# config.py : where I keep my keys as constants
import config


def about_me(client: tweepy.Client) -> None:
    """Print information about the client's user."""
    # The `public_metrics` addition will give me my followers count, among other things
    me = client.get_me(user_fields=["public_metrics"])
    print(f"My name: {me.data.name}")
    print(f"My handle: @{me.data.username}")
    print(f"My followers count: {me.data.public_metrics['followers_count']}")


def get_ztm_tweets(client: tweepy.Client) -> list[tweepy.Tweet]:
    """Return a list of latest ZTM tweets"""
    ztm = client.get_user(username="zerotomasteryio")
    response = client.get_users_tweets(ztm.data.id)
    return response.data


if __name__ == "__main__":
    client = tweepy.Client(
        bearer_token=config.BEARER_TOKEN,
        consumer_key=config.API_KEY,
        consumer_secret=config.API_SECRET,
        access_token=config.ACCESS_TOKEN,
        access_token_secret=config.ACCESS_SECRET,
    )
    print("=== About Me ===")
    about_me(client)
    print()
    print("=== ZTM Tweets ===")
    for tweet in get_ztm_tweets(client):
        print(tweet, end="\n\n")
