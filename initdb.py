#!/usr/bin/python
import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Float, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from destinygotg import load_config

Base = declarative_base()

class Bungie(Base):
    __tablename__ = 'bungie'
    id = Column(String(50), primary_key=True)
    bungie_name = Column(String(50), nullable=False)
    membership_type = Column(Integer, nullable=False)

class Account(Base):
    __tablename__ = 'account'
    id = Column(Integer, primary_key=True)
    display_name = Column(String(50), nullable=False)
    membership_type = Column(Integer, nullable=False)
    bungie_id = Column(String(50), ForeignKey('bungie.id'))
    bungie = relationship(Bungie)

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    membership_id = Column(Integer, ForeignKey('account.id'))
    account = relationship(Account)
    level = Column(Integer)
    class_hash = Column(Integer)
    class_type = Column(Integer)
    last_played = Column(DateTime)
    light_level = Column(Integer)
    minutes_played = Column(Integer)
    race_hash = Column(Integer)
    race_type = Column(Integer)

class Discord(Base):
    __tablename__ = 'discord'
    id = Column(Integer, primary_key=True)
    membership_id = Column(Integer, ForeignKey('account.id'), primary_key=True)
    account = relationship(Account)
    discord_name = Column(String(50))

class CharacterInstanceStats(Base):
    __tablename__ = "characterInstanceStats"
    id = Column(Integer, primary_key=True)
    instance_id = Column(Integer, primary_key=True)
    mode = Column(Integer)
    reference_id = Column(Integer)
    is_private = Column(Boolean)
    period = Column(DateTime)
    activityDurationSeconds = Column(Integer)
    assists = Column(Integer)
    averageScorePerKill = Column(Integer)
    averageScorePerLife = Column(Integer)
    completed = Column(Integer)
    completionReason = Column(Integer)
    deaths = Column(Integer)
    fireteamId = Column(Integer)
    kills = Column(Integer)
    killsDeathsAssists = Column(Integer)
    killsDeathsRatio = Column(Integer)
    playerCount = Column(Integer)
    score = Column(Integer)
    standing = Column(Integer)
    startSeconds = Column(Integer)
    team = Column(Integer)
    teamScore = Column(Integer)
    timePlayedSeconds = Column(Integer)

class CharacterPvPStats(Base):

