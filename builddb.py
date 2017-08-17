#!/usr/bin/python
#This file (with update option set) is run daily; it pulls new clan members and new accounts. For existing members, it adds newly created characters, and updates all existing stats.
#Perhaps most importantly, it pulls in new activities completed by all members.
import os, sys
import json, requests
import sqlite3
from datetime import datetime
from sqlalchemy import exists, and_
from sqlalchemy.sql.expression import literal_column
from initdb import Base, Bungie, Account, PvPTotal, PvPAverage, PvETotal, PvEAverage, Character, CharacterUsesWeapon, AggregateStatsCharacter, MedalsCharacter, ActivityReference, ClassReference, WeaponReference, ActivityTypeReference, BucketReference, CharacterStatMayhemClash, LastUpdated
from destinygotg import Session, loadConfig

URL_START = "https://bungie.net/Platform"
#URL_START = "https://bungie.net/D1/Platform"
UPDATE_DIFF = 1 # Number of days between updates

def makeHeader():
    return {'X-API-KEY':os.environ['BUNGIE_APIKEY']}

def buildDB():
    """Main function to build the full database"""
    handleBungieUsers()
    handleDestinyUsers()
    #handleAggregateStats(session)
    #handleCharacters(session)
    #handleAggregateActivities(session)
    #handleMedals(session)
    #handleWeaponUsage(session)
    #handleActivityHistory(session)
    #handleReferenceTables(session)

def handleBungieUsers():
    session = Session()
    currentPage = 1
    clan_url = f"{URL_START}/Group/{os.environ['BUNGIE_CLANID']}/ClanMembers/?currentPage={currentPage}&platformType=2"
    outFile = f"clanUser_p{currentPage}.json"
    message = f"Fetching page {currentPage} of clan users."
    iterator = ['Response', 'results']
    infoMap = {'values' :{'id':[['bungieNetUserInfo', 'membershipId'], ['membershipId']]
                         ,'bungie_name':[['bungieNetUserInfo', 'displayName'], ['destinyUserInfo','displayName']]
                         ,'membership_type':[['bungieNetUserInfo', 'membershipType'], ['destinyUserInfo', 'membershipType']]}}
    instrument = ['Response', 'hasMore']
    output = requestAndInsert(session, infoMap, clan_url, outFile, message, iterator, Bungie, instrument)
    while output is True:
        currentPage += 1
        clan_url = f"{URL_START}/Group/{os.environ['BUNGIE_CLANID']}/ClanMembers/?currentPage={currentPage}&platformType=2"
        outFile = f"clanUser_p{currentPage}.json"
        message = f"Fetching page {currentPage} of clan users."
        output = requestAndInsert(session, infoMap, clan_url, outFile, message, iterator, Bungie, instrument)

def dynamicDictIndex(dct, value):
    try:
        ret = dct
        for item in value:
            ret = ret[item]
    except KeyError:
        ret = None
    return ret

def buildDict(dct, valueMap):
    outDict = {}
    for (key, valList) in valueMap.items():
        ret = dynamicDictIndex(dct, valList[0])
        if ret == None:
            ret = dynamicDictIndex(dct, valList[1])
        outDict[key] = ret
    return outDict

#infoMap = {'attrs':{'attr1':'attr1Name', ...}
#           ,'kwargs':{'kwargs1':'attr1', ...}
#           ,'values':{'value1':'location1', ...}
#           ,'statics':{'static1':'attr1', ...}

def requestAndInsert(session, infoMap, url, outFile, message, iterator, table, instrument=None):
    """Documentation of function"""
    data = jsonRequest(url, outFile, message)
    if data is None:
        print("No data retrieved.")
        return None
    group = dynamicDictIndex(data, iterator)
    for elem in group:
        insertDict = buildDict(elem, infoMap['values'])
        if 'statics' in infoMap:
            for (key, value) in infoMap['statics']:
                insertDict[key] = infoMap['attrs'][value]
        insert_elem = table(**insertDict)
        insertOrUpdate(table, insert_elem, session)
    if instrument is not None:
        output = dynamicDictIndex(data, instrument)
        return output

