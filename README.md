# TweetSentimentAnalysis
Tweet Sentiment Analysis using text blob, tweepy, Matplot
Sentiment Analysis also called opinion mining or emotion AI, is the process of determining whether a piece of writing is positive, negative or neutral
It’s applied for reviews and social media for a variety of applications. We are using the Twitter API tweepy and approach is based on the lexicon. The work here for tweepy is to perform actions like create and search along with various keys(authentication keys provided for accessing tweets).I will not waste your time and jump right in.

Getting modules! Install tweepy and textblob depending on the python version you use. Register for the twitter API and get the keys we get a set of 4 keys in total being consumer key, consumer token , access key, and access token secret all of these four keys could be saved in a single file and read from the file or simply store these variables in the script. Authenticate and get into the mainframe *hackerman* Okay I am Joking, use the OAuthhandler from tweepy it is used to authenticate and set all the other variables such as access token, access token secret.

Tokenization time(Textblob) this is where text blob enters it tokenizes each word from the string given to it and evaluates each of those words(a named tuple of words) based in polarity(a float value [-1.0,1.0]) and subjectivity(a float value [0.0,1.0].Polarity could be defined as the tone and subjectivity as relevance.

Actual code it’s creating .csv files then retrieving the tweets with search function from tweepy and just segregating the tweet content into the creator, a number of retweets, username, text, followers, and so on.
Thanks for reading !

The Reason I didn’t use images or show how my actual project looks like is because my Twitter access has been revoked and for some reason my email id is insufficient.

Tweet Sentiment Analysis with Tweepy , TextBlob and Matplot
I share two versions of my tweet sentiment analysis
One Version uses tkinter to make a gui based final product and 
Other creates a .csv file showing the other parameters such as time,date, tweet and has a polarity and a subjectivity column too.
How to get started make a twitter developer account and request for tokens
this is an excellent guide for getting the keys and also create twitter bots
-https://realpython.com/twitter-bot-python-tweepy/  (credits to owner)

install all the modules 
pip install tweepy,tkinter,matplotlib
