#!/usr/bin/python3

from fractions import Fraction
import random
from enum import Enum


def random_roll(chance):
    roll = random.randint(1,100)
    return roll <= chance


class CombatDeaths(Enum):
    DIE = 0
    KILL = 1
    NEITHER = 2


class CombatOutcome(object):

    def __init__(self, your_hits, enemy_hits, deaths):
        self.your_hits = your_hits
        self.enemy_hits = enemy_hits
        self.deaths = deaths


class HitOutcome(object):

    def __init__(self, hits, cancel):
        self.num_hits = hits
        self.cancelled = cancel

    def __add__(self, other):
        return HitOutcome(self.num_hits + other.num_hits, self.cancelled or other.cancelled)


class TrueBlade(object):

    def __init__(self, hit, crit, skill, speed, enemy_hit, enemy_crit):
        self.hit_chance = hit
        self.crit_chance = crit
        self.skill_stat = skill
        self.speed_stat = speed

        self.enemy_hit = enemy_hit
        self.enemy_crit = enemy_crit

        self.has_adept = False
        self.has_vantage = False
        self.has_cancel = False
        self.has_pavise = False
        self.has_astra = False

    def set_skills(self, adept, astra, cancel, pavise, vantage):
        self.has_adept = adept
        self.has_astra = astra
        self.has_cancel = cancel
        self.has_pavise = pavise
        self.has_vantage = vantage

    def show_skills(self):
        print("Adept:  ",self.has_adept)
        print("Astra:  ",self.has_astra)
        print("Cancel: ",self.has_cancel)
        print("Pavise: ",self.has_pavise)
        print("Vantage:",self.has_vantage)

    def run_scenario(self, htk, htd, init, num_runs, single = False):
        num_die = 0
        num_kill = 0
        num_neither = 0
        for _ in range(num_runs):
            outcome = None
            if single:
                outcome = self.single_combat(htk, htd, init).deaths
            else:
                outcome = self.repeated_combat(htk, htd, init)
            if outcome is CombatDeaths.KILL:
                num_kill += 1
            elif outcome is CombatDeaths.DIE:
                num_die += 1
            else:
                num_neither += 1
        print("Num kills:  ",num_kill)
        print("Num deaths: ",num_die)
        print("Num neither:",num_neither)

    def repeated_combat(self, hits_to_kill, hits_to_die, initiate):
        outcome = self.single_combat(hits_to_kill, hits_to_die, initiate)
        if outcome.deaths == CombatDeaths.NEITHER:
            return self.repeated_combat(hits_to_kill - outcome.your_hits, hits_to_die - outcome.enemy_hits, not initiate)
        else:
            return outcome.deaths

    def single_combat(self, hits_to_kill, hits_to_die, initiate):
        if not initiate and self.has_vantage and random_roll(self.speed_stat):
            return self.single_combat(hits_to_kill, hits_to_die, True)

        your_hits = 0
        enemy_hits = 0
        deaths = CombatDeaths.NEITHER

        if not initiate:
            enemy_hits = self.enemy_hit_()

            if enemy_hits >= hits_to_die:
                deaths = CombatDeaths.DIE
            else:
                first_hit = self.single_hit_()
                your_hits = first_hit.num_hits
                if your_hits >= hits_to_kill:
                    deaths = CombatDeaths.KILL
                else:
                    second_hit = self.single_hit_()
                    your_hits += second_hit.num_hits
                    if your_hits >= hits_to_kill:
                        deaths = CombatDeaths.KILL
        else:
            first_hit = self.single_hit_()
            your_hits = first_hit.num_hits

            if your_hits >= hits_to_kill:
                deaths = CombatDeaths.KILL
            else:
                if not first_hit.cancelled:
                    enemy_hits = self.enemy_hit_()
                if enemy_hits >= hits_to_die:
                    deaths = CombatDeaths.DIE
                else: 
                    second_hit = self.single_hit_()
                    your_hits += second_hit.num_hits

                    if your_hits >= hits_to_kill:
                        deaths = CombatDeaths.KILL

        return CombatOutcome(your_hits, enemy_hits, deaths)
            
    def enemy_hit_(self):
        enemy_hits = 0

        pavise_proc = False
        if self.has_pavise:
            pavise_proc = random_roll(self.skill_stat)
        if not pavise_proc:
            if random_roll(self.enemy_hit):
                if random_roll(self.enemy_crit):
                    enemy_hits += 3
                else:
                    enemy_hits += 1
        return enemy_hits

    # check order assumptions:
    # adept > astra > hit > crit > cancel
    # (note that astra hits cannot crit - which is dumb)
    # (I'm also not sure if crit is checked after hit or not)
    def single_hit_(self):
        if self.has_adept:
            adept_proc = random_roll(self.speed_stat)
            if adept_proc:
                return self.non_adept_hit_() + self.non_adept_hit_()
        return self.non_adept_hit_()

    def non_adept_hit_(self):
        hits = 0
        cancel = False

        astra_proc = False
        if self.has_astra:
            # currently this breaks on odd skill stats
            astra_proc = random_roll(self.skill_stat/2)

        if astra_proc:
            for _ in range(5):
                if random_roll(self.hit_chance):
                    hits += 1
                    # this assumes astra hits can proc cancel (idk if that is true or not)
                    if self.has_cancel:
                        cancel = cancel or random_roll(self.speed_stat)
        else:
            if random_roll(self.hit_chance):
                if random_roll(self.crit_chance):
                    hits += 3
                else:
                    hits += 1
                if self.has_cancel:
                    cancel = cancel or random_roll(self.speed_stat)
        return HitOutcome(hits, cancel)


if __name__ == "__main__":

    runs = 100000

    tb = TrueBlade(95,25,40,40,20,0)

    print("No skills, 3-1-True")
    tb.run_scenario(3,1,True,runs)

    # adept, astra, cancel, pavise, vantage
    tb.set_skills(True,True,True,True,False)
    tb.show_skills()

    print("All skills, 4-2-True")
    tb.run_scenario(4,2,True,runs)
    print("All skills, 4-2-False")
    tb.run_scenario(4,2,False,runs)

