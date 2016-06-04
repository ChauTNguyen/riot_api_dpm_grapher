from src.functions import *
from time import sleep

NUM_OF_GAMES = 25

def crawl_dpm(summoner_id):
    dpms = []
    region = "na"

    list_response = get_match_list(region, summoner_id)

    match_ids = []
    count = 0
    i = 0
    while count != NUM_OF_GAMES:
        if list_response['matches'][i]['role'] == 'DUO_CARRY':
            match_ids.append(list_response['matches'][i]['matchId'])
            count += 1
        i += 1

    print("\nFinished processing matches.")

    for i in range(0, len(match_ids)):
        print("Grabbing match", i + 1, end="")
        current_match_response = get_match(region, str(match_ids[i]))

        # print("Game: " + str(i+1) + " - " + convert_to_minutes_seconds(get_match_duration(current_match_response))
        #       + " minutes - " + get_champion_name(get_champ_id(current_match_response, _participant_id))
        #       + " - Total damage dealt "
        #       + str(get_total_damage_dealt_by_id(current_match_response, _participant_id))
        #       + " ||| " + "DPM: "
        #       + str(calculate_dpm(get_total_damage_dealt_by_id(current_match_response, _participant_id), int(get_match_duration(current_match_response) / NUMBER_OF_GAMES)))
        #       ) # participantIds are indexed 1-10 in the json file

        dpms.append(
            calculate_dpm(get_total_damage_dealt_by_id(current_match_response, get_participant_id(current_match_response, summoner_id)),
                          int(get_match_duration(current_match_response) / 60)))

    print()

    # print("Total seconds wasted: " + str(total_game_seconds))
    # print("Total minutes&seconds wasted: " + str(total_game_seconds / 60))
    # print("Total hours&minutes wasted: " + str(convert_to_minutes_seconds(total_game_seconds / 60)))
    #
    # print()
    #
    # print("Average damage dealt: " + str(total_damage / len(match_ids)))
    # print("Average game time in seconds: " + str(total_game_seconds / len(match_ids)))
    # print("Average game time in minutes&seconds: " + convert_to_minutes_seconds(total_game_seconds / len(match_ids)))
    # print("Average Dpm: " + str(calculate_dpm(total_damage, total_game_seconds / 60)))

    print("Finished appending DPM.")
    return dpms


def crawl_avg_dpm(summoner_id):
    avg_dpm = 0
    region = "na"

    list_response = get_match_list(region, summoner_id)

    match_ids = []
    count = 0
    i = 0
    while count != NUM_OF_GAMES:
        if list_response['matches'][i]['role'] == 'DUO_CARRY':
            match_ids.append(list_response['matches'][i]['matchId'])
            count += 1
        i += 1

    print("\nFinished processing matches.")

    total_game_seconds = 0.0
    total_damage = 0.0

    for i in range(0, len(match_ids)):
        print("Grabbing match", i + 1, end="")
        current_match_response = get_match(region, str(match_ids[i]))
        total_game_seconds += int(get_match_duration(current_match_response))
        total_damage += int(get_total_damage_dealt_by_id(current_match_response, get_participant_id(current_match_response, summoner_id)))

    print()

    avg_dpm = calculate_dpm(total_damage, total_game_seconds / 60)
    print("Finished appending AVG DPM.")
    return avg_dpm
