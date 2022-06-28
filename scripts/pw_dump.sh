#!/bin/bash
clear

mkdir -p backup/custom/$1/
mkdir -p backup/reference/$1/


rm -f backup/custom/$1/*
rm -f backup/reference/$1/*
rm -f collector/fixtures/*

echo -e "\e[1;35mCOLLECTOR REFERENCES...\e[0;m"
python manage.py dumpdata collector.PathfinderGear --format xml --output backup/reference/$1/pathfinder_gear.xml
python manage.py dumpdata collector.PathfinderArmor --format xml --output backup/reference/$1/pathfinder_armor.xml
python manage.py dumpdata collector.PathfinderWeapon --format xml --output backup/reference/$1/pathfinder_weapon.xml
python manage.py dumpdata collector.PathfinderFeat --format xml --output backup/reference/$1/pathfinder_feat.xml
python manage.py dumpdata collector.PathfinderSkill --format xml --output backup/reference/$1/pathfinder_skill.xml
python manage.py dumpdata collector.PathfinderRace --format xml --output backup/reference/$1/pathfinder_race.xml
python manage.py dumpdata collector.PathfinderClass --format xml --output backup/reference/$1/pathfinder_class.xml
python manage.py dumpdata collector.PathfinderSpell --format xml --output backup/reference/$1/pathfinder_spell.xml


echo -e "\e[1;35mCOLLECTOR CUSTOM...\e[0;m"
python manage.py dumpdata collector.PathfinderCharacter --format xml --output backup/custom/$1/pathfinder_character.xml
python manage.py dumpdata collector.PathfinderLevel --format xml --output backup/custom/$1/pathfinder_level.xml
python manage.py dumpdata collector.PathfinderRank --format xml --output backup/custom/$1/pathfinder_rank.xml



echo -e "\e[1;35mMoving to fixtures...\e[0;m"
cp backup/reference/$1/* collector/fixtures/



echo -e "\e[1;35m...done\e[0;m"