def multiRequestAndInsert(session, elems, infoMap, url, outFile, message, iterator, table, instrument=None):
    for elem in elems:
        attrMap = {}
        for (key, value) in infoMap['attrs']:
            attrMap[key] = getattr(elem, value)
        kwargs = {}
        for (key, value) in infoMap['kwargs']:
            kwargs[key] = attrMap[value]
        if not needsUpdate(table, kwargs, session):
            print(f"Not updating {table} table for user: {queriedMap['name']}")
            continue
        requestAndInsert(session, infoMap, url, outFile, message, iterator, table, instrument)

def handleDestinyUsers():
    """Retrieve JSONs for users, listing their Destiny accounts. Builds account table."""
    session = Session()
    elems = session.query(Bungie).all()
    infoMap = {'attrs'  :{'id'             : 'id'
                         ,'name'           : 'bungie_name'
                         ,'membershipType' : 'membership_type'}
              ,'kwargs' :{'bungie_id' : 'id'}
              ,'values' :{'id'              : [['membershipId']]
                         ,'membership_type' : [['membershipType']]
                         ,'display_name'    : [['displayName']]}
              ,'statics' :{'bungie_id' : 'id'}}
    user_url = f"{URL_START}/User/GetMembershipsById/{attrMap['id']}/{attrMap['membershipType']}/"
    outFile = f"{bungieName}.json"
    message = f"Fetching membership data for: {bungieName}"
    iterator = ['Response', 'destinyMemberships']
    table = Account
    multiRequestAndInsert(session, elems, infoMap, user_url, outFile, message, iterator, table)

def oldHandleDestinyUsers(session):
    """Retrieve JSONs for users, listing their Destiny accounts. Builds account table."""
    users = session.query(Bungie).all()
    for user in users:
        bungieId = user.id
        bungieName = user.bungie_name
        kwargs = {"bungie_id" : bungieId}
        if not needsUpdate(Account, kwargs, session):
            print(f"Not updating account table for user: {bungieName}")
            continue
        membershipType = user.membership_type
        user_url = f"{URL_START}/User/GetMembershipsById/{bungieId}/{membershipType}/"
        message = f"Fetching membership data for: {bungieName}"
        outFile = f"{bungieName}.json"
        data = jsonRequest(user_url, outFile, message)
        if data is None:
            #TODO: Throw an error
            print("")
            continue
        #Grab all of the individual accounts and put them in the Account table
        accounts = data['Response']['destinyMemberships']
        for account in accounts:
            accountDict = {}
            accountDict['id'] = account['membershipId']
            accountDict['membership_type'] = account['membershipType']
            accountDict['display_name'] = account['displayName']
            accountDict['bungie_id'] = bungieId
            new_account = Account(**accountDict)
            insertOrUpdate(Account, new_account, session)

def handleAggregateStats(session):
    """Retrieve aggregate stats for users. Builds PvP and PvE average and total tables."""
    accounts = session.query(Account).all()
    for account in accounts:
        membershipId = account.id
        displayName = account.display_name
        kwargs = {"id" : membershipId}
        if not needsUpdate(PvPTotal, kwargs, session):
            print(f"Not updating PvP and PvE tables for user: {displayName}")
            continue
        membershipType = account.membership_type
        stat_url = f"{URL_START}/Destiny/Stats/Account/{membershipType}/{membershipId}"
        message = f"Fetching aggregate historical stats for: {displayName}"
        outFile = f"{displayName}_stats.json"
        data = jsonRequest(stat_url, outFile, message)
        if data is None:
            #TODO: Throw an error
            print("")
            continue

        #This part does the heavy lifting of table building
        #PvP first
        pvpTotalDict = {}
        pvpAvgDict = {}
        pveTotalDict = {}
        pveAvgDict = {}
        
        def fillDict(avgDict, totalDict, pvpOrPve):
            #We need to check if stats exist (if mode hasn't been played, there will be no stats
            allTime = data['Response']['mergedAllCharacters']['results'][pvpOrPve]
            if not 'allTime' in allTime:
                return None
            stats = allTime['allTime']
            for stat in stats:
                if 'pga' in stats[stat]:
                    avgDict[stat] = stats[stat]['pga']['value']
                totalDict[stat] = stats[stat]['basic']['value']

        fillDict(pvpAvgDict, pvpTotalDict, 'allPvP')
        fillDict(pveAvgDict, pveTotalDict, 'allPvE')
        
        #Now we just need to tack on the membershipId
        pvpTotalDict['id'] = membershipId
        pvpAvgDict['id'] = membershipId
        pveTotalDict['id'] = membershipId
        pveAvgDict['id'] = membershipId
        #And put these in the database. Double **s unpack a dictionary into the row.
        new_pvp_total = PvPTotal(**pvpTotalDict)
        new_pvp_avg = PvPAverage(**pvpAvgDict)
        new_pve_total = PvETotal(**pveTotalDict)
        new_pve_avg = PvEAverage(**pveAvgDict)
        insertOrUpdate(PvPTotal, new_pvp_total, session)
        insertOrUpdate(PvPAverage, new_pvp_avg, session)
        insertOrUpdate(PvETotal, new_pve_total, session)
        insertOrUpdate(PvEAverage, new_pve_avg, session)

