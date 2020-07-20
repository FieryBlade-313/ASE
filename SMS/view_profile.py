import mysql.connector as mysql
import urllib.request
import urllib.parse
import json
from ret_pass import return_pass

def read_and_send(mess,number):

    resp, code = sendSMS('17dQ9VIqzsY-SaO7zL5u6LLm30oEhjNFLtsc4GssEa', number,
                         mess)
    print(resp)


# Function to View Profile
def view_profile(message,number):
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
    f = open('message.txt','r+')
    f.seek(0)
    f.truncate()

    sentence = message
    words = sentence.split(',')
    username = words[1]
    present = False
    for item in items:
        if item['Username'] == username:
            present=True
            name = item['Name']
            email= item['Email']
            mobile= item['mobile']
            break
    if not present:
        out_str = 'You are not registered !!' 
        print(out_str)
        f.write(out_str+'\n')
        
    elif mobile!=str(number)[2:]:
        out_str = 'Please Send a message from your Registered Mobile Number '
        print(out_str)
        f.write(out_str+'\n')
        
    else:
        out_str = 'Your profile\n'
        print(out_str)
        f.write(out_str)
        out_str = 'Name : {}\n'.format(name)
        print(out_str)
        f.write(out_str)
        out_str = 'Username : {}\n'.format(username)
        print(out_str)
        f.write(out_str)
        out_str = 'Email ID : {}\n'.format(email)
        print(out_str)
        f.write(out_str)
        out_str = 'Mobile No : {}\n'.format(mobile)
        print(out_str)
        f.write(out_str)

    f.close()
    f = open('message.txt','r')
    fin = f.read()
    print('*****')
    print(fin)
    f.close()
    read_and_send(fin,str(number))


# Function to get Messages stored in inbox
def getMessages(apikey, inboxID):
    params = {'apikey': apikey, 'inbox_id': inboxID}
    f = urllib.request.urlopen('https://api.textlocal.in/get_messages/?'
                               + urllib.parse.urlencode(params))
    return (f.read(),f.code)


# Function to Send messages to User
def sendSMS(apikey, numbers,message,test=True):
    params = {'apikey': apikey, 'numbers': numbers, 'message': message,'test':test}
    f = urllib.request.urlopen('https://api.textlocal.in/send/?'
                               + urllib.parse.urlencode(params))
    return (f.read(), f.code)


if __name__ == '__main__':
    resp, code = getMessages('17dQ9VIqzsY-SaO7zL5u6LLm30oEhjNFLtsc4GssEa', 10)
    mess = json.loads(resp)
    print(mess)
    for each_message in mess['messages']:
        view_profile(each_message['message'],each_message['number'])
