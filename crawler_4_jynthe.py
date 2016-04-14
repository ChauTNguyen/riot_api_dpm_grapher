from crawler import get_match, get_champion_name, get_total_damage_dealt_by_id, get_champ_id, get_match_duration, convert_to_minutes_seconds
from crawler import config
import time

KEY = config.key
region = "na"

# snownobo match ids. match ids are always first
# newest to oldest
match_ids = [2151814134, 2151746897, 2151117303, 2151113256, 2151068241, 2151070857,
             2148985988, 2148939120, 2148931983, 2148854194, 2148756190, 2148639840,
             2148575712, 2148518678
             ]
# match_ids = [2148756190]
# participants_ids = [1, 3, 5, 8, 1, 1, 8, 8, 1, 7]
# champions_ids = [22, 81, 202, 22, 236, 236, 42, 42, 15, 202]
summoner_id = 49188821

# count : 10

for i in range(0, len(match_ids)):
    current_match_response = get_match(region, str(match_ids[i]))

    for n in range(0, 10):
        if current_match_response['participantIdentities'][n]['player']['summonerId'] == summoner_id:
            _participant_id = current_match_response['participantIdentities'][n]['participantId']

    print("Game: " + str(i+1) + " - " + convert_to_minutes_seconds(get_match_duration(current_match_response))
          + " minutes - " + get_champion_name(get_champ_id(current_match_response, _participant_id)) + " - Total damage dealt",
                get_total_damage_dealt_by_id(current_match_response, _participant_id)
          ) # participant_id must be - 1. the array is 0-9, participantids are 1-10

    time.sleep(.75) # to stay under the rate limit