"abilityKills": {
"basic": {
"displayValue": "22",
"value": 22.0
},
"pga": {
"displayValue": "7.3",
"value": 7.333333333333333
},
"statId": "abilityKills"
},
"activitiesEntered": {
"basic": {
"displayValue": "3",
"value": 3.0
},
"statId": "activitiesEntered"
},
"activitiesWon": {
"basic": {
"displayValue": "2",
"value": 2.0
},
"statId": "activitiesWon"
},
"allParticipantsCount": {
"basic": {
"displayValue": "24",
"value": 24.0
},
"statId": "allParticipantsCount"
},
"allParticipantsScore": {
"basic": {
"displayValue": "313",
"value": 313.0
},
"statId": "allParticipantsScore"
},
"allParticipantsTimePlayed": {
"basic": {
"displayValue": "3h 40m",
"value": 13200.0
},
"statId": "allParticipantsTimePlayed"
},
"assists": {
"basic": {
"displayValue": "19",
"value": 19.0
},
"pga": {
"displayValue": "6.3",
"value": 6.333333333333333
},
"statId": "assists"
},
"averageDeathDistance": {
"basic": {
"displayValue": "0.0",
"value": 0.0
},
"statId": "averageDeathDistance"
},
"averageKillDistance": {
"basic": {
"displayValue": "10.2",
"value": 10.235294117647058
},
"statId": "averageKillDistance"
},
"averageLifespan": {
"basic": {
"displayValue": "0m 53s",
"value": 53.58064516129032
},
"statId": "averageLifespan"
},
"averageScorePerKill": {
"basic": {
"displayValue": "1",
"value": 1.2745098039215685
},
"statId": "averageScorePerKill"
},
"averageScorePerLife": {
"basic": {
"displayValue": "2",
"value": 2.096774193548387
},
"statId": "averageScorePerLife"
},
"bestSingleGameKills": {
"basic": {
"displayValue": "20",
"value": 20.0
},
"statId": "bestSingleGameKills"
},
"bestSingleGameScore": {
"basic": {
"displayValue": "31",
"value": 31.0
},
"statId": "bestSingleGameScore"
},
"combatRating": {
"basic": {
"displayValue": "165.03",
"value": 165.03395891077585
},
"statId": "combatRating"
},
"deaths": {
"basic": {
"displayValue": "30",
"value": 30.0
},
"pga": {
"displayValue": "10.0",
"value": 10.0
},
"statId": "deaths"
},
"fastestCompletionMs": {
"basic": {
"displayValue": "8:59.600",
"value": 539600.0
},
"statId": "fastestCompletionMs"
},
"highestCharacterLevel": {
"basic": {
"displayValue": "20",
"value": 20.0
},
"statId": "highestCharacterLevel"
},
"highestLightLevel": {
"basic": {
"displayValue": "257",
"value": 257.0
},
"statId": "highestLightLevel"
},
"kills": {
"basic": {
"displayValue": "51",
"value": 51.0
},
"pga": {
"displayValue": "17.0",
"value": 17.0
},
"statId": "kills"
},
"killsDeathsAssists": {
"basic": {
"displayValue": "2.02",
"value": 2.0166666666666666
},
"statId": "killsDeathsAssists"
},
"killsDeathsRatio": {
"basic": {
"displayValue": "1.70",
"value": 1.7
},
"statId": "killsDeathsRatio"
},
"longestKillDistance": {
"basic": {
"displayValue": "39.0",
"value": 39.0
},
"statId": "longestKillDistance"
},
"longestKillSpree": {
"basic": {
"displayValue": "5",
"value": 5.0
},
"statId": "longestKillSpree"
},
"longestSingleLife": {
"basic": {
"displayValue": "1m 51s",
"value": 111.0
},
"statId": "longestSingleLife"
},
"mostPrecisionKills": {
"basic": {
"displayValue": "3",
"value": 3.0
},
"statId": "mostPrecisionKills"
},
"objectivesCompleted": {
"basic": {
"displayValue": "31",
"value": 31.0
},
"pga": {
"displayValue": "10.3",
"value": 10.333333333333334
},
"statId": "objectivesCompleted"
},
"orbsDropped": {
"basic": {
"displayValue": "3",
"value": 3.0
},
"pga": {
"displayValue": "1.0",
"value": 1.0
},
"statId": "orbsDropped"
},
"orbsGathered": {
"basic": {
"displayValue": "2",
"value": 2.0
},
"pga": {
"displayValue": "0.7",
"value": 0.6666666666666666
},
"statId": "orbsGathered"
},
"precisionKills": {
"basic": {
"displayValue": "5",
"value": 5.0
},
"pga": {
"displayValue": "1.7",
"value": 1.6666666666666667
},
"statId": "precisionKills"
},
"remainingTimeAfterQuitSeconds": {
"basic": {
"displayValue": "0m 0s",
"value": 0.0
},
"pga": {
"displayValue": "0m 0s",
"value": 0.0
},
"statId": "remainingTimeAfterQuitSeconds"
},
"resurrectionsPerformed": {
"basic": {
"displayValue": "0",
"value": 0.0
},
"pga": {
"displayValue": "0.0",
"value": 0.0
},
"statId": "resurrectionsPerformed"
},
"resurrectionsReceived": {
"basic": {
"displayValue": "0",
"value": 0.0
},
"pga": {
"displayValue": "0.0",
"value": 0.0
},
"statId": "resurrectionsReceived"
},
"score": {
"basic": {
"displayValue": "65",
"value": 65.0
},
"pga": {
"displayValue": "22",
"value": 21.666666666666668
},
"statId": "score"
},
"secondsPlayed": {
"basic": {
"displayValue": "27m 41s",
"value": 1661.0
},
"pga": {
"displayValue": "9m 13s",
"value": 553.6666666666666
},
"statId": "secondsPlayed"
},
"suicides": {
"basic": {
"displayValue": "0",
"value": 0.0
},
"pga": {
"displayValue": "0.0",
"value": 0.0
},
"statId": "suicides"
},
"teamScore": {
"basic": {
"displayValue": "180",
"value": 180.0
},
"pga": {
"displayValue": "60",
"value": 60.0
},
"statId": "teamScore"
},
"totalActivityDurationSeconds": {
"basic": {
"displayValue": "27m 47s",
"value": 1667.0
},
"pga": {
"displayValue": "9m 15s",
"value": 555.6666666666666
},
"statId": "totalActivityDurationSeconds"
},
"totalDeathDistance": {
"basic": {
"displayValue": "0.0",
"value": 0.0
},
"statId": "totalDeathDistance"
},
"totalKillDistance": {
"basic": {
"displayValue": "522.0",
"value": 522.0
},
"statId": "totalKillDistance"
},
"weaponBestType": {
"basic": {
"displayValue": "Pulse Rifle",
"value": 2.0
},
"statId": "weaponBestType"
},
"weaponKillsAbility": {
"basic": {
"displayValue": "0",
"value": 0.0
},
"pga": {
"displayValue": "0.0",
"value": 0.0
},
"statId": "weaponKillsAbility"
},
"weaponKillsAutoRifle": {
"basic": {
"displayValue": "0",
"value": 0.0
},
"pga": {
"displayValue": "0.0",
"value": 0.0
},
"statId": "weaponKillsAutoRifle"
},
"weaponKillsFusionRifle": {
"basic": {
"displayValue": "9",
"value": 9.0
},
"pga": {
"displayValue": "3.0",
"value": 3.0
},
"statId": "weaponKillsFusionRifle"
},
"weaponKillsGrenade": {
"basic": {
"displayValue": "2",
"value": 2.0
},
"pga": {
"displayValue": "0.7",
"value": 0.6666666666666666
},
"statId": "weaponKillsGrenade"
},
"weaponKillsHandCannon": {
"basic": {
"displayValue": "8",
"value": 8.0
},
"pga": {
"displayValue": "2.7",
"value": 2.6666666666666665
},
"statId": "weaponKillsHandCannon"
},
"weaponKillsMachinegun": {
"basic": {
"displayValue": "0",
"value": 0.0
},
"pga": {
"displayValue": "0.0",
"value": 0.0
},
"statId": "weaponKillsMachinegun"
},
"weaponKillsMelee": {
"basic": {
"displayValue": "13",
"value": 13.0
},
"pga": {
"displayValue": "4.3",
"value": 4.333333333333333
},
"statId": "weaponKillsMelee"
},
"weaponKillsPulseRifle": {
"basic": {
"displayValue": "11",
"value": 11.0
},
"pga": {
"displayValue": "3.7",
"value": 3.6666666666666665
},
"statId": "weaponKillsPulseRifle"
},
"weaponKillsRelic": {
"basic": {
"displayValue": "0",
"value": 0.0
},
"pga": {
"displayValue": "0.0",
"value": 0.0
},
"statId": "weaponKillsRelic"
},
"weaponKillsRocketLauncher": {
"basic": {
"displayValue": "0",
"value": 0.0
},
"pga": {
"displayValue": "0.0",
"value": 0.0
},
"statId": "weaponKillsRocketLauncher"
},
"weaponKillsScoutRifle": {
"basic": {
"displayValue": "0",
"value": 0.0
},
"pga": {
"displayValue": "0.0",
"value": 0.0
},
"statId": "weaponKillsScoutRifle"
},
"weaponKillsShotgun": {
"basic": {
"displayValue": "0",
"value": 0.0
},
"pga": {
"displayValue": "0.0",
"value": 0.0
},
"statId": "weaponKillsShotgun"
},
"weaponKillsSideArm": {
"basic": {
"displayValue": "0",
"value": 0.0
},
"pga": {
"displayValue": "0.0",
"value": 0.0
},
"statId": "weaponKillsSideArm"
},
"weaponKillsSniper": {
"basic": {
"displayValue": "0",
"value": 0.0
},
"pga": {
"displayValue": "0.0",
"value": 0.0
},
"statId": "weaponKillsSniper"
},
"weaponKillsSubmachinegun": {
"basic": {
"displayValue": "0",
"value": 0.0
},
"pga": {
"displayValue": "0.0",
"value": 0.0
},
"statId": "weaponKillsSubmachinegun"
},
"weaponKillsSuper": {
"basic": {
"displayValue": "7",
"value": 7.0
},
"pga": {
"displayValue": "2.3",
"value": 2.3333333333333335
},
"statId": "weaponKillsSuper"
},
"weaponKillsSword": {
"basic": {
"displayValue": "0",
"value": 0.0
},
"pga": {
"displayValue": "0.0",
"value": 0.0
},
"statId": "weaponKillsSword"
},
"winLossRatio": {
"basic": {
"displayValue": "2.00",
"value": 2.0
},
"statId": "winLossRatio"
}

