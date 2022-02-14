#!/usr/bin/python3

from job import Job
from attributes import Attributes
from skill_names import SkillNames

# the lists of job skills are not complete

msSkills = []
msSkills.append(SkillNames.SWORD_ARTS)
msSkills.append(SkillNames.STAFF_ARTS)
msSkills.append(SkillNames.INSTANTANEOUS_FORCE)
msSkills.append(SkillNames.FIRE_MAGIC)
msSkills.append(SkillNames.WATER_MAGIC)
msSkills.append(SkillNames.EARTH_MAGIC)
msSkills.append(SkillNames.WIND_MAGIC)
msSkills.append(SkillNames.LIGHTNING_MAGIC)
msSkills.append(SkillNames.DARK_MAGIC)
msSkills.append(SkillNames.LIGHT_MAGIC)
msSkills.append(SkillNames.MAGIC_WEAPON)
msSkills.append(SkillNames.MAGIC_PRESERVATION)
msSkills.append(SkillNames.MAGIC_POWER_DETECTION)
msSkills.append(SkillNames.CALCULATION)
msSkills.append(SkillNames.WILLPOWER)
magicSwordsman = Job("Magic Swordsman", Attributes.AGILITY, Attributes.MAGIC, msSkills)

mgSkills = []
mgSkills.append(SkillNames.STAFF_ARTS)
mgSkills.append(SkillNames.FIRE_MAGIC)
mgSkills.append(SkillNames.WATER_MAGIC)
mgSkills.append(SkillNames.EARTH_MAGIC)
mgSkills.append(SkillNames.WIND_MAGIC)
mgSkills.append(SkillNames.LIGHTNING_MAGIC)
mgSkills.append(SkillNames.DARK_MAGIC)
mgSkills.append(SkillNames.LIGHT_MAGIC)
mgSkills.append(SkillNames.MAGIC_WEAPON)
mgSkills.append(SkillNames.MAGIC_PRESERVATION)
mgSkills.append(SkillNames.MAGIC_POWER_DETECTION)
mgSkills.append(SkillNames.CALCULATION)
mgSkills.append(SkillNames.COOKING)
magician = Job("Magician", Attributes.MP, Attributes.MAGIC, mgSkills)

prSkills = []
prSkills.append(SkillNames.LIGHT_MAGIC)
prSkills.append(SkillNames.MAGIC_POWER_DETECTION)
prSkills.append(SkillNames.MAGIC_PRESERVATION)
prSkills.append(SkillNames.ENCOURAGEMENT)
prSkills.append(SkillNames.CALCULATION)
prSkills.append(SkillNames.PROTECTION)
priest = Job("Priest", Attributes.MAGIC, Attributes.INTELLIGENCE, prSkills)

frSkills = []
frSkills.append(SkillNames.SWORD_ARTS)
frSkills.append(SkillNames.MARTIAL_ARTS)
frSkills.append(SkillNames.KI_ARTS)
frSkills.append(SkillNames.ARMOR)
frSkills.append(SkillNames.INSTANTANEOUS_FORCE)
frSkills.append(SkillNames.JUMP)
frSkills.append(SkillNames.WILLPOWER)
frSkills.append(SkillNames.DANGER_DETECTION)
frSkills.append(SkillNames.COMMANDER)
fighter = Job("Fighter", Attributes.STRENGTH, Attributes.AGILITY, frSkills)


