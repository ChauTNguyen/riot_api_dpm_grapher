from crawler import *
from time import sleep
dpm = []
def crawl():
    KEY = config.key
    region = "na"

    # snownobo's summoner id. match ids are always first
    summoner_id = 49188821
    list_response = get_match_list(region, summoner_id)

    match_ids = []

    for i in range(0, 100):
        if list_response['matches'][i]['role'] == 'DUO_CARRY':
            match_ids.append(list_response['matches'][i]['matchId'])

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
        dpm.append(calculate_dpm(get_total_damage_dealt_by_id(current_match_response, _participant_id), int(get_match_duration(current_match_response) / 60)))
        sleep(.75) # to stay under the rate limit

    print()

    print("Total seconds wasted: " + str(totalGameSeconds))
    print("Total minutes&seconds wasted: " + str(totalGameSeconds / 60))
    print("Total hours&minutes wasted: " + str(convert_to_minutes_seconds(totalGameSeconds / 60)))

    print()

    print("Average damage dealt: " + str(totalDamage / len(match_ids)))
    print("Average game time in seconds: " + str(totalGameSeconds / len(match_ids)))
    print("Average game time in minutes&seconds: " + convert_to_minutes_seconds(totalGameSeconds / len(match_ids)))
    print("Average Dpm: " + str(calculate_dpm(totalDamage, totalGameSeconds / 60)))

    return dpm
    # screenshot: http://puu.sh/ohxDl/9fb92c438e.png