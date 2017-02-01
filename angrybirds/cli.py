import click
from .auth import login
from .stream import AngryBirdsStreamListener
import tweepy


@click.group()
@click.pass_context
def main(ctx):
    pass


@main.command()
@click.pass_context
def listen(ctx):
    auth = login()
    api = tweepy.API(auth)
    streamListener = AngryBirdsStreamListener()
    stream = tweepy.Stream(auth=api.auth, listener=streamListener)
    stream.filter(track=['python'])
