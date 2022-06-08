from django.db import models


class Pmodel(models.Model):
    class Meta:
        abstract = True

    @property
    def to_json(self):
        str = ''
        return str

    def fix(self):
        pass