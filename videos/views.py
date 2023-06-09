from django.shortcuts import render
from .models import Youtube_video
from django.db.models import Q
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView



#from recup.owner import OwnerListView, OwnerDetailView, OwnerCreateView, OwnerUpdateView, OwnerDeleteView



class Youtube_videoListView(ListView):
    model = Youtube_video
    #queryset = Deces.objects.order_by('-created')
    paginate_by = 25
    def get_context_data(self,**kwargs):
        context = super().get_context_data( **kwargs)
        #context['total_records'] = self.queryset.count()
        all_records = Youtube_video.objects.all()
        total_records=all_records.count()
        context['total_records'] = total_records


        # add a searchbar
        strval = self.request.GET.get("search", False)
        if strval:

            query = Q(titre_deces__icontains=strval)
            query.add(Q(detail_deces__icontains=strval), Q.OR)
            youtube_video_list = Youtube_video.objects.filter(query).select_related().order_by('-updated')[:100]
            context['youtube_video_list']=youtube_video_list
        #else:
            #deces_list = Deces.objects.all().order_by('-updated')
            #context['deces_list'] = deces_list
        context['search']=strval









        return context

class Youtube_videoDetailView(DetailView):
    model = Youtube_video