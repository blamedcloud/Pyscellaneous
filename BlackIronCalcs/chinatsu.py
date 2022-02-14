#!/usr/bin/python3

from character import Character
from job import Job
from skill import SkillList
from skill_list import *

from job_list import priest

def chapter113():
    skillList = SkillList()
    skillList.add_skill(lightMagic, 134)
    skillList.add_skill(calculation, 147)
    skillList.add_skill(evasion, 83)
    skillList.add_skill(dangerDetection, 113)
    skillList.add_skill(swordArts, 97)
    skillList.add_skill(encouragement, 38)
    return (skillList, 0)

if __name__ == "__main__":

    chinatsu = Character("Rokusai Chinatsu", 16, "Female", "Human", priest)
    chinatsu.setBases(30,50,30,20,30,50,50,20,20)

    chinatsu.setSkillList(*chapter113())

    chinatsu.show_status()

