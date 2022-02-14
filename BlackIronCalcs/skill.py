#!/usr/bin/python3

from attributes import Attributes, AttributeList
from skill_names import SkillNames
from job import Job


class Skill(object):

    def __init__(self, name, atr1, atr2, atr3, atr4):
        assert(isinstance(name, SkillNames))
        self.name = name
        self.attribute_gains = {}
        for atr in [atr1, atr2, atr3, atr4]:
            assert(isinstance(atr, Attributes))
            boost = 1
            if atr in [Attributes.HP, Attributes.MP]:
                boost = 5
            if atr in self.attribute_gains:
                self.attribute_gains[atr] += boost
            else:
                self.attribute_gains[atr] = boost

    def getName(self):
        return self.name

    def getPrintableName(self):
        return self.name.name.title().replace('_',' ')

    def gains_at_level(self, level):
        if level > 200:
            gains = lambda boost, lvl: 300*boost + (lvl-200)*boost*4
        elif level > 100:
            gains = lambda boost, lvl: 100*boost + (lvl-100)*boost*2
        else: # level <= 100
            gains = lambda boost, lvl: lvl*boost
        level_gains = {atr:gains(boost,level) for (atr, boost) in self.attribute_gains.items()}
        return AttributeList(level_gains)


class SkillList(object):

    def __init__(self):
        self.skills = {}

    def add_skill(self, skill, lvl):
        assert(isinstance(skill, Skill))
        assert(skill not in self.skills)
        self.skills[skill] = lvl

    def __len__(self):
        return len(self.skills)

    def __contains__(self, skill):
        assert(isinstance(skill, Skill))
        return skill in self.skills

    def getJobSkillTotal(self, job):
        assert(isinstance(job, Job))
        jobSkillTotal = 0
        for (skill, level) in self.skills.items():
            if skill.getName() in job:
                jobSkillTotal += level
        return jobSkillTotal

    def getSkillStatBoosts(self):
        boosts = AttributeList({})
        for (skill, level) in self.skills.items():
            boosts += skill.gains_at_level(level)
        return boosts

    def show_skills(self, job):
        assert(isinstance(job, Job))
        for (skill, level) in self.skills.items():
            prefix = job.getPrefix(skill.getName())
            print(prefix,skill.getPrintableName(),"LV"+str(level))
