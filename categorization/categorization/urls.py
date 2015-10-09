from django.conf.urls import url

urlpatterns = [
    url(r'^cat.html$', 'imagematch.views.match_images', name='home')
]