# class PvEAggregate(Base):
#     __tablename__ = 'pveAggregate'
#     id = Column(Integer, ForeignKey('account.id'), primary_key=True)
#     account = relationship(Account)
#     abilityKills = Column(Integer)
#     activitiesCleared = Column(Integer)
#     activitiesEntered = Column(Integer)
#     allParticipantsCount = Column(Integer)
#     allParticipantsTimePlayed = Column(Integer)
#     assists = Column(Integer)
#     averageKillDistance = Column(Float)
#     averageLifespan = Column(Float)
#     averageDeathDistance = Column(Float)
#     bestSingleGameKills = Column(Integer)
#     courtOfOryxAttempts = Column(Integer)
#     courtOfOryxCompletions = Column(Integer)
#     courtOfOryxWinsTier1 = Column(Integer)
#     courtOfOryxWinsTier2 = Column(Integer)
#     courtOfOryxWinsTier3 = Column(Integer)
#     deaths = Column(Integer)
#     fastestCompletion = Column(Integer)
#     highestCharacterLevel = Column(Integer)
#     highestLightLevel = Column(Integer)
#     kills = Column(Integer)
#     killsDeathsAssists = Column(Float)
#     killsDeathsRatio = Column(Float)
#     longestKillDistance = Column(Integer)
#     longestKillSpree = Column(Integer)
#     longestSingleLife = Column(Integer)
#     mostPrecisionKills = Column(Integer)
#     objectivesCompleted = Column(Integer)
#     orbsDropped = Column(Integer)
#     orbsGathered = Column(Integer)
#     precisionKills = Column(Integer)
#     publicEventsCompleted = Column(Integer)
#     publicEventsJoined = Column(Integer)
#     remainingTimeAfterQuitSeconds = Column(Integer)
#     resurrectionsPerformed = Column(Integer)
#     resurrectionsReceived = Column(Integer)
#     secondsPlayed = Column(Integer)
#     suicides = Column(Integer)
#     totalActivityDurationSeconds = Column(Integer)
#     totalDeathDistance = Column(Integer)
#     totalKillDistance = Column(Integer)
#     weaponBestType = Column(Integer)
#     weaponKillsAutoRifle = Column(Integer)
#     weaponKillsHandCannon = Column(Integer)
#     weaponKillsFusionRifle = Column(Integer)
#     weaponKillsGrenade = Column(Integer)
#     weaponKillsMachinegun = Column(Integer)
#     weaponKillsMelee = Column(Integer)
#     weaponKillsPulseRifle = Column(Integer)
#     weaponKillsRelic = Column(Integer)
#     weaponKillsRocketLauncher = Column(Integer)
#     weaponKillsScoutRifle = Column(Integer)
#     weaponKillsShotgun = Column(Integer)
#     weaponKillsSideArm = Column(Integer)
#     weaponKillsSniper = Column(Integer)
#     weaponKillsSubmachinegun = Column(Integer)
#     weaponKillsSuper = Column(Integer)
#     weaponKillsSword = Column(Integer)
#     winLossRatio = Column(Float)
#     zonesCaptured = Column(Integer)
#     abilityKillspg = Column(Float)
#     assistspg = Column(Float)
#     deathspg = Column(Float)
#     killspg = Column(Float)
#     objectivesCompletedpg = Column(Float)
#     orbsDroppedpg = Column(Float)
#     orbsGatheredpg = Column(Float)
#     precisionKillspg = Column(Float)
#     publicEventsCompletedpg = Column(Float)
#     publicEventsJoinedpg = Column(Float)
#     remainingTimeAfterQuitSecondspg = Column(Float)
#     resurrectionsPerformedpg = Column(Float)
#     resurrectionsReceivedpg = Column(Float)
#     secondsPlayedpg = Column(Float)
#     suicidespg = Column(Float)
#     totalActivityDurationSecondspg = Column(Float)
#     weaponKillsAutoRiflepg = Column(Float)
#     weaponKillsHandCannonpg = Column(Float)
#     weaponKillsFusionRiflepg = Column(Float)
#     weaponKillsGrenadepg = Column(Float)
#     weaponKillsMachinegunpg = Column(Float)
#     weaponKillsMeleepg = Column(Float)
#     weaponKillsPulseRiflepg = Column(Float)
#     weaponKillsRelicpg = Column(Float)
#     weaponKillsRocketLauncherpg = Column(Float)
#     weaponKillsScoutRiflepg = Column(Float)
#     weaponKillsShotgunpg = Column(Float)
#     weaponKillsSideArmpg = Column(Float)
#     weaponKillsSniperpg = Column(Float)
#     weaponKillsSubmachinegunpg = Column(Float)
#     weaponKillsSuperpg = Column(Float)
#     weaponKillsSwordpg = Column(Float)
#     zonesCapturedpg = Column(Float)
#     zonesNeutralizedpg = Column(Float)
#     zonesNeutralized = Column(Integer)

