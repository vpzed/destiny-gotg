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
    total_minutes_played = Column(Integer)
    max_light = Column(Integer)
    most_recently_played = Column(DateTime)

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

class TotalStats(object):
    mode = Column(String, primary_key=True)
    abilityKills = Column(Integer)
    activitiesCleared = Column(Integer)
    activitiesEntered = Column(Integer)
    activitiesWon = Column(Integer)
    adventuresCompleted = Column(Integer)
    allParticipantsCount = Column(Integer)
    allParticipantsScore = Column(Integer)
    allParticipantsTimePlayed = Column(Integer)
    assists = Column(Integer)
    averageDeathDistance = Column(Float)
    averageKillDistance = Column(Float)
    averageLifespan = Column(Float)
    averageScorePerKill = Column(Float)
    averageScorePerLife = Column(Float)
    bestSingleGameKills = Column(Integer)
    bestSingleGameScore = Column(Integer)
    combatRating = Column(Float)
    deaths = Column(Integer)
    fastestCompletionMs = Column(Integer)
    heroicPublicEventsCompleted = Column(Integer)
    highestCharacterLevel = Column(Integer)
    highestLightLevel = Column(Integer)
    kills = Column(Integer)
    killsDeathsAssists = Column(Float)
    killsDeathsRatio = Column(Float)
    longestKillDistance = Column(Integer)
    longestKillSpree = Column(Integer)
    longestSingleLife = Column(Integer)
    mostPrecisionKills = Column(Integer)
    objectivesCompleted = Column(Integer)
    orbsDropped = Column(Integer)
    orbsGathered = Column(Integer)
    publicEventsCompleted = Column(Integer)
    publicEventsJoined = Column(Integer)
    precisionKills = Column(Integer)
    remainingTimeAfterQuitSeconds = Column(Integer)
    resurrectionsPerformed = Column(Integer)
    resurrectionsReceived = Column(Integer)
    score = Column(Integer)
    secondsPlayed = Column(Integer)
    suicides = Column(Integer)
    teamScore = Column(Integer)
    totalActivityDurationSeconds = Column(Integer)
    totalDeathDistance = Column(Integer)
    totalKillDistance = Column(Integer)
    weaponBestType = Column(Integer)
    weaponKillsAbility = Column(Integer)
    weaponKillsAutoRifle = Column(Integer)
    weaponKillsFusionRifle = Column(Integer)
    weaponKillsGrenade = Column(Integer)
    weaponKillsGrenadeLauncher = Column(Integer)
    weaponKillsHandCannon = Column(Integer)
    weaponKillsMachinegun = Column(Integer)
    weaponKillsMelee = Column(Integer)
    weaponKillsPulseRifle = Column(Integer)
    weaponKillsRelic = Column(Integer)
    weaponKillsRocketLauncher = Column(Integer)
    weaponKillsScoutRifle = Column(Integer)
    weaponKillsShotgun = Column(Integer)
    weaponKillsSideArm = Column(Integer)
    weaponKillsSniper = Column(Integer)
    weaponKillsSubmachinegun = Column(Integer)
    weaponKillsSuper = Column(Integer)
    weaponKillsSword = Column(Integer)
    winLossRatio = Column(Integer)
    zonesCaptured = Column(Integer)
    zonesNeutralized = Column(Integer)
    abilityKillspg = Column(Float)
    assistspg = Column(Float)
    deathspg = Column(Float)
    killspg = Column(Float)
    objectivesCompletedpg = Column(Float)
    orbsDroppedpg = Column(Float)
    orbsGatheredpg = Column(Float)
    precisionKillspg = Column(Float)
    publicEventsCompletedpg = Column(Float)
    publicEventsJoinedpg = Column(Float)
    remainingTimeAfterQuitSecondspg = Column(Float)
    resurrectionsPerformedpg = Column(Float)
    resurrectionsReceivedpg = Column(Float)
    scorepg = Column(Float)
    secondsPlayedpg = Column(Float)
    suicidespg = Column(Float)
    teamScorepg = Column(Float)
    totalActivityDurationSecondspg = Column(Float)
    weaponKillsAutoRiflepg = Column(Float)
    weaponKillsHandCannonpg = Column(Float)
    weaponKillsFusionRiflepg = Column(Float)
    weaponKillsGrenadepg = Column(Float)
    weaponKillsGrenadeLauncherpg = Column(Float)
    weaponKillsMachinegunpg = Column(Float)
    weaponKillsMeleepg = Column(Float)
    weaponKillsPulseRiflepg = Column(Float)
    weaponKillsRelicpg = Column(Float)
    weaponKillsRocketLauncherpg = Column(Float)
    weaponKillsScoutRiflepg = Column(Float)
    weaponKillsShotgunpg = Column(Float)
    weaponKillsSideArmpg = Column(Float)
    weaponKillsSniperpg = Column(Float)
    weaponKillsSubmachinegunpg = Column(Float)
    weaponKillsSuperpg = Column(Float)
    weaponKillsSwordpg = Column(Float)
    zonesCapturedpg = Column(Float)
    zonesNeutralizedpg = Column(Float)

