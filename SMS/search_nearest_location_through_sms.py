import collections
import mysql.connector as mysql
import urllib.request
import urllib.parse
import json
import urllib.request
import urllib.parse
from bisect import bisect_left
from ret_pass import return_pass


def read_and_send(mess,number):

    resp, code = sendSMS('17dQ9VIqzsY-SaO7zL5u6LLm30oEhjNFLtsc4GssEa', number,
                         mess)
    print(resp)


# Function to search for a particular location in database
def bin_search(arr,left,right,val):
    while left<= right:
        mid = int((left+right)/2)
        if arr[mid]== val:
            return mid
        else:
            if arr[mid] > val:
                right = mid
            else:
                left = mid+1
    return left


# Function to get nearest jobs
def get_nearest_jobs(username,val,new_number):
    db = mysql.connect(
        host='localhost',
        user='root',
        passwd=return_pass(),
        database='aseproject',
    )
    cursor = db.cursor()
    table_name = 'user_details'
    query = "SELECT * FROM {}".format(table_name)
    cursor.execute(query)
    result = cursor.fetchall()
    items = [dict(zip([key[0] for key in cursor.description],row)) for row in result]
    present = False

    f = open('message.txt','r+')
    f.seek(0)
    f.truncate()

    for item in items:
        if item['Username']==username:
            number = item['mobile']
            present=True
            break
    if not present:
        print('You are not registered !!')
        f.write('You are not registered !!'+'\n')
    else:
        new_number = '91'+number
        query = "SELECT * FROM location_table"
        cursor.execute(query)
        result = cursor.fetchall()
        items = [dict(zip([key[0] for key in cursor.description],row)) for row in result]
        items = sorted(items,key= lambda x: x['location'])
        location_list = [item['location'] for item in items]
        left_index = bisect_left(location_list,val)
        if abs(val-location_list[left_index-1]) < abs(val-location_list[left_index]):
            left_index= left_index-1
        right_index = left_index
        while  right_index+1 < len(location_list) and location_list[right_index+1]==val:
            right_index = right_index+1
        if (right_index-left_index+1) % 2 ==0:
            middle_index = int((left_index+right_index)/2)+1
        else:
            middle_index = int((left_index+right_index)/2)
        lim = 2
        list_ranges = [x for x in range(middle_index-lim,middle_index+lim) if 0 <= x < len(location_list)]
        final_dict = [items[i] for i in list_ranges]
        out_str = 'Jobs available near location {}:'.format(val)
        print(out_str)
        f.write(out_str+'\n')
        for item in final_dict:
            item['time_of_completion']= item['time_of_completion'].strftime("%B %d, %Y")
            out_str = "Job Name: {}".format(item['job_name'])
            print(out_str)
            f.write(out_str+'\n')
            out_str = "Base Pay: {}".format(item['base_pay'])
            print(out_str)
            f.write(out_str+'\n')
            out_str = "Time of Completion: {}".format(item['time_of_completion'])
            print(out_str)
            f.write(out_str+'\n')
            out_str = "Location: {}".format(item['location'])
            print(out_str)
            f.write(out_str+'\n')
            print(' ')
        json_data = {
                'items': final_dict,
            }
        print(' ')

    f.close()
    f = open('message.txt','r')
    fin = f.read()
    print('*****')
    print(fin)
    f.close()
    read_and_send(fin,new_number)


# Function to retrieve messages from Inbox
def getMessages(apikey, inboxID):
    params = {'apikey': apikey, 'inbox_id': inboxID}
    f = urllib.request.urlopen('https://api.textlocal.in/get_messages/?'
                               + urllib.parse.urlencode(params))
    return (f.read(), f.code)


# Function to send SMS
def sendSMS(apikey, numbers,message,test=True):
    params = {'apikey': apikey, 'numbers': numbers, 'message': message,'test':test}
    f = urllib.request.urlopen('https://api.textlocal.in/send/?'
                               + urllib.parse.urlencode(params))
    return (f.read(), f.code)

# Code to filter jobs based on message sent by user
if __name__ == '__main__':
    resp, code = getMessages('17dQ9VIqzsY-SaO7zL5u6LLm30oEhjNFLtsc4GssEa', 10)
    mess = json.loads(resp)
    for each_message in mess['messages']:
        x = int(each_message['message'].split(',')[2])
        get_nearest_jobs(each_message['message'].split(',')[1],x,each_message['number'])

