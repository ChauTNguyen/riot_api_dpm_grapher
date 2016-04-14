import config
import requests

KEY = config.key

REGION_ENDPOINT = "https://na.api.pvp.net/api/lol/"

def get_match(region, matchId):
    """
    Retrieve match by match ID.
    """
    return requests.get(
        REGION_ENDPOINT + region + "/v2.2/match/" + str(matchId) + "?api_key=" + str(KEY)
        ).json()

def get_champion_name(championId):
    return requests.get(
        "https://global.api.pvp.net/api/lol/static-data/na/v1.2/champion/" + str(championId) + "?api_key=" + KEY
    ).json()['key']

def get_total_damage_dealt_by_id(response, participantId):
    return response['participants'][participantId-1]['stats']['totalDamageDealtToChampions']
    # participantId is +1 in participantIdentities... must account for that

def get_champ_id(response, participantId):
    return response['participants'][participantId-1]['championId']

def get_match_duration(response):
    return response['matchDuration']

def convert_to_minutes_seconds(seconds): # 2208 / 60 = 33
    a = seconds / 60
    a,b = divmod(a, 1.0)
    b *= 60
    c = str(round(b))
    if len(str(c)) == 1:
        c = "0" + c
    return str(int(a)) + ":" + c

def calculate_dpm(total_damage, minutes):
    return round(total_damage / minutes)