class WeaponStats(object):
    mode = Column(String, primary_key=True)
    activitiesEntered = Column(Integer)
    weaponKillsAbility = Column(Integer)
    weaponKillsAutoRifle = Column(Integer)
    weaponKillsFusionRifle = Column(Integer)
    weaponKillsGrenade = Column(Integer)
    weaponKillsGrenadeLauncher = Column(Integer)
    weaponKillsHandCannon = Column(Integer)
    weaponKillsMachinegun = Column(Integer)
    weaponKillsMelee = Column(Integer)
    weaponKillsPrecisionKillsAutoRifle = Column(Float)
    weaponKillsPrecisionKillsFusionRifle = Column(Float)
    weaponKillsPrecisionKillsGrenade = Column(Float)
    weaponKillsPrecisionKillsGrenadeLauncher = Column(Float)
    weaponKillsPrecisionKillsHandCannon = Column(Float)
    weaponKillsPrecisionKillsMachinegun = Column(Float)
    weaponKillsPrecisionKillsMelee = Column(Float)
    weaponKillsPrecisionKillsPulseRifle = Column(Float)
    weaponKillsPrecisionKillsRelic = Column(Float)
    weaponKillsPrecisionKillsRocketLauncher = Column(Float)
    weaponKillsPrecisionKillsScoutRifle = Column(Float)
    weaponKillsPrecisionKillsShotgun = Column(Float)
    weaponKillsPrecisionKillsSideArm = Column(Float)
    weaponKillsPrecisionKillsSniper = Column(Float)
    weaponKillsPrecisionKillsSubmachinegun = Column(Float)
    weaponKillsPrecisionKillsSuper = Column(Float)
    weaponKillsPulseRifle = Column(Integer)
    weaponKillsRelic = Column(Integer)
    weaponKillsRocketLauncher = Column(Integer)
    weaponKillsScoutRifle = Column(Integer)
    weaponKillsShotgun = Column(Integer)
    weaponKillsSideArm = Column(Integer)
    weaponKillsSniper = Column(Integer)
    weaponKillsSubmachinegun = Column(Integer)
    weaponKillsSuper = Column(Integer)
    weaponKillsSword = Column(Integer)
    weaponPrecisionKillsAutoRifle = Column(Integer)
    weaponPrecisionKillsFusionRifle = Column(Integer)
    weaponPrecisionKillsGrenade = Column(Integer)
    weaponPrecisionKillsGrenadeLauncher = Column(Integer)
    weaponPrecisionKillsHandCannon = Column(Integer)
    weaponPrecisionKillsMachinegun = Column(Integer)
    weaponPrecisionKillsMelee = Column(Integer)
    weaponPrecisionKillsPulseRifle = Column(Integer)
    weaponPrecisionKillsRelic = Column(Integer)
    weaponPrecisionKillsRocketLauncher = Column(Integer)
    weaponPrecisionKillsScoutRifle = Column(Integer)
    weaponPrecisionKillsShotgun = Column(Integer)
    weaponPrecisionKillsSideArm = Column(Integer)
    weaponPrecisionKillsSniper = Column(Integer)
    weaponPrecisionKillsSubmachinegun = Column(Integer)
    weaponPrecisionKillsSuper = Column(Integer)
    weaponKillsAbilitypg = Column(Float)
    weaponKillsAutoRiflepg = Column(Float)
    weaponKillsFusionRiflepg = Column(Float)
    weaponKillsGrenadepg = Column(Float)
    weaponKillsGrenadeLauncherpg = Column(Float)
    weaponKillsHandCannonpg = Column(Float)
    weaponKillsMachinegunpg = Column(Float)
    weaponKillsMeleepg = Column(Float)
    weaponKillsPulseRiflepg = Column(Float)
    weaponKillsRelicpg = Column(Float)
    weaponKillsRocketLauncherpg = Column(Float)
    weaponKillsScoutRiflepg = Column(Float)
    weaponKillsShotgunpg = Column(Float)
    weaponKillsSideArmpg = Column(Float)
    weaponKillsSniperpg = Column(Float)
    weaponKillsSubmachinegunpg = Column(Float)
    weaponKillsSuperpg = Column(Float)
    weaponKillsSwordpg = Column(Float)
    weaponPrecisionKillsAutoRiflepg = Column(Float)
    weaponPrecisionKillsFusionRiflepg = Column(Float)
    weaponPrecisionKillsGrenadepg = Column(Float)
    weaponPrecisionKillsGrenadeLauncherpg = Column(Float)
    weaponPrecisionKillsHandCannonpg = Column(Float)
    weaponPrecisionKillsMachinegunpg = Column(Float)
    weaponPrecisionKillsMeleepg = Column(Float)
    weaponPrecisionKillsPulseRiflepg = Column(Float)
    weaponPrecisionKillsRelicpg = Column(Float)
    weaponPrecisionKillsRocketLauncherpg = Column(Float)
    weaponPrecisionKillsScoutRiflepg = Column(Float)
    weaponPrecisionKillsShotgunpg = Column(Float)
    weaponPrecisionKillsSideArmpg = Column(Float)
    weaponPrecisionKillsSniperpg = Column(Float)
    weaponPrecisionKillsSubmachinegunpg = Column(Float)
    weaponPrecisionKillsSuperpg = Column(Float)

