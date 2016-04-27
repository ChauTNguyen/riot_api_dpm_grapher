from functions import *
from time import sleep

avg_dpms = []

def crawl(summoner_id):
    dpms = []

    region = "na"

    list_response = get_match_list(region, summoner_id)

    match_ids = []
    count = 0           # to make it so we only get 50 games...
    i = 0
    while count != 50:
        if list_response['matches'][i]['role'] == 'DUO_CARRY':
            match_ids.append(list_response['matches'][i]['matchId'])
            count += 1
        i += 1

    total_game_seconds = 0.0
    total_damage = 0.0

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

        total_game_seconds += int(get_match_duration(current_match_response))
        total_damage += int(get_total_damage_dealt_by_id(current_match_response, _participant_id))

        dpms.append(calculate_dpm(get_total_damage_dealt_by_id(current_match_response, _participant_id), int(get_match_duration(current_match_response) / 60)))
        sleep(.75) # to stay under the rate limit

    print()

    print("Total seconds wasted: " + str(total_game_seconds))
    print("Total minutes&seconds wasted: " + str(total_game_seconds / 60))
    print("Total hours&minutes wasted: " + str(convert_to_minutes_seconds(total_game_seconds / 60)))

    print()

    print("Average damage dealt: " + str(total_damage / len(match_ids)))
    print("Average game time in seconds: " + str(total_game_seconds / len(match_ids)))
    print("Average game time in minutes&seconds: " + convert_to_minutes_seconds(total_game_seconds / len(match_ids)))
    print("Average Dpm: " + str(calculate_dpm(total_damage, total_game_seconds / 60)))

    avg_dpms.append(calculate_dpm(total_damage, total_game_seconds / 60))

    return dpms