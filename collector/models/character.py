from django.db import models
from collector.models.pmodel import Pmodel


class Character(Pmodel):
    class Meta:
        abstract = True

    name = models.CharField(max_length=512, default='', unique=True)
    rid = models.CharField(max_length=512, default='', blank=True)
    need_fix = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def make_rid(self):
        str = self.name.lower()
        tuples = [
            [' ', '_'],
            ['-', '_'],
            ['é', 'e'],
            ['à', 'e'],
            ['è', 'e'],
            ['ê', 'e'],
            ['ë', 'e'],
            ['ö', 'oe'],
            ['ç', 'c'],
            ['ç', 'c'],
            ['ù', 'u']
        ]
        for t in tuples:
            str = str.replace(t[0], t[1])
        return str

    def fix(self):
        super().fix()
        self.rid = self.make_rid()
