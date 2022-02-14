#!/usr/bin/python3

from attributes import Attributes, AttributeList
from job import Job
from skill import SkillList

JOB_LVL_REQS = {1:0, 2:10, 3:30, 4:100, 5:200, 6:400, 7:700, 8:1200, 9:1800}

JOB_LVL_BOOSTS = {1:(3,5), 2:(10,20), 3:(30,50), 4:(60,100), 5:(100,170), 6:(150,250), 7:(300,500), 8:(600,1000), 9:(1000,2000)}

class Character(object):

    def __init__(self, name, age, gender, race, job):
        self.name = name
        self.age = age
        self.gender = gender
        self.race = race
        assert(isinstance(job, Job))
        self.job = job
        self.base_stats = None
        self.stats_set = False
        self.skill_list = None
        self.skills_set = False
        self.unset_skills = 0

    def setBases(self, hp, mp, stre, end, agi, magic, intel, dex, luck):
        bases = {}
        bases[Attributes.HP] = hp
        bases[Attributes.MP] = mp
        bases[Attributes.STRENGTH] = stre
        bases[Attributes.ENDURANCE] = end
        bases[Attributes.AGILITY] = agi
        bases[Attributes.MAGIC] = magic
        bases[Attributes.INTELLIGENCE] = intel
        bases[Attributes.DEXTERITY] = dex
        bases[Attributes.LUCK] = luck
        self.base_stats = AttributeList(bases)
        self.stats_set = True

    def setSkillList(self, skills, empty_slots = 0):
        assert(isinstance(skills, SkillList))
        self.skill_list = skills
        self.skills_set = True
        self.unset_skills = empty_slots

    def isSetup(self):
        return self.stats_set and self.skills_set

    def getJobLevel(self):
        assert(self.isSetup())
        jobSkillTotal = self.skill_list.getJobSkillTotal(self.job)
        jobLevel = 1
        for (jLvl, sTotal) in JOB_LVL_REQS.items():
            if jobSkillTotal >= sTotal:
                if jLvl > jobLevel:
                    jobLevel = jLvl
        return jobLevel

    def getJobBoosts(self):
        jobLevel = self.getJobLevel()
        lvl_boosts = JOB_LVL_BOOSTS[jobLevel]
        jobBoosts = {}
        for attr in [self.job.getFirstAttr(), self.job.getSecondAttr()]:
            if attr in [Attributes.HP, Attributes.MP]:
                jobBoosts[attr] = lvl_boosts[1]
            else:
                jobBoosts[attr] = lvl_boosts[0]
        return AttributeList(jobBoosts)

    def getTotalStats(self):
        return self.base_stats + self.skill_list.getSkillStatBoosts() + self.getJobBoosts()

    def show_status(self):
        print("="*30)
        print()
        print(self.name,'|',self.age,'years old |',self.gender,'|',self.race)
        jobLevel = self.getJobLevel()
        print("Job:",self.job.getName(),"LV"+str(jobLevel))
        jobBoosts = self.getJobBoosts()
        stats = self.getTotalStats()
        assert(len(stats)==len(Attributes))
        for attr in Attributes:
            attrName = attr.name.title()
            if attr in jobBoosts:
                print(attrName+":",stats[attr],"(+"+str(jobBoosts[attr])+")")
            else:
                print(attrName+":",stats[attr])
        print()
        print("Skill Slots")
        self.skill_list.show_skills(self.job)
        if self.unset_skills > 0:
            for _ in range(self.unset_skills):
                print("o Not Set")
        print()
        print("="*30)


