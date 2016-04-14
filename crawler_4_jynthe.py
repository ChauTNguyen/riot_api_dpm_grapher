from crawler import get_match, get_champion_name, get_total_damage_dealt_by_id, get_champ_id, get_match_duration, convert_to_minutes_seconds, calculate_dpm
from crawler import config
import time
import requests

KEY = config.key
region = "na"

# snownobo match ids. match ids are always first
# newest to oldest

list_response = requests.get("https://na.api.pvp.net/api/lol/na/v2.2/matchlist/by-summoner/49188821?api_key=" + KEY).json()

match_ids = []

for i in range(0, 40):
    if list_response['matches'][i]['role'] == 'DUO_CARRY':
        match_ids.append(list_response['matches'][i]['matchId'])



# match_ids = [2151814134, 2151746897, 2151117303, 2151113256, 2151068241, 2151070857,
#              2148985988, 2148939120, 2148931983, 2148854194, 2148756190, 2148639840,
#              2148575712, 2148518678, 2133871688
#              ]
# match_ids = [2148756190]
# participants_ids = [1, 3, 5, 8, 1, 1, 8, 8, 1, 7]
# champions_ids = [22, 81, 202, 22, 236, 236, 42, 42, 15, 202]
summoner_id = 49188821

# count : 10

totalGameSeconds = 0.0
totalDamage = 0.0

for i in range(0, len(match_ids)):
    current_match_response = get_match(region, str(match_ids[i]))

    for n in range(0, 10):
        if current_match_response['participantIdentities'][n]['player']['summonerId'] == summoner_id:
            _participant_id = current_match_response['participantIdentities'][n]['participantId']

    print("Game: " + str(i+1) + " - " + convert_to_minutes_seconds(get_match_duration(current_match_response))
          + " minutes - " + get_champion_name(get_champ_id(current_match_response, _participant_id))
          + " - Total damage dealt "
          + str(get_total_damage_dealt_by_id(current_match_response, _participant_id))
          + " ||| " + "DPM: "
          + str(calculate_dpm(get_total_damage_dealt_by_id(current_match_response, _participant_id), int(get_match_duration(current_match_response) / 60)))
          ) # participant_id must be - 1. the array is 0-9, participantids are 1-10

    totalGameSeconds += int(get_match_duration(current_match_response))
    totalDamage += int(get_total_damage_dealt_by_id(current_match_response, _participant_id))

    time.sleep(.75) # to stay under the rate limit

print()

print("Total seconds wasted: " + str(totalGameSeconds))
print("Total minutes&seconds wasted: " + str(totalGameSeconds / 60))
print("Total hours&minutes wasted: " + str(convert_to_minutes_seconds(totalGameSeconds / 60)))

print()

print("Average damage dealt: " + str(totalDamage / len(match_ids)))
print("Average game time in seconds: " + str(totalGameSeconds / len(match_ids)))
print("Average game time in minutes&seconds: " + convert_to_minutes_seconds(totalGameSeconds / len(match_ids)))
print("Average Dpm: " + str(calculate_dpm(totalDamage, totalGameSeconds / 60)))

# screenshot: http://puu.sh/ohxDl/9fb92c438e.png