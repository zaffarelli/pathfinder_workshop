from django.urls import re_path

from collector.views.frontend import index, display_crossover_sheet

urlpatterns = [
    re_path('^$', index, name='index'),
    re_path(r'^ajax/action/character_sheet/(?P<slug>\w+)/$', display_crossover_sheet, name='display_crossover_sheet'),
    re_path(r'^ajax/action/character_sheet/(?P<slug>\w+)/(?P<option>\w+)/$', display_crossover_sheet,name='display_crossover_sheet'),
]