def handleCharacters(session):
    """Retrieve JSONs for accounts, listing their Destiny characters. Builds characters table."""
    accounts = session.query(Account).all()
    for account in accounts:
        membershipId = account.id
        displayName = account.display_name
        kwargs = {"membership_id" : membershipId}
        if not needsUpdate(Character, kwargs, session):
            print(f"Not updating character table for user: {displayName}")
            continue
        membershipType = account.membership_type
        account_url = f"{URL_START}/Destiny/{membershipType}/Account/{membershipId}"
        message = f"Fetching character data for: {displayName}"
        outFile = f"{displayName}_characters.json"
        data = jsonRequest(account_url, outFile, message)
        if data is None:
            #TODO: Throw an error
            continue

        #Grab all of the individual accounts and put them in the Account table
        characters = data['Response']['data']['characters']
        for character in characters:
            characterDict = {}
            characterDict['id'] = character['characterBase']['characterId']
            characterDict['minutes_played'] = character['characterBase']['minutesPlayedTotal']
            characterDict['light_level'] = character['characterBase']['powerLevel']
            characterDict['membership_id'] = membershipId
            characterDict['class_hash'] = character['characterBase']['classHash']
            characterDict['grimoire'] = character['characterBase']['grimoireScore']
            new_character = Character(**characterDict)
            insertOrUpdate(Character, new_character, session)

#TODO: Next 2 functions are basically identical (and can be written identically). Abstract out.
def handleAggregateActivities(session):
    """Retrieve aggregate activity stats for users. Builds aggregateStatsCharacter table."""
    characters = session.query(Character).all()
    for character in characters:
        characterId = character.id
        membershipId = character.membership_id
        displayName = session.query(Account).filter_by(id=membershipId).first().display_name
        kwargs = {"id" : characterId}
        if not needsUpdate(AggregateStatsCharacter, kwargs, session):
            print(f"Not updating AggregateStatsCharacter table for user: {displayName}")
            continue
        membershipType = session.query(Account).filter_by(id=membershipId).first().membership_type
        stat_url = f"{URL_START}/Destiny/Stats/AggregateActivityStats/{membershipType}/{membershipId}/{characterId}"
        message = f"Fetching aggregate activity stats for: {displayName}"
        outFile =f"{displayName}_activities.json"
        data = jsonRequest(stat_url, outFile, message)
        if data is None:
            #TODO: Throw an error
            print("")
            continue
        #This part does the heavy lifting of table building
        aggStatDict = {}
        aggStatDict['id'] = characterId
        activities = data['Response']['data']['activities']
        for activity in activities:
            aggStatDict['activity_hash'] = activity['activityHash']
            for value in activity['values']:
                aggStatDict[value] = activity['values'][value]['basic']['value']
        new_aggregate_statistics = AggregateStatsCharacter(**aggStatDict)
        insertOrUpdate(AggregateStatsCharacter, new_aggregate_statistics, session)

