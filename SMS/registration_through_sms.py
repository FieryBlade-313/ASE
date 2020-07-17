import mysql.connector as mysql
import urllib.request
import urllib.parse
import json


# Function to add Registrations received through SMS to Database
def add_to_database(message):
    db = mysql.connect(
        host='localhost',
        user='root',
        passwd='',
        database='aseproject',
    )
    print(db)
    cursor = db.cursor()
    sentence = message
    words = sentence.split(',')
    name = words[1]
    user_pass = words[2]
    user_age= words[3]
    print(name,user_pass,int(user_age))
    query = "INSERT INTO prac_table values (%s ,%s ,%s)"
    values = (name, user_pass, int(user_age))
    cursor.execute(query, values)
    db.commit()


# Function to get Messages stored in inbox
def getMessages(apikey, inboxID):
    params = {'apikey': apikey, 'inbox_id': inboxID}
    f = urllib.request.urlopen('https://api.textlocal.in/get_messages/?'
                               + urllib.parse.urlencode(params))
    return (f.read(),f.code)

# Code to get registration messages from inbox and store them in database
resp, code = getMessages('17dQ9VIqzsY-SaO7zL5u6LLm30oEhjNFLtsc4GssEa', 10)
mess = json.loads(resp)
print(mess)
for each_message in mess['messages']:
    add_to_database(each_message['message'])
