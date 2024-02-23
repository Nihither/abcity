from django.shortcuts import render, HttpResponse, HttpResponseRedirect, loader, get_object_or_404
from .models import Video


def index(request):
    return HttpResponseRedirect(redirect_to='video/')


def video_content_list(request):
    video_content = Video.objects.all()
    content = {
        "content": video_content
    }
    return render(request, 'content/video_list.html', context=content)


def video_page(request, video_id):
    video = get_object_or_404(Video, pk=video_id)
    content = {
        "video": video
    }
    return render(request, 'content/video_page.html', context=content)