def handleWeaponUsage(session):
    """Retrieve weapon usage for characters. Builds characterUsesWeapon table."""
    characters = session.query(Character).all()
    for character in characters:
        characterId = character.id
        membershipId = character.membership_id
        displayName = session.query(Account).filter_by(id=membershipId).first().display_name
        kwargs = {"character_id" : characterId}
        if not needsUpdate(CharacterUsesWeapon, kwargs, session):
            print(f"Not updating CharacterUsesWeapon table for user: {displayName}")
            continue
        membershipType = session.query(Account).filter_by(id=membershipId).first().membership_type
        stat_url = f"{URL_START}/Destiny/Stats/UniqueWeapons/{membershipType}/{membershipId}/{characterId}"
        message = f"Fetching weapon usage stats for: {displayName}"
        outFile = f"{displayName}_weapons.json"
        data = jsonRequest(stat_url, outFile, message)
        if data is None:
            #TODO: Throw an error
            print("")
            continue
        elif data['Response']['data'] == {}:
            continue
        weapons = data['Response']['data']['weapons']
        for weapon in weapons:
            weaponDict = {}
            weaponDict['character_id'] = characterId
            weaponDict['id'] = weapon['referenceId']
            weaponValues = weapon['values']
            weaponDict['kills'] = weaponValues['uniqueWeaponKills']['basic']['value']
            weaponDict['precision_kills'] = weaponValues['uniqueWeaponPrecisionKills']['basic']['value']
            weaponDict['precision_kill_percentage'] = weaponValues['uniqueWeaponKillsPrecisionKills']['basic']['value']
            new_weapon_stats = CharacterUsesWeapon(**weaponDict)
            
            matches = session.query(exists().where(and_(CharacterUsesWeapon.id == new_weapon_stats.id, CharacterUsesWeapon.character_id == new_weapon_stats.character_id))).scalar()
            if matches:
                # We have to do some strange things to pass update statements. This creates a dynamic dictionary to update all fields.
                session.query(CharacterUsesWeapon).filter_by(id=new_weapon_stats.id, character_id=new_weapon_stats.character_id).update({column: getattr(new_weapon_stats, column) for column in CharacterUsesWeapon.__table__.columns.keys()})
            else:
                session.add(new_weapon_stats)
            session.commit()

def handleMedals(session):
    """Retrieve aggregate activity stats for users. Builds aggregateStatsCharacter table."""
    accounts = session.query(Account).all()
    for account in accounts:
        membershipId = account.id
        displayName = session.query(Account).filter_by(id=membershipId).first().display_name
        kwargs = {"membership_id" : membershipId}
        if not needsUpdate(MedalsCharacter, kwargs, session):
            print(f"Not updating MedalsCharacter table for user: {displayName}")
            continue
        membershipType = session.query(Account).filter_by(id=membershipId).first().membership_type
        stat_url = f"{URL_START}/Destiny/Stats/Account/{membershipType}/{membershipId}/?Groups=Medals"
        message = f"Fetching medal stats for: {displayName}"
        outFile = f"{displayName}_medals.json"
        data = jsonRequest(stat_url, outFile, message)
        if data is None:
            #TODO: Throw an error
            print("")
            continue
        
        #This part does the heavy lifting of table building
        medalDict = {}
        characters = data['Response']['characters']
        for character in characters:
            medalDict['id'] = character['characterId']
            medalDict['membership_id'] = membershipId
            if 'merged' in character and 'allTime' in character['merged']:
                for medal in character['merged']['allTime']:
                    medalDict[medal] = character['merged']['allTime'][medal]['basic']['value']
            new_medal_statistics = MedalsCharacter(**medalDict)
            insertOrUpdate(MedalsCharacter, new_medal_statistics, session)

# This is going to be a lot. 2-36 are all different activity modes that will each require tracking.
def handleActivityHistory(session):
    accounts = session.query(Account).all()
    for account in accounts:
        membershipId = account.id
        displayName = account.display_name
        kwargs = {"id" : membershipId}
        if not needsUpdate(CharacterStatMayhemClash, kwargs, session):
            pass
            print(f"Not updating CharacterStatMayhemClash table for user: {displayName}")
            continue
        membershipType = account.membership_type
        stat_url = f"{URL_START}/Destiny/Stats/{membershipType}/{membershipId}/0/?modes=MayhemClash"
        message = f"Fetching mayhem clash stats for: {displayName}"
        outFile = f"{displayName}_stats.json"
        data = jsonRequest(stat_url, outFile, message)
        print("Data received.")
        if data is None:
            #TODO: Throw an error
            print("")
            continue
        
        #This part does the heavy lifting of table building
        actDict = {}
        actDict['id'] = membershipId
        if 'allTime' in data['Response']['mayhemClash']:
            stats = data['Response']['mayhemClash']['allTime']
        else:
            continue
        for stat in stats:
            actDict[stat] = stats[stat]['basic']['value']
            new_activity_statistics = CharacterStatMayhemClash(**actDict)
            insertOrUpdate(CharacterStatMayhemClash, new_activity_statistics, session)