class MedalStats(object):
    activitiesEntered = Column(Integer)
    allMedalsEarned = Column(Integer)
    allMedalsScore = Column(Integer)
    medalsAbilityArcLightningKillMulti = Column(Integer)
    medalsAbilityGhostGunKillMulti = Column(Integer)
    medalsAbilityHavocKillMulti = Column(Integer)
    medalsAbilityNovaBombKillMulti = Column(Integer)
    medalsAbilityRadianceGrenadeKillMulti = Column(Integer)
    medalsAbilityShadowStrikeKillMulti = Column(Integer)
    medalsAbilityThermalHammerKillMulti = Column(Integer)
    medalsAbilityVoidBowKillMulti = Column(Integer)
    medalsAbilityWardDeflect = Column(Integer)
    medalsActivityCompleteControlMostCaptures = Column(Integer)
    medalsActivityCompleteCycle = Column(Integer)
    medalsActivityCompleteDeathless = Column(Integer)
    medalsActivityCompleteHighestScoreLosing = Column(Integer)
    medalsActivityCompleteHighestScoreWinning = Column(Integer)
    medalsActivityCompleteLonewolf = Column(Integer)
    medalsActivityCompleteSalvageMostCancels = Column(Integer)
    medalsActivityCompleteSalvageShutout = Column(Integer)
    medalsActivityCompleteSingularityPerfectRunner = Column(Integer)
    medalsActivityCompleteVictoryBlowout = Column(Integer)
    medalsActivityCompleteVictory = Column(Integer)
    medalsActivityCompleteVictoryElimination = Column(Integer)
    medalsActivityCompleteVictoryEliminationPerfect = Column(Integer)
    medalsActivityCompleteVictoryEliminationShutout = Column(Integer)
    medalsActivityCompleteVictoryExtraLastSecond = Column(Integer)
    medalsActivityCompleteVictoryLastSecond = Column(Integer)
    medalsActivityCompleteVictoryMercy = Column(Integer)
    medalsActivityCompleteVictoryRumbleBlowout = Column(Integer)
    medalsActivityCompleteVictoryRumble = Column(Integer)
    medalsActivityCompleteVictoryRumbleLastSecond = Column(Integer)
    medalsActivityCompleteVictoryRumbleSuddenDeath = Column(Integer)
    medalsActivityCompleteVictorySuddenDeath = Column(Integer)
    medalsAvenger = Column(Integer)
    medalsBuddyResurrectionMulti = Column(Integer)
    medalsBuddyResurrectionSpree = Column(Integer)
    medalsCloseCallTalent = Column(Integer)
    medalsComebackKill = Column(Integer)
    medalsDominationKill = Column(Integer)
    medalsDominionZoneCapturedSpree = Column(Integer)
    medalsDominionZoneDefenseKillSpree = Column(Integer)
    medalsDominionZoneOffenseKillSpree = Column(Integer)
    medalsEliminationLastStandKill = Column(Integer)
    medalsEliminationLastStandRevive = Column(Integer)
    medalsEliminationWipeQuick = Column(Integer)
    medalsEliminationWipeSolo = Column(Integer)
    medalsFirstBlood = Column(Integer)
    medalsFirstPlaceKillSpree = Column(Integer)
    medalsGrenadeKillStick = Column(Integer)
    medalsHazardKill = Column(Integer)
    medalsHunterKillInvisible = Column(Integer)
    medalsKillAssistSpree = Column(Integer)
    medalsKillAssistSpreeFfa = Column(Integer)
    medalsKillHeadshot = Column(Integer)
    medalsKilljoy = Column(Integer)
    medalsKilljoyMega = Column(Integer)
    medalsKillMulti2 = Column(Integer)
    medalsKillMulti3 = Column(Integer)
    medalsKillMulti4 = Column(Integer)
    medalsKillMulti5 = Column(Integer)
    medalsKillMulti6 = Column(Integer)
    medalsKillMulti7 = Column(Integer)
    medalsKillPostmortem = Column(Integer)
    medalsKillSpree1 = Column(Integer)
    medalsKillSpree2 = Column(Integer)
    medalsKillSpree3 = Column(Integer)
    medalsKillSpreeAbsurd = Column(Integer)
    medalsKillSpreeNoDamage = Column(Integer)
    medalsMeleeKillHunterThrowingKnifeHeadshot = Column(Integer)
    medalsPaybackKill = Column(Integer)
    medalsRadianceShutdown = Column(Integer)
    medalsRescue = Column(Integer)
    medalsSalvageProbeCanceled = Column(Integer)
    medalsSalvageProbeCompleteSpree = Column(Integer)
    medalsSalvageProbeDefenseKill = Column(Integer)
    medalsSalvageProbeOffenseKillMulti = Column(Integer)
    medalsSalvageZoneCapturedSpree = Column(Integer)
    medalsSingularityFlagCaptureMulti = Column(Integer)
    medalsSingularityFlagHolderKilledClose = Column(Integer)
    medalsSingularityFlagHolderKilledMulti = Column(Integer)
    medalsSingularityRunnerDefenseMulti = Column(Integer)
    medalsSupremacy = Column(Integer)
    medalsSupremacyConfirmStreakLarge = Column(Integer)
    medalsSupremacyDenyMulti = Column(Integer)
    medalsSupremacyMostConfirms = Column(Integer)
    medalsSupremacyMostDenies = Column(Integer)
    medalsSupremacyMostSelfConfirms = Column(Integer)
    medalsSupremacyMulti = Column(Integer)
    medalsSupremacyNeverCollected = Column(Integer)
    medalsSupremacySelfDeny = Column(Integer)
    medalsTeamDominationHold1m = Column(Integer)
    medalsTeamKillSpree = Column(Integer)
    medalsUnknown = Column(Integer)
    medalsVehicleFotcTurretKillSpree = Column(Integer)
    medalsVehicleInterceptorKillSplatter = Column(Integer)
    medalsVehicleInterceptorKillSpree = Column(Integer)
    medalsVehiclePikeKillSplatter = Column(Integer)
    medalsVehiclePikeKillSpree = Column(Integer)
    medalsVehicleSparrowKillSplatter = Column(Integer)
    medalsWeaponAutoRifleKillSpree = Column(Integer)
    medalsWeaponFusionRifleKillSpree = Column(Integer)
    medalsWeaponHandCannonHeadshotSpree = Column(Integer)
    medalsWeaponMachineGunKillSpree = Column(Integer)
    medalsWeaponPulseRifleKillSpree = Column(Integer)
    medalsWeaponRocketLauncherKillSpree = Column(Integer)
    medalsWeaponScoutRifleKillSpree = Column(Integer)
    medalsWeaponShotgunKillSpree = Column(Integer)
    medalsWeaponSidearmKillSpree = Column(Integer)
    medalsWeaponSniperRifleHeadshotSpree = Column(Integer)
    medalsWeaponSwordKillSpree = Column(Integer)
    medalsWinningScore = Column(Integer)
    medalsZoneCapturedBInitial = Column(Integer)