# class PvPAggregate(Base):
#     __tablename__ = 'pvpAggregate'
#     id = Column(Integer, ForeignKey('account.id'), primary_key=True)
#     account = relationship(Account)
#     abilityKills = Column(Integer)
#     activitiesEntered = Column(Integer)
#     activitiesWon = Column(Integer)
#     allParticipantsCount = Column(Integer)
#     allParticipantsScore = Column(Integer)
#     allParticipantsTimePlayed = Column(Integer)
#     assists = Column(Integer)
#     averageKillDistance = Column(Float)
#     averageLifespan = Column(Float)
#     averageDeathDistance = Column(Float)
#     averageScorePerKill = Column(Float)
#     averageScorePerLife = Column(Float)
#     bestSingleGameKills = Column(Integer)
#     bestSingleGameScore = Column(Integer)
#     closeCalls = Column(Integer)
#     combatRating = Column(Float)
#     deaths = Column(Integer)
#     defensiveKills = Column(Integer)
#     dominationKills = Column(Integer)
#     highestCharacterLevel = Column(Integer)
#     highestLightLevel = Column(Integer)
#     kills = Column(Integer)
#     killsDeathsAssists = Column(Float)
#     killsDeathsRatio = Column(Float)
#     longestKillDistance = Column(Integer)
#     longestKillSpree = Column(Integer)
#     longestSingleLife = Column(Integer)
#     mostPrecisionKills = Column(Integer)
#     objectivesCompleted = Column(Integer)
#     offensiveKills = Column(Integer)
#     orbsDropped = Column(Integer)
#     orbsGathered = Column(Integer)
#     precisionKills = Column(Integer)
#     relicsCaptured = Column(Integer)
#     remainingTimeAfterQuitSeconds = Column(Integer)
#     resurrectionsPerformed = Column(Integer)
#     resurrectionsReceived = Column(Integer)
#     score = Column(Integer)
#     secondsPlayed = Column(Integer)
#     suicides = Column(Integer)
#     teamScore = Column(Integer)
#     totalActivityDurationSeconds = Column(Integer)
#     totalDeathDistance = Column(Integer)
#     totalKillDistance = Column(Integer)
#     weaponBestType = Column(Integer)
#     weaponKillsAutoRifle = Column(Integer)
#     weaponKillsHandCannon = Column(Integer)
#     weaponKillsFusionRifle = Column(Integer)
#     weaponKillsGrenade = Column(Integer)
#     weaponKillsMachinegun = Column(Integer)
#     weaponKillsMelee = Column(Integer)
#     weaponKillsPulseRifle = Column(Integer)
#     weaponKillsRelic = Column(Integer)
#     weaponKillsRocketLauncher = Column(Integer)
#     weaponKillsScoutRifle = Column(Integer)
#     weaponKillsShotgun = Column(Integer)
#     weaponKillsSideArm = Column(Integer)
#     weaponKillsSniper = Column(Integer)
#     weaponKillsSubmachinegun = Column(Integer)
#     weaponKillsSuper = Column(Integer)
#     weaponKillsSword = Column(Integer)
#     winLossRatio = Column(Float)
#     zonesCaptured = Column(Integer)
#     zonesNeutralized = Column(Integer)
#     abilityKillspg = Column(Float)
#     assistspg = Column(Float)
#     closeCallspg = Column(Float)
#     deathspg = Column(Float)
#     dominationKillspg = Column(Float)
#     killspg = Column(Float)
#     objectivesCompletedpg = Column(Float)
#     offensiveKillspg = Column(Float)
#     orbsDroppedpg = Column(Float)
#     orbsGatheredpg = Column(Float)
#     precisionKillspg = Column(Float)
#     relicsCapturedpg = Column(Float)
#     remainingTimeAfterQuitSecondspg = Column(Float)
#     resurrectionsPerformedpg = Column(Float)
#     resurrectionsReceivedpg = Column(Float)
#     scorepg = Column(Float)
#     secondsPlayedpg = Column(Float)
#     suicidespg = Column(Float)
#     teamScorepg = Column(Float)
#     totalActivityDurationSecondspg = Column(Float)
#     weaponKillsAutoRiflepg = Column(Float)
#     weaponKillsHandCannonpg = Column(Float)
#     weaponKillsFusionRiflepg = Column(Float)
#     weaponKillsGrenadepg = Column(Float)
#     weaponKillsMachinegunpg = Column(Float)
#     weaponKillsMeleepg = Column(Float)
#     weaponKillsPulseRiflepg = Column(Float)
#     weaponKillsRelicpg = Column(Float)
#     weaponKillsRocketLauncherpg = Column(Float)
#     weaponKillsScoutRiflepg = Column(Float)
#     weaponKillsShotgunpg = Column(Float)
#     weaponKillsSideArmpg = Column(Float)
#     weaponKillsSniperpg = Column(Float)
#     weaponKillsSubmachinegunpg = Column(Float)
#     weaponKillsSuperpg = Column(Float)
#     weaponKillsSwordpg = Column(Float)
#     zonesCapturedpg = Column(Float)
#     zonesNeutralizedpg = Column(Float)

