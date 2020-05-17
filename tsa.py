from textblob import TextBlob
import csv
import tweepy
from unidecode import unidecode
f =  open("auth.txt","r")
ak = f.readlines()
f.close

auth1 = tweepy.auth.OAuthHandler(ak[0].replace("\n",""),ak[1].replace("\n",""))
auth1.set_access_token(ak[2].replace("\n",""),ak[3].replace("\n",""))

api = tweepy.API(auth1)

target_num = 20
query = "Obama"

csvFile = open('results.csv','w')
csvWriter = csv.writer(csvFile)
csvWriter.writerow(["Username","Author ID", "Created", "Text", "Retwc","Hashtag","Followers ", "Friends", "Polarity", "Subjectivity"]) 
counter = 0

for tweet in tweepy.Cursor(api.search,q = query, lang = "en", result_type = "popular" , count = target_num).items():
    created = tweet.created_at
    text = tweet.text
    text = unidecode(text)
    retwc = tweet.retweet_count
    try:
        hashtag = tweet.entities[u'hashtag'][0][u'text']
    except:
        hashtag = "None"
    username = tweet.author.name
    authorid = tweet.author.id
    followers = tweet.author.followers_count
    friends = tweet.author.friends_count

    text_blob = TextBlob(text)
    polarity = text_blob.polarity
    subjectivity = text_blob.subjectivity
    csvWriter.writerow([username,authorid,created,text,retwc,hashtag,followers,friends,polarity,subjectivity])

    counter = counter + 1
    if(counter == target_num):
        break

csvFile.close()

