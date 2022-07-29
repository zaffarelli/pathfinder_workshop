from django.shortcuts import render, redirect
from collector.utils.pathfinder_tools import FONTSET
from collector.models.pathfinder_character import PathfinderCharacter


def index(request):
    if not request.user.is_authenticated:
        return redirect('accounts/login/')
    characters = PathfinderCharacter.objects.order_by('-current_xp', 'name')
    ch = []
    for c in characters:
        ch.append({'name': c.name,'rid':c.rid, 'object': c.to_json(), 'roster': c.roster})
    context = {'fontset': FONTSET, 'characters': ch}
    return render(request, 'collector/index.html', context=context)