# class AccountWeaponUsage(Base):
#     __tablename__ = 'accountWeaponUsage'
#     id = Column(Integer, ForeignKey('account.id'), primary_key=True) 
#     account = relationship(Account)
#     weaponHash = Column(Integer, primary_key=True)
#     kills = Column(Integer)
#     precision_kills = Column(Integer)
#     precision_kill_percentage = Column(Float)

# class CharacterActivityStats(Base):
#     __tablename__ = 'characterActivityStats'
#     id = Column(Integer, ForeignKey('character.id'), primary_key=True)
#     character = relationship(Character)
#     activityHash = Column(Integer, primary_key=True)
#     activityAssists = Column(Integer)
#     activityCompletions = Column(Integer)
#     activityDeaths = Column(Integer)
#     activityGatesHit = Column(Integer)
#     activityKills = Column(Integer)
#     activityKillsDeathsAssists = Column(Float)
#     activityKillsDeathsRatio = Column(Float)
#     activityPrecisionKills = Column(Integer)
#     activitySecondsPlayed = Column(Integer)
#     activityWins = Column(Integer)
#     fastestCompletionSecondsForActivity = Column(Integer)

# class AccountMedals(Base):
#     __tablename__ = 'accountMedals'
#     id = Column(Integer, ForeignKey('account.id'), primary_key=True)
#     account = relationship(Account)
#     activitiesEntered = Column(Integer)
#     allMedalsEarned = Column(Integer)
#     allMedalsScore = Column(Integer)
#     medalsAbilityArcLightningKillMulti = Column(Integer)
#     medalsAbilityGhostGunKillMulti = Column(Integer)
#     medalsAbilityHavocKillMulti = Column(Integer)
#     medalsAbilityNovaBombKillMulti = Column(Integer)
#     medalsAbilityRadianceGrenadeKillMulti = Column(Integer)
#     medalsAbilityShadowStrikeKillMulti = Column(Integer)
#     medalsAbilityThermalHammerKillMulti = Column(Integer)
#     medalsAbilityVoidBowKillMulti = Column(Integer)
#     medalsAbilityWardDeflect = Column(Integer)
#     medalsActivityCompleteControlMostCaptures = Column(Integer)
#     medalsActivityCompleteCycle = Column(Integer)
#     medalsActivityCompleteDeathless = Column(Integer)
#     medalsActivityCompleteHighestScoreLosing = Column(Integer)
#     medalsActivityCompleteHighestScoreWinning = Column(Integer)
#     medalsActivityCompleteLonewolf = Column(Integer)
#     medalsActivityCompleteSalvageMostCancels = Column(Integer)
#     medalsActivityCompleteSalvageShutout = Column(Integer)
#     medalsActivityCompleteSingularityPerfectRunner = Column(Integer)
#     medalsActivityCompleteVictoryBlowout = Column(Integer)
#     medalsActivityCompleteVictory = Column(Integer)
#     medalsActivityCompleteVictoryElimination = Column(Integer)
#     medalsActivityCompleteVictoryEliminationPerfect = Column(Integer)
#     medalsActivityCompleteVictoryEliminationShutout = Column(Integer)
#     medalsActivityCompleteVictoryExtraLastSecond = Column(Integer)
#     medalsActivityCompleteVictoryLastSecond = Column(Integer)
#     medalsActivityCompleteVictoryMercy = Column(Integer)
#     medalsActivityCompleteVictoryRumbleBlowout = Column(Integer)
#     medalsActivityCompleteVictoryRumble = Column(Integer)
#     medalsActivityCompleteVictoryRumbleLastSecond = Column(Integer)
#     medalsActivityCompleteVictoryRumbleSuddenDeath = Column(Integer)
#     medalsActivityCompleteVictorySuddenDeath = Column(Integer)
#     medalsAvenger = Column(Integer)
#     medalsBuddyResurrectionMulti = Column(Integer)
#     medalsBuddyResurrectionSpree = Column(Integer)
#     medalsCloseCallTalent = Column(Integer)
#     medalsComebackKill = Column(Integer)
#     medalsDominationKill = Column(Integer)
#     medalsDominionZoneCapturedSpree = Column(Integer)
#     medalsDominionZoneDefenseKillSpree = Column(Integer)
#     medalsDominionZoneOffenseKillSpree = Column(Integer)
#     medalsEliminationLastStandKill = Column(Integer)
#     medalsEliminationLastStandRevive = Column(Integer)
#     medalsEliminationWipeQuick = Column(Integer)
#     medalsEliminationWipeSolo = Column(Integer)
#     medalsFirstBlood = Column(Integer)
#     medalsFirstPlaceKillSpree = Column(Integer)
#     medalsGrenadeKillStick = Column(Integer)
#     medalsHazardKill = Column(Integer)
#     medalsHunterKillInvisible = Column(Integer)
#     medalsKillAssistSpree = Column(Integer)
#     medalsKillAssistSpreeFfa = Column(Integer)
#     medalsKillHeadshot = Column(Integer)
#     medalsKilljoy = Column(Integer)
#     medalsKilljoyMega = Column(Integer)
#     medalsKillMulti2 = Column(Integer)
#     medalsKillMulti3 = Column(Integer)
#     medalsKillMulti4 = Column(Integer)
#     medalsKillMulti5 = Column(Integer)
#     medalsKillMulti6 = Column(Integer)
#     medalsKillMulti7 = Column(Integer)
#     medalsKillPostmortem = Column(Integer)
#     medalsKillSpree1 = Column(Integer)
#     medalsKillSpree2 = Column(Integer)
#     medalsKillSpree3 = Column(Integer)
#     medalsKillSpreeAbsurd = Column(Integer)
#     medalsKillSpreeNoDamage = Column(Integer)
#     medalsMeleeKillHunterThrowingKnifeHeadshot = Column(Integer)
#     medalsPaybackKill = Column(Integer)
#     medalsRadianceShutdown = Column(Integer)
#     medalsRescue = Column(Integer)
#     medalsSalvageProbeCanceled = Column(Integer)
#     medalsSalvageProbeCompleteSpree = Column(Integer)
#     medalsSalvageProbeDefenseKill = Column(Integer)
#     medalsSalvageProbeOffenseKillMulti = Column(Integer)
#     medalsSalvageZoneCapturedSpree = Column(Integer)
#     medalsSingularityFlagCaptureMulti = Column(Integer)
#     medalsSingularityFlagHolderKilledClose = Column(Integer)
#     medalsSingularityFlagHolderKilledMulti = Column(Integer)
#     medalsSingularityRunnerDefenseMulti = Column(Integer)
#     medalsSupremacy = Column(Integer)
#     medalsSupremacyConfirmStreakLarge = Column(Integer)
#     medalsSupremacyDenyMulti = Column(Integer)
#     medalsSupremacyMostConfirms = Column(Integer)
#     medalsSupremacyMostDenies = Column(Integer)
#     medalsSupremacyMostSelfConfirms = Column(Integer)
#     medalsSupremacyMulti = Column(Integer)
#     medalsSupremacyNeverCollected = Column(Integer)
#     medalsSupremacySelfDeny = Column(Integer)
#     medalsTeamDominationHold1m = Column(Integer)
#     medalsTeamKillSpree = Column(Integer)
#     medalsUnknown = Column(Integer)
#     medalsVehicleFotcTurretKillSpree = Column(Integer)
#     medalsVehicleInterceptorKillSplatter = Column(Integer)
#     medalsVehicleInterceptorKillSpree = Column(Integer)
#     medalsVehiclePikeKillSplatter = Column(Integer)
#     medalsVehiclePikeKillSpree = Column(Integer)
#     medalsVehicleSparrowKillSplatter = Column(Integer)
#     medalsWeaponAutoRifleKillSpree = Column(Integer)
#     medalsWeaponFusionRifleKillSpree = Column(Integer)
#     medalsWeaponHandCannonHeadshotSpree = Column(Integer)
#     medalsWeaponMachineGunKillSpree = Column(Integer)
#     medalsWeaponPulseRifleKillSpree = Column(Integer)
#     medalsWeaponRocketLauncherKillSpree = Column(Integer)
#     medalsWeaponScoutRifleKillSpree = Column(Integer)
#     medalsWeaponShotgunKillSpree = Column(Integer)
#     medalsWeaponSidearmKillSpree = Column(Integer)
#     medalsWeaponSniperRifleHeadshotSpree = Column(Integer)
#     medalsWeaponSwordKillSpree = Column(Integer)
#     medalsWinningScore = Column(Integer)
#     medalsZoneCapturedBInitial = Column(Integer)

