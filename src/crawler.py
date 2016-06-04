from src.functions import *
from time import sleep

NUM_OF_GAMES = 25

def crawl_dpm(summoner_id):
    dpms = []

    list_response = get_match_list(summoner_id)

    match_ids = get_matches_with_role(list_response, 'DUO_CARRY', NUM_OF_GAMES)

    print("\nFinished processing matches.")

    for i in range(0, len(match_ids)):
        print("Grabbing match", i + 1, end="")
        current_match_response = get_match(str(match_ids[i]))

        dpms.append(
            calculate_dpm(get_total_damage_dealt_by_id(current_match_response, get_participant_id(current_match_response, summoner_id)),
                          int(get_match_duration(current_match_response) / 60)))

        sleep(2)

    print()

    return dpms


def crawl_avg_dpm(summoner_id):
    list_response = get_match_list(summoner_id)

    match_ids = get_matches_with_role(list_response, 'DUO_CARRY', NUM_OF_GAMES)

    print("\nFinished processing matches.")

    total_game_seconds = 0.0
    total_damage = 0.0

    for i in range(0, len(match_ids)):
        print("Grabbing match", i + 1, end="")
        current_match_response = get_match(str(match_ids[i]))
        total_game_seconds += int(get_match_duration(current_match_response))
        total_damage += int(get_total_damage_dealt_by_id(current_match_response, get_participant_id(current_match_response, summoner_id)))
        sleep(2)

    print()

    return calculate_dpm(total_damage, total_game_seconds / 60)