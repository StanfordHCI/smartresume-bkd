#import requests
import calendar
import time
import string
from random import *

NUM_SAMPLES = 1
BASE_URL = 'http://srbkd-env.us-west-2.elasticbeanstalk.com/'

worker_opts = {'1': 'Ali Alkhatib', '2': 'Junwon Park', '3': 'Katharina Lix', '4': 'Jan Peters', '5': 'Melissa Valentine', '6': 'Niloufar Salehi', '7': 'Spam Girl', '8': 'Shirish Goyal', '9': 'Ranjay Krishna', '10': 'Sherry Ruan'} # {'worker_id': 'worker_name'}

requester_opts = {'A2XJMS2J2FMVXK': 'Ali Alkhatib', 'A2XJMS2J2FMVX1': 'Govinda Dasu', 'A2XJMS2J2FMVX2':'Michael Bernstein', 'A2XJMS2J2FMVX3': 'University of California', 'A2XJMS2J2FMVX4': 'Stanford University', 'A2XJMS2J2FMVX5': 'Cornell University', 'A2XJMS2J2FMVX6': 'Bloomberg Inc.', 'A2XJMS2J2FMVX7': 'Exxon Inc.', 'A2XJMS2J2FMVX8': 'Microsoft Inc.'} # {'requester_id': 'requester_name'}

# make hit_id string verson of model id for generated samples 

category_opts = ['Sentiment', 'Survey', 'Image Tag', 'Transcription', 'Classification']

# reward should be random number between $0.00 and $1.00

status_opts = ['Approved - Pending Payment', 'Approved - Paid', 'Rejected', 'Pending Approval']

feedback_opts = ['good', 'bad', 'very good']

for s in NUM_SAMPLES:
    worker_id = random.choice(worker_opts.keys())
    worker_name = worker_opts[worker_id]
    requester_id = random.choice(requester_opts.keys())
    requester_name = requester_opts[requester_id]
    hit_id = str(int(time.time()*1000000)) + ''.join(choice(string.ascii_uppercase + string.digits) for _ in range(14)) # should be unique -- neg prob of being same
    category_opts = random.choice(category_opts)
    reward = "${:.2f}".format(round(random.random(), 2))
    status = random.choice(status_opts)
    feedback = random.choice(feedback_opts)
    '''
    r = requests.post(BASE_URL + 'task/', data={
        'number': 12524, 
        'type': 'issue', 
        'action': 'show'
    })
    '''
