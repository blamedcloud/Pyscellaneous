#!/usr/bin/python3

from character import Character
from job import Job
from skill import SkillList
from skill_list import *

from job_list import magician

def chapter7():
    skillList = SkillList()
    skillList.add_skill(martialArts, 17)
    return (skillList, 1)
    
def chapter113():
    skillList = SkillList()
    skillList.add_skill(martialArts, 107)
    skillList.add_skill(darkMagic, 92)
    skillList.add_skill(staffArts, 114)
    skillList.add_skill(pleasantSleep, 42)
    skillList.add_skill(evasion, 95)
    skillList.add_skill(throwing, 120)
    skillList.add_skill(magicPowerDetection, 41)
    skillList.add_skill(strongShoulder, 74)
    return (skillList, 2)

def chapter173():
    skillList = SkillList()
    skillList.add_skill(martialArts, 136)
    skillList.add_skill(darkMagic, 120)
    skillList.add_skill(staffArts, 158)
    skillList.add_skill(pleasantSleep, 57)
    skillList.add_skill(evasion, 126)
    skillList.add_skill(throwing, 160)
    skillList.add_skill(magicPowerDetection, 73)
    skillList.add_skill(strongShoulder, 134)
    skillList.add_skill(cooking, 64)
    skillList.add_skill(jump, 50)
    return (skillList, 2)


if __name__ == "__main__":

    haruna = Character("Katsuragi Haruna", 16, "Female", "Human", magician)
    haruna.setBases(10,0,1,1,1,1,1,1,1)

    #haruna.setSkillList(*chapter7())
    haruna.setSkillList(*chapter113())
    #haruna.setSkillList(*chapter173())

    haruna.show_status()
