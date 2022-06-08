from django.urls import re_path

from collector.views.frontend import index

urlpatterns = [
    re_path('^$', index, name='index'),

]
