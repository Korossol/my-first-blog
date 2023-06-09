import json
import re

from . models import Youtube_video
#from .models import Youtube_video
#from zoukways.music import model






# Opening JSON file
f = open('zoukway.json')

# returns JSON object as
# a dictionary
data = json.load(f)
 
# Iterating through the json
# list
band=[]
ens=dict()
for link in data['UCyXE77e8qocz1L0JaAcHVYw']['video_data']:
    #print(link)
    title=data['UCyXE77e8qocz1L0JaAcHVYw']['video_data'][link]['title']

    
 #   if Youtube_video.objects.filter(yt_link=link).exists():
       # print(link,'is on the DB check to update the youtube title  :', title)
        #name_in_db=Youtube_video.objects.values(yt_link=link)
   # else :
      #  print('link:', link,' to be saved from video ', title )
      #  print('saved')

    

    #dictionary of link and video title
    ens[link]=title
    #print(title)
    #x = re.findall('^[A-Z]*[a-z]*',title)
    x = re.findall('^[A-Z]*',title)
    #print('XXXXXXXXXXXXXX RE RESULT : ', x)




    
    
    if len(x[0])>2:
        band.append(x)
#print('number of band is : ',len(band))
#print('BAND DICT ' ,band)
print(ens)

# Closing file
f.close()

