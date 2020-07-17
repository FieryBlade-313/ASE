import collections
import mysql.connector as mysql
import urllib.request
import urllib.parse
import json
import datetime
from bisect import bisect_left


# Function to search for a particular location in database
def bin_search(arr,left,right,val):
    while left<=right:
        mid = int((left+right)/2)
        if arr[mid]==val:
            return mid
        else:
            if arr[mid] > val:
                right = mid
            else:
                left = mid+1
    return left


# Function to get nearest jobs
def get_nearest_jobs(val):
    db = mysql.connect(
        host='localhost',
        user='root',
        passwd='',
        database='aseproject',
    )
    cursor = db.cursor()
    table_name = 'jobs_available'
    query = "SELECT * FROM jobs_available"
    cursor.execute(query)
    result = cursor.fetchall()
    items = [dict(zip([key[0] for key in cursor.description],row)) for row in result]
    items = sorted(items,key= lambda x: x['location'])
    print(' ')
    location_list = [item['location'] for item in items]
    print(' ')
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
    print('Jobs available near location {}:'.format(val))
    for item in final_dict:
        item['time_of_completion']= item['time_of_completion'].strftime("%B %d, %Y")
        print("Job Name: {}".format(item['job_name']))
        print("Base Pay: {}".format(item['base_pay']))
        print("Time of Completion: {}".format(item['time_of_completion']))
        print("Location: {}".format(item['location']))
        print(' ')
    json_data = {
            'items': final_dict,
        }
    print(' ')
    # print(json_data)
    json_data = json.dumps(json_data)
    # print(json_data)
    return json_data


# Function to retrieve messages from Inbox
def getMessages(apikey, inboxID):
    params = {'apikey': apikey, 'inbox_id': inboxID}
    f = urllib.request.urlopen('https://api.textlocal.in/get_messages/?'
                               + urllib.parse.urlencode(params))
    return (f.read(), f.code)


# Code to filter jobs based on message sent by user
resp, code = getMessages('17dQ9VIqzsY-SaO7zL5u6LLm30oEhjNFLtsc4GssEa', 10)
mess = json.loads(resp)
for each_message in mess['messages']:
    x = int(each_message['message'].split(',')[1])
    get_nearest_jobs(x)



