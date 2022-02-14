#!/usr/bin/python3

from attributes import Attributes
from skill_names import SkillNames

class Job(object):

    def __init__(self, name, attr1, attr2, job_skills):
        assert(isinstance(attr1, Attributes))
        assert(isinstance(attr2, Attributes))
        assert(attr1 != attr2)
        assert(len(job_skills)>0)
        for sk in job_skills:
            assert(isinstance(sk, SkillNames))
        self.name = name
        self.attr1 = attr1
        self.attr2 = attr2
        self.job_skills = job_skills

    def getName(self):
        return self.name

    def getFirstAttr(self):
        return self.attr1

    def getSecondAttr(self):
        return self.attr2

    def getJobSkills(self):
        return self.job_skills

    def getPrefix(self, skill_name):
        if skill_name in self:
            return "*"
        else:
            return "o"

    def __len__(self):
        return len(self.job_skills)

    def __contains__(self, skill):
        assert(isinstance(skill, SkillNames))
        return skill in self.job_skills
