from django.conf.urls import url, re_path
from .views import get_posts, post_detail, create_or_edit_a_post

urlpatterns = [
    re_path(r'^$', get_posts, name='get_posts'),
    re_path(r'^(?P<pk>\d+)/$', post_detail, name='post_detail'),
    re_path(r'^new/$', create_or_edit_a_post, name="new_post"),
    re_path(r'^(?P<pk>\d+)/edit$', create_or_edit_a_post, name="edit_post")
]