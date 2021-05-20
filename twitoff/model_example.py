from flask_sqlalchemy import SQLAlchemy
import random
from flask_migrate import Migrate

DB = SQLAlchemy()
MIGRATE = Migrate()

# Creates a 'user' Table
class User(DB.Model):
    # id primary key column for 'User'
    id = DB.Column(DB.BigInteger, primary_key=True)
    # username column for 'User'
    username = DB.Column(DB.String, nullable=False)
    # most recent tweets
    newest_tweet = DB.Column(DB.BigInteger)

    def __repr__(self):
        return "<User: {}>".format(self.name)


# Creates a 'tweet' Table
class Tweet(DB.Model):
    # id primary key column for 'tweet'
    id = DB.Column(DB.BigInteger, primary_key=True)
    # text column for 'tweet'
    text = DB.Column(DB.Unicode(300))
    # user_id foreign key column for 'tweet'
    user_id = DB.Column(DB.BigInteger, DB.ForeignKey(
        'user.id'), nullable=False)
    # create database relationship between tables
    user = DB.relationship('User', backref=DB.backref('tweets', lazy=True))

    def __repr__(self):
        return "<Tweet: {}>".format(self.text)


def insert_example_user():
    # Do not run twice
    nick = User(id=1, name="Nick")
    james = User(id=2, name="NotJames")
    # Add users
    DB.session.add(nick)
    DB.session.add(james)
    DB.session.commit()

def insert_example_tweet(count=6):
    # Do not run twice
    tweets = []

    tweet_text = ["SHEEEEESH", "Lambda Rocks", "I love data science",
     "Lunch Time", "CRACKED", "Any Questions?"]

    while count > 0:
        id = count
        text = random.choice(tweet_text)
        user_id = random.randint(1, 2)

        tweet = Tweet(id=id, text=text, user_id=user_id)
        tweet.append(tweet)
        count -= 1

    DB.session.add_all(tweets)

    DB.session.commit()