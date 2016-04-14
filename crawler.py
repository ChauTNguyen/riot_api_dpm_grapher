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