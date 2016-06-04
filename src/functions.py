import requests
import src.config as config
from time import sleep

KEY = config.key

REGION_ENDPOINT = "https://na.api.pvp.net/api/lol/"


# These functions grab responses.
def get_summoner_id(region, summoner_name):
    return requests.get(
        REGION_ENDPOINT + region + "/v1.4/summoner/by-name/" + summoner_name + "?api_key=" + KEY
    ).json()[summoner_name]['id']


def get_match_list(region, summoner_id):
    """Return a match list by summoner id."""
    return requests.get(
        REGION_ENDPOINT + region + "/v2.2/matchlist/by-summoner/" + str(summoner_id) + "?api_key=" + KEY
    ).json()


def get_match(region, matchId):
    response = requests.get(REGION_ENDPOINT + region + "/v2.2/match/" + str(matchId) + "?api_key=" + str(KEY))

    while response.status_code == 429:      # rate limiter
        print("\n\tExceeded rate limit.")
        print("\tTrying again in 5 seconds...")
        sleep(5)
        response = requests.get(REGION_ENDPOINT + region + "/v2.2/match/" + str(matchId) + "?api_key=" + str(KEY))

    print(" => SUCCESS")
    return response.json()



def get_champion_name(champion_id):
    """Return a champion name corresponding to the champion id."""
    return requests.get(
        "https://global.api.pvp.net/api/lol/static-data/na/v1.2/champion/" + str(champion_id) + "?api_key=" + KEY
    ).json()['key']


# These functions below use a match response to return specific information.
def get_total_damage_dealt_by_id(match_response, participant_id):
    """Return the total damage dealt by participant id within a match."""
    return match_response['participants'][participant_id-1]['stats']['totalDamageDealtToChampions']
    # participantId is +1 in participantIdentities (within the standard riot json file) ... must account for that


def get_champ_id(match_response, participantId):
    """Return the champion id by participant id within a match."""
    return match_response['participants'][participantId-1]['championId']


def get_match_duration(match_response):
    """Return the match duration in minutes."""
    return match_response['matchDuration']


def get_participant_id(match_response, summoner_id):
    for n in range(0, 10):
        # Find the participant ID of the summoner in the current match.
        if match_response['participantIdentities'][n]['player']['summonerId'] == summoner_id:
            return match_response['participantIdentities'][n]['participantId']


# Extra functions
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