#!/usr/bin/env python
import os
import json
import sqlite3
import requests
import zipfile
import shutil
#import discordBot
import initdb
import builddb

APP_PATH = "./etc"
DBPATH = f"{APP_PATH}/guardians2.db"

def check_db():
    """Check to see if a database exists"""
    return os.path.isfile(os.environ['DBPATH'])

def init_db(engine):
    """Sets up the tables for the database"""
    initdb.init_db(engine)

def check_manifest():
    """Check to see if manifest file exists"""
    return os.path.isfile(os.environ['MANIFEST_CONTENT'])

def get_manifest():
    """Pulls the requested definitions into the manifest database"""
    manifest_url = "http://www.bungie.net/Platform/Destiny2/Manifest/"
    r = requests.get(manifest_url)
    manifest = r.json()
    mani_url = f"http://www.bungie.net/{manifest['Response']['mobileWorldContentPaths']['en']}"
    #Download the file, write it to MANZIP
    r = requests.get(mani_url)
    with open(f"{APP_PATH}/MANZIP", "wb") as manzip:
        manzip.write(r.content)
    #Extract the file contents, and rename the extracted file
    with zipfile.ZipFile(f"{APP_PATH}/MANZIP") as myzip:
        name = myzip.namelist()
        myzip.extractall()
    shutil.move(name[0], os.environ['MANIFEST_CONTENT'])

def build_db():
    """Main function to build the full database"""
    builddb.build_db()

# def run_discord(engine):
#     discordBot.run_bot(engine)
