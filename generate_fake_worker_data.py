import requests

NUM_SAMPLES = 1

worker_opts = {'1': 'Ali Alkhatib', '2': 'Junwon Park', '3': 'Katharina Lix', '4': 'Jan Peters', '5': 'Melissa Valentine', '6': 'Niloufar Salehi', '7': 'Spam Girl', '8': 'Shirish Goyal', '9': 'Ranjay Krishna', '10': 'Sherry Ruan'} # {'worker_id': 'worker_name'}

requester_opts = {'A2XJMS2J2FMVXK': 'Ali Alkhatib', 'A2XJMS2J2FMVX1': 'Govinda Dasu', 'A2XJMS2J2FMVX2':'Michael Bernstein', 'A2XJMS2J2FMVX3': 'University of California', 'A2XJMS2J2FMVX4': 'Stanford University', 'A2XJMS2J2FMVX5': 'Cornell University', 'A2XJMS2J2FMVX6': 'Bloomberg Inc.', 'A2XJMS2J2FMVX7': 'Exxon Inc.', 'A2XJMS2J2FMVX8': 'Microsoft Inc.'} # {'requester_id': 'requester_name'}

# make hit_id string verson of model id for generated samples 

category_opts = ['Sentiment', 'Survey', 'Image Tag', 'Transcription', 'Classification']

# reward should be random number between $0.00 and $1.00

status_opts = ['Approved - Pending Payment', 'Approved - Paid', 'Rejected', 'Pending Approval']

feedback = ['good', 'bad', 'very good']

for s in NUM_SAMPLES:
