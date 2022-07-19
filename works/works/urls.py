
from django.contrib import admin
from django.urls import path
from work import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home_page, name = "home"),
    path('upload/',views.upload, name = "upload"),
    path('books/',views.book_list, name = "book_list"),
    path('books/upload/',views.upload_book, name = "upload_book"),
    path('contact/',views.contact, name = "contact"),
    path('<slug:slug>/',views.article_detail, name="detail"),


]
if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)