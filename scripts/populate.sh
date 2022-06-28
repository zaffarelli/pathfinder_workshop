#!/bin/bash

python ./manage.py shell < ./scripts/populate.py
python ./manage.py shell < ./scripts/load_spells.py