def handleReferenceTables(session):
    """Connects to the manifest.content database and builds the necessary reference tables."""
    def buildReferenceTable(tableName, table, statement, dictionary, condition=None):
        print(f"Building {tableName} reference table...")
        con = sqlite3.connect(os.environ['MANIFEST_CONTENT'])
        cur = con.cursor()
        with con:
            cur.execute(statement)
            group = cur.fetchall()
            for item in group:
                itemInfo = json.loads(item[1])
                itemDict = {}
                if not condition is None and condition(itemInfo):
                    continue
                for (key,value) in dictionary.items():
                    itemDict[key] = itemInfo[value]
                new_item_def = table(**itemDict)
                insertOrUpdate(table, new_item_def, session)

    # Classes
    classTable = ClassReference
    classInfo = {'id':'classHash', 'class_name':'className'}
    classStatement = "SELECT * FROM DestinyClassDefinition"
    classDict = buildReferenceTable("class", classTable, classStatement, classInfo)

    # Weapons
    weaponTable = WeaponReference
    weaponInfo = {'id':'itemHash', 'weapon_name':'itemName', 'weapon_type':'itemTypeName', 'weapon_rarity':'tierTypeName'}
    weaponStatement = "SELECT * FROM DestinyInventoryItemDefinition"
    def weaponCondition(info):
        weapon_types = ['Rocket Launcher', 'Scout Rifle', 'Fusion Rifle', 'Sniper Rifle', 'Shotgun', 'Machine Gun', 'Pulse Rifle', 'Auto Rifle', 'Hand Cannon', 'Sidearm']
        return not ("itemTypeName" in info and info['itemTypeName'] in weapon_types)
    weaponDict = buildReferenceTable("weapon", weaponTable, weaponStatement, weaponInfo, weaponCondition)

    # Activities
    activityTable = ActivityReference
    activityInfo = {'id':'activityHash', 'activity_name':'activityName', 'activity_type_hash':'activityTypeHash'}
    activityStatement = "SELECT * FROM DestinyActivityDefinition"
    def activityCondition(info):
        return not ("activityName" in info)
    activityDict = buildReferenceTable("activity", activityTable, activityStatement, activityInfo, activityCondition)

    # Activity types
    activityTypeTable = ActivityTypeReference
    activityTypeInfo = {'id':'activityTypeHash', 'activity_type_name':'activityTypeName'}
    activityTypeStatement = "SELECT * FROM DestinyActivityTypeDefinition"
    def activityTypeCondition(info):
        return not ("activityTypeName" in info)
    activityTypeDict = buildReferenceTable("activity type", activityTypeTable, activityTypeStatement, activityTypeInfo, activityTypeCondition)

    # Buckets
    bucketTable = BucketReference
    bucketInfo = {'id':'bucketHash', 'bucket_name':'bucketName'}
    bucketStatement = "SELECT * FROM DestinyInventoryBucketDefinition"
    def bucketCondition(info): 
        return not ("bucketName" in info)
    bucketDict = buildReferenceTable("bucket", bucketTable, bucketStatement, bucketInfo, bucketCondition)

def jsonRequest(url, outFile, message=""):
    print(f"Connecting to Bungie: {url}")
    print(message)
    res = requests.get(url, headers=makeHeader())
    #print(res.text)
    data = res.json()
    error_stat = data['ErrorStatus']
    if error_stat == "Success":
        #with open(outFile,"w+") as f:
        #    json.dump(data, f)
        return data
    else:
        print("Error Status: " + error_stat)
        return None 

def insertOrUpdate(table, obj, session):
    matches = session.query(exists().where(table.id == obj.id)).scalar()
    if matches:
        # We have to do some strange things to pass update statements. This create a dynamic dictionary to update all fields.
        session.query(table).filter_by(id=obj.id).update({column: getattr(obj, column) for column in table.__table__.columns.keys()})
    else:
        session.add(obj)
    session.commit()

def needsUpdate(table, kwargs, session):
    now = datetime.now()
    try:
        lastUpdate = session.query(table).filter_by(**kwargs).first().last_updated
        print("Fetching last update...")
        daysSince = (now - lastUpdate).days
        #print (f"Days since update: {daysSince}")
        return daysSince >= UPDATE_DIFF
    except (AttributeError, TypeError):
        return True

if __name__ == "__main__":
    # loadConfig for testing purposes
    APP_PATH = "/etc/destinygotg"
    loadConfig()
    import time
    start_time = time.time()
    buildDB()
    print("--- %s seconds ---" % (time.time() - start_time))
