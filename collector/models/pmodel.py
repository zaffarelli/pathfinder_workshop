from django.db import models
import json
from collector.utils.pathfinder_tools import json_default

class Pmodel(models.Model):
    class Meta:
        abstract = True

    def to_json(self):
        jstr = json.dumps(self, default=json_default, sort_keys=True, indent=4)
        return jstr

    def fix(self):
        pass