class AccountTotalStats(TotalStats, Base):
    __tablename__ = "accountTotalStats"
    id = Column(Integer, ForeignKey('account.id'), primary_key=True)
    account = relationship(Account)

class CharacterTotalStats(TotalStats, Base):
    __tablename__ = "characterTotalStats"
    id = Column(Integer, ForeignKey('character.id'), primary_key=True)
    character = relationship(Character)

class AccountWeaponStats(WeaponStats, Base):
    __tablename__ = "accountWeaponStats"
    id = Column(Integer, ForeignKey('account.id'), primary_key=True)
    account = relationship(Account)

class CharacterWeaponStats(WeaponStats, Base):
    __tablename__ = "characterWeaponStats"
    id = Column(Integer, ForeignKey('character.id'), primary_key=True)
    character = relationship(Character)

class AccountExoticWeaponStats(WeaponStats, Base):
    __tablename__ = "accountExoticWeaponStats"
    id = Column(Integer, ForeignKey('account.id'), primary_key=True)
    account = relationship(Account)

class CharacterExoticWeaponStats(WeaponStats, Base):
    __tablename__ = "characterExoticWeaponStats"
    id = Column(Integer, ForeignKey('character.id'), primary_key=True)
    character = relationship(Character)

class AccountMedalStats(MedalStats, Base):
    __tablename__ = "accountMedalStats"
    id = Column(Integer, ForeignKey('account.id'), primary_key=True)
    account = relationship(Account)

class CharacterMedalStats(MedalStats, Base):
    __tablename__ = "characterMedalStats"
    id = Column(Integer, ForeignKey('character.id'), primary_key=True)
    character = relationship(Character)

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
