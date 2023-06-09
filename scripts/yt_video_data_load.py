import json
import re
from videos.models import Youtube_video



def run():

    # Opening JSON file
    f = open('zoukway.json')

    # returns JSON object as
    # a dictionary
    data = json.load(f)
    
    # Iterating through the json
    # list
    count=0
    newrecord=0
    oldrecord=0
    for link in data['UCyXE77e8qocz1L0JaAcHVYw']['video_data']:
        #print(link)
        title=data['UCyXE77e8qocz1L0JaAcHVYw']['video_data'][link]['title']
        date=data['UCyXE77e8qocz1L0JaAcHVYw']['video_data'][link]['publishedAt']


        print('ready to save : ',title,'published : ',date)


        #check database to create or update
        vid, created = Youtube_video.objects.get_or_create(url=link,defaults={'name':title,'date_published':date})
        vid.save()
        print('saved')
        count+=1
        if created is True :
          newrecord+=1
        if created is False:
          oldrecord+=1
         

    print('total record :',count)
    print('newrecord : ', newrecord)
    print('oldrecord : ', oldrecord)
    

    # Closing file
    f.close()