# class AccountActivityModeStats(Base):
#     __tablename__ = "accountActivityModeStats"
#     id = Column(Integer, ForeignKey('account.id'), primary_key=True)
#     account = relationship(Account)
#     mode = Column(String, primary_key=True)
#     abilityKills = Column(Integer)
#     activitiesCleared = Column(Integer)
#     activitiesEntered = Column(Integer)
#     activitiesWon = Column(Integer)
#     activityDuration = Column(Integer)
#     allParticipantsCount = Column(Integer)
#     allParticipantsScore = Column(Integer)
#     allParticipantsTimePlayed = Column(Integer)
#     assists = Column(Integer)
#     averageDeathDistance = Column(Float)
#     averageKillDistance = Column(Float)
#     averageLifespan = Column(Float)
#     averageScorePerKill = Column(Float)
#     averageScorePerLife = Column(Float)
#     bestSingleGameKills = Column(Integer)
#     bestSingleGameScore = Column(Integer)
#     capturedYourOwnKill = Column(Integer)
#     carrierKills = Column(Integer)
#     closeCalls = Column(Integer)
#     combatRating = Column(Float)
#     completionReason = Column(Integer)
#     courtOfOryxAttempts = Column(Integer)
#     courtOfOryxCompletions = Column(Integer)
#     courtOfOryxWinsTier1 = Column(Integer)
#     courtOfOryxWinsTier2 = Column(Integer)
#     courtOfOryxWinsTier3 = Column(Integer)
#     dailyMedalsEarned = Column(Integer)
#     deaths = Column(Integer)
#     defensiveKills = Column(Integer)
#     dominationKills = Column(Integer)
#     dunkKills = Column(Integer)
#     fastestCompletion = Column(Integer)
#     fireTeamId = Column(Integer)
#     gatesHit = Column(Integer)
#     highestCharacterLevel = Column(Integer)
#     highestLightLevel = Column(Integer)
#     highestSandboxLevel = Column(Integer)
#     kills = Column(Integer)
#     killsDeathsAssists = Column(Float)
#     killsDeathsRatio = Column(Float)
#     longestKillDistance = Column(Integer)
#     longestKillSpree = Column(Integer)
#     longestSingleLife = Column(Integer)
#     lostTagToOpponent = Column(Integer)
#     mostPrecisionKills = Column(Integer)
#     objectivesCompleted = Column(Integer)
#     offensiveKills = Column(Integer)
#     orbsDropped = Column(Integer)
#     orbsGathered = Column(Integer)
#     playerCount = Column(Integer)
#     precisionKills = Column(Integer)
#     publicEventsCompleted = Column(Integer)
#     publicEventsJoined = Column(Integer)
#     raceCompletionMilliseconds = Column(Integer)
#     raceCompletionSeconds = Column(Integer)
#     recoveredOwnDeadTag = Column(Integer)
#     recoveredTeammateTags = Column(Integer)
#     relicsCaptured = Column(Integer)
#     remainingTimeAfterQuitSeconds = Column(Integer)
#     resurrectionsPerformed = Column(Integer)
#     resurrectionsReceived = Column(Integer)
#     score = Column(Integer)
#     secondsPlayed = Column(Integer)
#     slamDunks = Column(Integer)
#     sparksCaptured = Column(Integer)
#     standing = Column(Integer)
#     styleDunks = Column(Integer)
#     suicides = Column(Integer)
#     tagCaptures = Column(Integer)
#     tagsCapturedPerTagLost = Column(Float)
#     team = Column(Integer)
#     teamScore = Column(Integer)
#     totalActivityDurationSeconds = Column(Integer)
#     totalDeathDistance = Column(Integer)
#     totalKillDistance = Column(Integer)
#     weaponBestType = Column(Integer)
#     weaponKillsAutoRifle = Column(Integer)
#     weaponKillsHandCannon = Column(Integer)
#     weaponKillsFusionRifle = Column(Integer)
#     weaponKillsGrenade = Column(Integer)
#     weaponKillsMachinegun = Column(Integer)
#     weaponKillsMelee = Column(Integer)
#     weaponKillsPulseRifle = Column(Integer)
#     weaponKillsRelic = Column(Integer)
#     weaponKillsRocketLauncher = Column(Integer)
#     weaponKillsScoutRifle = Column(Integer)
#     weaponKillsShotgun = Column(Integer)
#     weaponKillsSideArm = Column(Integer)
#     weaponKillsSniper = Column(Integer)
#     weaponKillsSubmachinegun = Column(Integer)
#     weaponKillsSuper = Column(Integer)
#     weaponKillsSword = Column(Integer)
#     winLossRatio = Column(Float)
#     zonesCaptured = Column(Integer)
#     zonesNeutralized = Column(Integer)

