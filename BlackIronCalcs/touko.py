#!/usr/bin/python3

from character import Character
from job import Job
from skill import SkillList
from skill_list import *

from job_list import fighter 

def chapter113():
    skillList = SkillList()
    skillList.add_skill(martialArts, 130)
    skillList.add_skill(instantaneousForce, 121)
    skillList.add_skill(jump, 89)
    skillList.add_skill(evasion, 77)
    skillList.add_skill(willpower, 94)
    skillList.add_skill(bigEater, 68)
    return (skillList, 1)

if __name__ == "__main__":

    touko = Character("Mizuhori Touko", 16, "Female", "Human", fighter)
    touko.setBases(40,10,20,20,20,20,20,20,20)

    touko.setSkillList(*chapter113())

    touko.show_status()


