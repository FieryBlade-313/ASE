import mysql.connector as mysql
import urllib.request
import urllib.parse
import json
from ret_pass import return_pass


def read_and_send(mess,number):

    resp, code = sendSMS('17dQ9VIqzsY-SaO7zL5u6LLm30oEhjNFLtsc4GssEa', number,
                         mess)
    print(resp)


# Function to register
def add_to_database(message,number):
    db = mysql.connect(
        host='localhost',
        user='root',
        passwd=return_pass(),
        database='aseproject',
    )
    print(db)
    cursor = db.cursor()
    table_name = 'user_details'
    query = "SELECT * FROM {}".format(table_name)
    cursor.execute(query)
    result = cursor.fetchall()
    items = [dict(zip([key[0] for key in cursor.description],row)) for row in result]
    sentence = message
    words = sentence.split(',')
    name = words[1]
    username = words[2]
    password= words[3]
    email= words[4]
    mobile= str(number)[2:]

    f = open('message.txt','r+')
    f.seek(0)
    f.truncate()

    present = False
    for item in items:
        if item['Username']==username:
            present=True
            break
    if present:
        print('User already exists')
        f.write('User already exists'+'\n')
    else:
        query = "INSERT INTO {}( Name,Username,Password,Email,mobile) values (%s ,%s ,%s,%s,%s)".format(table_name)
        values = (name, username,password,email,mobile)
        try:
            cursor.execute(query, values)
            db.commit()
        except Exception as e:
            print(e)
            f.write(str(e)+'\n')
        print("Succesfully registered\nName : {}\nUsername : {}\nEmail : {}\nMobile : {}".format(name, username, email,
                                                                                                 mobile))
        f.write("Succesfully registered\nName : {}\nUsername : {}\nEmail : {}\nMobile : {}".format(name, username, email,
                                                                                                 mobile))

    f.close()
    f = open('message.txt','r')
    fin = f.read()
    print('*****')
    print(fin)
    f.close()
    read_and_send(fin,number)



def sendSMS(apikey, numbers,message,test=True):
    params = {'apikey': apikey, 'numbers': numbers, 'message': message,'test':test}
    f = urllib.request.urlopen('https://api.textlocal.in/send/?'
                               + urllib.parse.urlencode(params))
    return (f.read(), f.code)

# Function to get Messages stored in inbox
def getMessages(apikey, inboxID):
    params = {'apikey': apikey, 'inbox_id': inboxID}
    f = urllib.request.urlopen('https://api.textlocal.in/get_messages/?'
                               + urllib.parse.urlencode(params))
    return (f.read(),f.code)

# Code to get registration messages from inbox and store them in database
if __name__ == '__main__':
    resp, code = getMessages('17dQ9VIqzsY-SaO7zL5u6LLm30oEhjNFLtsc4GssEa', 10)
    mess = json.loads(resp)
    print(mess)
    for each_message in mess['messages']:
        add_to_database(each_message['message'],each_message['number'])
