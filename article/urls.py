from django.conf.urls.static import static
from django.urls import path, include
from article import views
from django.views.decorators.csrf import csrf_exempt

# ARTICLE
urlpatterns = [
    path('', views.index),
    path('about', views.about),
    path('work', views.work),
    path('contact', views.contact),
    path('single/<int:pk>', views.single),
    path('message', views.message),
    # path('single/<int:pk>', views.single),
    path('fileUpload/', csrf_exempt(views.upload_file_view)),
    path('imageUpload/', csrf_exempt(views.upload_image_view)),
]