# class ActivityReference(Base):
#     __tablename__ = 'activityReference'
#     id = Column(Integer, primary_key=True)
#     activity_name = Column(String(50))
#     activity_type_hash = Column(String(50))

# class ActivityTypeReference(Base):
#     __tablename__ = 'activityTypeReference'
#     id = Column(Integer, primary_key=True)
#     activity_type_name = Column(String(50))
    
# class ClassReference(Base):
#     __tablename__ = 'classReference'
#     id = Column(Integer, primary_key=True)
#     class_name = Column(String(50))

# class WeaponReference(Base):
#     __tablename__ = 'weaponReference'
#     id = Column(Integer, primary_key=True)
#     weapon_name = Column(String(50))
#     weapon_type = Column(String(50))
#     weapon_rarity = Column(String(50))

# class BucketReference(Base):
#     __tablename__ = 'bucketReference'
#     id = Column(Integer, primary_key=True)
#     bucket_name = Column(String(50))

# # I will not be including single game tracking for a while, probably. Maybe when D2 gets started I'll ramp it up, but we're going to need some more storage space.
# #class Activity(Base):
# #    __tablename__ = 'activity'
# #    instance_id = Column(Integer, primary_key=True)
# #    activity_id = Column(Integer, ForeignKey('activityReference.activity_id'))
# #    activityReference = relationship(ActivityReference)
# #    reference_id = Column(Integer)
# #    #Other activity-specific fields

# #class CharacterPlaysActivity(Base):
# #    __tablename__ = 'characterPlaysActivity'
# #    character_id = Column(Integer, ForeignKey('character.id'), primary_key=True)
# #    character = relationship(Character)
# #    instance_id = Column(Integer, ForeignKey('activity.instance_id'), primary_key=True)
# #    activity = relationship(Activity)
# #    #Other character-specific activity related fields

class LastUpdated(Base):
    __tablename__ = 'lastUpdated'
    id = Column(Integer, primary_key=True)
    table_name = Column(String(50), primary_key=True)
    last_updated = Column(DateTime)

def init_db(engine):
    Base.metadata.bind = engine
    Base.metadata.create_all(engine)

if __name__ == "__main__":
    # loadConfig for testing purposes
    load_config()
    init_db(engine)
