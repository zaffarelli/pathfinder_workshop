from django.db import models
from django.contrib import admin
from collector.models.pathfinder_spells_collection import PathfinderSpellsCollection

LARGE_STR = 64 * 4
STD_STR = 64 * 3
BIG_SIZE = 1024 * 6
HUGE_TEXT = 1024 * 8


class PathfinderSpell(models.Model):
    class Meta:
        verbose_name = 'Pathfinder Spell'

    name = models.CharField(max_length=STD_STR, default='', blank=True)
    school = models.CharField(max_length=STD_STR, default='', blank=True)
    subschool = models.CharField(max_length=STD_STR, default='', blank=True)
    descriptor = models.CharField(max_length=STD_STR, default='', blank=True)
    spell_level = models.CharField(max_length=LARGE_STR, default='', blank=True)
    casting_time = models.CharField(max_length=STD_STR, default='', blank=True)
    components = models.CharField(max_length=LARGE_STR, default='', blank=True)
    costly_components = models.CharField(max_length=STD_STR, default='', blank=True)
    range = models.CharField(max_length=STD_STR, default='', blank=True)
    area = models.CharField(max_length=STD_STR, default='', blank=True)
    effect = models.CharField(max_length=STD_STR, default='', blank=True)
    targets = models.CharField(max_length=LARGE_STR, default='', blank=True)
    duration = models.CharField(max_length=STD_STR, default='', blank=True)
    dismissible = models.CharField(max_length=STD_STR, default='', blank=True)
    shapeable = models.CharField(max_length=STD_STR, default='', blank=True)
    saving_throw = models.CharField(max_length=STD_STR, default='', blank=True)
    spell_resistance = models.CharField(max_length=LARGE_STR, default='', blank=True)
    description = models.TextField(max_length=BIG_SIZE, default='', blank=True)
    description_formatted = models.TextField(max_length=BIG_SIZE, default='', blank=True)

    spells_collection = models.ManyToManyField(PathfinderSpellsCollection, blank=True)

    source = models.CharField(max_length=STD_STR, default='', blank=True)
    full_text = models.TextField(max_length=HUGE_TEXT, default='', blank=True)

    verbal = models.BooleanField(default=False, blank=True)
    somatic = models.BooleanField(default=False, blank=True)
    material = models.BooleanField(default=False, blank=True)
    focus = models.BooleanField(default=False, blank=True)
    divine_focus = models.BooleanField(default=False, blank=True)

    sor = models.IntegerField(default=-1, blank=True, null=True)
    wiz = models.IntegerField(default=-1, blank=True, null=True)
    cleric = models.IntegerField(default=-1, blank=True, null=True)
    druid = models.IntegerField(default=-1, blank=True, null=True)
    ranger = models.IntegerField(default=-1, blank=True, null=True)
    bard = models.IntegerField(default=-1, blank=True, null=True)
    paladin = models.IntegerField(default=-1, blank=True, null=True)
    alchemist = models.IntegerField(default=-1, blank=True, null=True)
    summoner = models.IntegerField(default=-1, blank=True, null=True)
    witch = models.IntegerField(default=-1, blank=True, null=True)
    inquisitor = models.IntegerField(default=-1, blank=True, null=True)
    oracle = models.IntegerField(default=-1, blank=True, null=True)
    antipaladin = models.IntegerField(default=-1, blank=True, null=True)
    magus = models.IntegerField(default=-1, blank=True, null=True)
    adept = models.IntegerField(default=-1, blank=True, null=True)

    deity = models.CharField(max_length=STD_STR, default='', blank=True)
    SLA_Level = models.CharField(max_length=STD_STR, default='', blank=True)
    domain = models.CharField(max_length=STD_STR, default='', blank=True)
    short_description = models.TextField(max_length=BIG_SIZE, default='', blank=True)

    acid = models.BooleanField(default=False, blank=True)
    air = models.BooleanField(default=False, blank=True)
    chaotic = models.BooleanField(default=False, blank=True)
    cold = models.BooleanField(default=False, blank=True)
    curse = models.BooleanField(default=False, blank=True)
    darkness = models.BooleanField(default=False, blank=True)
    death = models.BooleanField(default=False, blank=True)
    disease = models.BooleanField(default=False, blank=True)
    earth = models.BooleanField(default=False, blank=True)
    electricity = models.BooleanField(default=False, blank=True)
    emotion = models.BooleanField(default=False, blank=True)
    evil = models.BooleanField(default=False, blank=True)
    fear = models.BooleanField(default=False, blank=True)
    fire = models.BooleanField(default=False, blank=True)
    force = models.BooleanField(default=False, blank=True)
    good = models.BooleanField(default=False, blank=True)
    language_dependent = models.BooleanField(default=False, blank=True)
    lawful = models.BooleanField(default=False, blank=True)
    light = models.BooleanField(default=False, blank=True)
    mind_affecting = models.BooleanField(default=False, blank=True)
    pain = models.BooleanField(default=False, blank=True)
    poison = models.BooleanField(default=False, blank=True)
    shadow = models.BooleanField(default=False, blank=True)
    sonic = models.BooleanField(default=False, blank=True)
    water = models.BooleanField(default=False, blank=True)

    linktext = models.CharField(max_length=STD_STR, default='', blank=True)
    src_id = models.CharField(max_length=STD_STR, default='', blank=True)

    material_costs = models.CharField(max_length=STD_STR, default='', blank=True)
    bloodline = models.CharField(max_length=STD_STR, default='', blank=True)
    patron = models.CharField(max_length=STD_STR, default='', blank=True)
    mythic_text = models.TextField(max_length=BIG_SIZE, default='', blank=True)
    augmented = models.TextField(max_length=BIG_SIZE, default='', blank=True)
    mythic = models.BooleanField(default=False, blank=True)

    bloodrager = models.CharField(max_length=STD_STR, default='', blank=True)
    shaman = models.CharField(max_length=STD_STR, default='', blank=True)
    psychic = models.CharField(max_length=STD_STR, default='', blank=True)
    medium = models.CharField(max_length=STD_STR, default='', blank=True)
    mesmerist = models.CharField(max_length=STD_STR, default='', blank=True)
    occultist = models.CharField(max_length=STD_STR, default='', blank=True)
    spiritualist = models.CharField(max_length=STD_STR, default='', blank=True)
    skald = models.CharField(max_length=STD_STR, default='', blank=True)
    investigator = models.CharField(max_length=STD_STR, default='', blank=True)
    hunter = models.CharField(max_length=STD_STR, default='', blank=True)
    haunt_statistics = models.TextField(max_length=BIG_SIZE, default='', blank=True)

    ruse = models.BooleanField(default=False, blank=True)
    draconic = models.BooleanField(default=False, blank=True)
    meditative = models.BooleanField(default=False, blank=True)
    summoner_unchained = models.CharField(max_length=STD_STR, default='', blank=True)

    def __str__(self):
        return f'{self.name}'


class PathfinderSpellAdmin(admin.ModelAdmin):
    ordering = ['SLA_Level', "name"]
    list_display = ['name', 'SLA_Level', 'source', 'school', 'short_description', 'wiz', 'cleric', 'druid']
    list_filter = ['source', 'druid', 'wiz', 'sor', 'cleric', 'paladin', 'ranger', 'bard']
    search_fields = ['name', 'description']

