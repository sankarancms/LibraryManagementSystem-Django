from django.conf.urls import url
from . import views


app_name = 'book'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<book_isbn>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<book_isbn>[0-9]+)/favorite/$', views.favorite, name='favorite'),
    url(r'^(?P<book_isbn>[0-9]+)/remove/$', views.unfav, name='unfav'),
    url(r'^book/add/$', views.BookCreate.as_view(), name= 'book-add'),
    url(r'^register/$', views.UserFormView.as_view(), name='register'),
    url(r'^login_user/$', views.login_user, name='login_user'),
    url(r'^logout_user/$', views.logout_user, name='logout_user'),



]