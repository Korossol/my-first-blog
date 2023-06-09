from videos.models import Youtube_video
#cmd on terminal=>python manage.py runscript delete_yt_video_table

def run():

    print('ready to delete')
    Youtube_video.objects.all().delete()
    print('all done, Youtube video table totally delete')
