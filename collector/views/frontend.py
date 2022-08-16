from django.shortcuts import render, redirect
from collector.utils.pathfinder_tools import FONTSET, get_modifier, as_modifier, as_squares
from collector.models.pathfinder_character import PathfinderCharacter
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from collector.utils.tools import is_ajax
import json
import math


def index(request):
    if not request.user.is_authenticated:
        return redirect('accounts/login/')
    characters = PathfinderCharacter.objects.order_by('-in_spotlight','-current_xp','-player',  'name')
    ch = []
    for c in characters:
        ch.append({'name': c.name, 'rid': c.rid, 'object': c.to_json(), 'roster': c.roster, 'player': c.player})
    context = {'fontset': FONTSET, 'characters': ch}
    return render(request, 'collector/index.html', context=context)


@csrf_exempt
def display_crossover_sheet(request, slug=None, option=None):
    if is_ajax(request):
        if slug is None:
            slug = 'julius_von_blow'
        c = PathfinderCharacter.objects.get(rid=slug)
        c.creature = 'PC'
        c.race_name = c.race.name
        c.alignment_str = c.alignment
        c.gender_str = c.get_gender_display()
        c.size = "Medium"
        if c.is_small:
            c.size = "Small"
        c.ccl = c.character_class_levels
        c.height_foot = f'{math.floor(c.height / 12)} ft. {c.height % 12} in.'
        c.weight_lbs = f'{c.weight} lbs'
        c.height_m = f'{math.floor(c.height * 2.54) / 100}'
        c.weight_kg = f'{c.weight / 2}'
        c.deity = c.fetch_deity()
        c.STR_mod = as_modifier(get_modifier(c.STR))
        c.DEX_mod = as_modifier(get_modifier(c.DEX))
        c.CON_mod = as_modifier(get_modifier(c.CON))
        c.INT_mod = as_modifier(get_modifier(c.INT))
        c.WIS_mod = as_modifier(get_modifier(c.WIS))
        c.CHA_mod = as_modifier(get_modifier(c.CHA))

        c.speed_sq = as_squares(c.speed)
        c.armor_speed_sq = as_squares(c.armor_speed)
        c.ranks_summary = c.total_ranks

        c.all_weapons = [{},{},{},{},{},{},{},{},{},{}]
        print(c.all_weapons)


        c.all_ranks = c.sheet_skills

        c.armor_bonus = c.AC_armor_bonus
        c.shield_bonus = "+4"

        c.nb_feats = c.total_feats
        c.spellbook = c.spells_lists

        c.feats_list = c.all_feats
        c.all_features = c.all_class_features

        # print(c.all_ranks)

        # spe = c.get_specialities()
        # shc = c.get_shortcuts()
        j = c.to_json()
        # k = json.loads(j)
        # k["sire_name"] = c.sire_name
        # k["background_notes"] = c.background_notes()
        # k["timeline"] = c.timeline()
        # k["disciplines_notes"] = c.disciplines_notes()
        # k["nature_notes"] = c.nature_notes()
        # k["meritsflaws_notes"] = c.meritsflaws_notes()
        # # print("DISCPLINES NOTES ---> ", k["disciplines_notes"])
        # j = json.dumps(k)
        pre_title = ""
        post_title = ""
        scenario = "Summer 2022 OS sessions"
        settings = {'version': 1.0, 'labels': {}, 'pre_title': pre_title, 'scenario': scenario,
                    'post_title': post_title, 'fontset': FONTSET, 'specialities': {}, 'shortcuts': {}}
        crossover_sheet_context = {'settings': json.dumps(settings, sort_keys=True, indent=4), 'data': j}

        return JsonResponse(crossover_sheet_context)
