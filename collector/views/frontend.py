from django.shortcuts import render, redirect
from collector.utils.pathfinder_tools import FONTSET


def index(request):
    if not request.user.is_authenticated:
        return redirect('accounts/login/')
    context = {'fontset': FONTSET}
    return render(request, 'collector/index.html', context=context)
