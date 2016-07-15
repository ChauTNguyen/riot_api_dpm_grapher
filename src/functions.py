import requests
from time import sleep

import src.config as config
from .config import NUM_OF_GAMES

KEY = config.key

REGION_ENDPOINT = "https://" + config.REGION + ".api.pvp.net/api/lol/"
TOO_MANY_REQUESTS = 429


# These functions grab responses.
def get_summoner_id(summoner_name):
    url = REGION_ENDPOINT + config.REGION + "/v1.4/summoner/by-name/" + summoner_name + "?api_key=" + KEY
    return rate_limiter(requests.get(url), url).json()[summoner_name]['id']


def get_match_list(summoner_id):
    """Return a match list by summoner id."""
    return requests.get(
        REGION_ENDPOINT + config.REGION + "/v2.2/matchlist/by-summoner/" + str(summoner_id) + "?api_key=" + KEY
    ).json()


def get_match(matchId):
    url = REGION_ENDPOINT + config.REGION + "/v2.2/match/" + str(matchId) + "?api_key=" + str(KEY)
    match_response = rate_limiter(
        requests.get(url), url)
    print(" => SUCCESS")
    return match_response.json()


def get_champion_name(champion_id):
    """Return a champion name corresponding to the champion id."""
    url = "https://global.api.pvp.net/api/lol/static-data/na/v1.2/champion/" + str(champion_id) + "?api_key=" + KEY
    return rate_limiter(
        requests.get(url), url
    ).json()['key']


# These functions below use a match response to return specific information.
def get_total_damage_dealt_by_id(match_response, participant_id):
    """Return the total damage dealt by participant id within a match."""
    return match_response['participants'][participant_id - 1]['stats']['totalDamageDealtToChampions']
    # participantId is +1 in participantIdentities (within the standard riot json file) ... must account for that


def get_champ_id(match_response, participantId):
    """Return the champion id by participant id within a match."""
    return match_response['participants'][participantId - 1]['championId']


def get_match_duration(match_response):
    """Return the match duration in minutes."""
    return match_response['matchDuration']


def get_participant_id(match_response, summoner_id):
    """Return the participantId of the participant within a match."""
    for n in range(0, 10):
        # Find the participant ID of the summoner in the current match.
        if match_response['participantIdentities'][n]['player']['summonerId'] == summoner_id:
            return match_response['participantIdentities'][n]['participantId']


def get_matches_with_role(list_response, role, num_of_games):
    """
    Return a list containing matches that all contain the same "role" value.
    {
   "matches": [
      {
         "timestamp": 1464940489115,
         "champion": 236,
         "region": "NA",
         "queue": "TEAM_BUILDER_DRAFT_RANKED_5x5",
         "season": "SEASON2016",
         "matchId": 2205686359,
         "role": "DUO_CARRY",  <--------
         "platformId": "NA1",
         "lane": "BOTTOM"
      },
    ...
    """
    match_ids = []
    count = 0
    i = 0
    while count != num_of_games:
        role_in_match = list_response['matches'][i]['role']

        if role_in_match == role:
            sleep(.75)
            match_with_role = list_response['matches'][i]['matchId']
            match_ids.append(match_with_role)
            count += 1
            print("LOADED", count, "/", NUM_OF_GAMES)
        i += 1

    return match_ids


# Extra functions
def rate_limiter(response, url):
    while str(response.status_code) == str(TOO_MANY_REQUESTS):
        print(response.status_code)
        print("\n\tExceeded rate limit.")
        print("\tTrying again in 5 seconds...")
        sleep(5)
        response = requests.get(url)
    return response


def convert_to_minutes_seconds(seconds):
    a = seconds / 60
    a, b = divmod(a, 1.0)
    b *= 60
    c = str(round(b))

    # just for formatting
    if len(str(c)) == 1:
        c = "0" + c
    return str(int(a)) + ":" + c


def calculate_dpm(total_damage, minutes):
    return round(total_damage / minutes)
