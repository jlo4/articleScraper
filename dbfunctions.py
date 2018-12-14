import MySQLdb
import datetime
from articlesDBCredentials import credentials

now = datetime.datetime.now()

conn = MySQLdb.connect("127.0.0.1", user=credentials['user'], passwd=credentials['password'], db=credentials['database'])

cursor = conn.cursor()

title = 'title1'
text = 'This is the text for first article.'
language = 'fi'
date = str(now.year) + '-' + str(now.month) + '-' + str(now.day)
words = "['words', 'from', 'article']"

def insertArticle(title, text, language, date='', words=''):
    '''
    Insert article into articles database
    '''
    cursor.execute("""INSERT INTO articles (title, text, language, date, words)
        VALUES(%s, %s, %s, %s, %s)""", (title, text, language, date, words))
    conn.commit()
    conn.close()

insertArticle(title, text, language, date=date, words=words)
