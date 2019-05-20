import praw
import re
import datetime
import time
import gui
from gui import *
from configparser import ConfigParser

def writeList(post_list, file, genre):
    file.write("----------------\n" + genre + "\n----------------\n")
    for item in post_list:
        file.write(item + '\n')

config = ConfigParser()
config.read('G:/RedditScraper/Logs/UserInfo.ini')
c_id = config.get('main_info', 'client_id')
c_secret = config.get('main_info', 'client_secret')
pword = config.get('main_info', 'password')
u_agent = config.get('main_info', 'user_agent')
u_name = config.get('main_info', 'username')
graphics = gui.GUI()
graphics.loadGUI()

reddit = praw.Reddit(client_id = c_id,
                     client_secret = c_secret,
                     password = pword,
                     user_agent = u_agent,
                     username = u_name)
reddit.read_only
listAllGenres = ["Black", "Death", "Thrash", "Traditional", "Underground", "Doom", "Sludge"
                 'Tech', 'Punk', "Blackened Death", "Power", "Speed", "Melodeath", ""]
listBlack = []
listDeath = []
listThrash = []
listTrad = []
listPower = []

regexSingleGenre = re.compile(r"\[\S+]")
today = datetime.date.today()
tomorrow = datetime.date.today() + datetime.timedelta(days=1)
currentDay = today.day
nextDay = tomorrow.day
logFile = open("Logs\\ContinuousLog.txt", 'a')
logFile.close()
logFile = open("Logs\\ContinuousLog.txt", "r")
outputPath = "Logs\\Tracked Songs " + str(datetime.datetime.now().month) + '-' + str(datetime.datetime.now().day) + ".txt"
outputFile = open(outputPath, "a")
outputFile.close()
listAllValidSubmissions = logFile.read().splitlines()
logFile.close()
while True:
    while currentDay is not nextDay:
        for submission in reddit.subreddit('metal').new(limit=20):
            flairContents = submission.link_flair_text
            if flairContents is None:
                flairContents = 'No Flair'
            genres = flairContents.replace('[','').replace(']', '').split('/')
            for postGenre in genres:
                postGenre = postGenre.replace('[', '').replace(']', '')
                for listGenre in listAllGenres:
                    if postGenre == listGenre:
                        if submission not in listAllValidSubmissions:
                            if postGenre == "Black":
                                listBlack.append(submission.title)
                            elif postGenre == "Death":
                                listDeath.append(submission.title)
                            elif postGenre == "Thrash":
                                listThrash.append(submission.title)
                            elif postGenre == "Traditional":
                                listTrad.append(submission.title)
                            print(submission.title)
                            logFile = open("Logs\\ContinuousLog.txt", "a")
                            
                            listAllValidSubmissions.append(submission)
                            logFile.write(submission.title + '\n')
                            logFile.close()
            time.sleep(2)
        for submission in reddit.subreddit('BlackMetal').new(limit = 20):
            if submission.score > 20:
                if '-' in submission.title:
                    if submission not in listAllValidSubmissions:
                        print(submission.title + '\n')
                        logFile = open("Logs\\ContinuousLog.txt", "a")
                        listAllValidSubmissions.append(submission)
                        logFile.write(submission.title + '\n')
                        logFile.close()
            time.sleep(2)
        for submission in reddit.subreddit('Deathmetal').new(limit = 20):
            if submission.score > 15:
                if '-' in submission.title:
                    if submission not in listAllValidSubmissions:
                        print(submission.title + '\n')
                        logFile = open("Logs\\ContinuousLog.txt", "a")
                        
                        listAllValidSubmissions.append(submission)
                        logFile.write(submission.title + '\n')
                        logFile.close()
            time.sleep(2)
        #logFile.close()
        time.sleep(120)

    for item in listAllValidSubmissions:
        genre = submission.link_flair_text.replace('[', '').replace(']', '').split('/')
        if genre == "Black":
            listBlack.append(item)
        if genre == "Death":
            listDeath.append(item)

    writeList(listBlack, outputFile, "Black Metal")
    writeList(listBlack, outputFile, "Death Metal")
    currentDay = nextDay
    nextDay = datetime.date.today() + datetime.timedelta(days=1)
    listAllValidSubmissions.clear()
    listDeath.clear()
    listBlack.clear()
    outputFile = open("Logs\\Tracked Songs: " + str(datetime.datetime.now().day) + ".txt", "a")






