import requests
import src.config as config

KEY = config.key

REGION_ENDPOINT = "https://na.api.pvp.net/api/lol/"

def get_summoner_id(region, summoner_name):
    return requests.get(REGION_ENDPOINT + region + "/v1.4/summoner/by-name/" + summoner_name + "?api_key=" + KEY).json()[summoner_name]['id']


def get_match_list(region, summoner_id):
    """Returns a match list by summoner id."""
    return requests.get(REGION_ENDPOINT + region + "/v2.2/matchlist/by-summoner/" + str(summoner_id) + "?api_key=" + KEY).json()


def get_match(region, matchId):
    """Retrieve match by match ID."""
    return requests.get(
        REGION_ENDPOINT + region + "/v2.2/match/" + str(matchId) + "?api_key=" + str(KEY)
        ).json()


def get_champion_name(champion_id):
    """Returns a champion name by champion id."""
    return requests.get(
        "https://global.api.pvp.net/api/lol/static-data/na/v1.2/champion/" + str(champion_id) + "?api_key=" + KEY
    ).json()['key']


def get_total_damage_dealt_by_id(response, participant_id):
    """Returns total damage dealt by participant id within a match."""
    return response['participants'][participant_id-1]['stats']['totalDamageDealtToChampions']
    # participantId is +1 in participantIdentities... must account for that


def get_champ_id(match_response, participantId):
    """Returns champion id by participant id within a match."""
    return match_response['participants'][participantId-1]['championId']


def get_match_duration(match_response):
    """Returns the match duration."""
    return match_response['matchDuration']


def convert_to_minutes_seconds(seconds):
    a = seconds / 60
    a,b = divmod(a, 1.0)
    b *= 60
    c = str(round(b))

    # just for formatting
    if len(str(c)) == 1:
        c = "0" + c
    return str(int(a)) + ":" + c


def calculate_dpm(total_damage, minutes):
    return round(total_damage / minutes)