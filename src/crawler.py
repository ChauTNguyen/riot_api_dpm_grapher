from src.functions import *
from .config import NUM_OF_GAMES


def crawl_dpm(summoner_id):
    dpms = []
    list_response = get_match_list(summoner_id)
    match_ids = get_matches_with_role(list_response, 'DUO_CARRY', NUM_OF_GAMES)

    for i in range(0, len(match_ids)):
        print("Grabbing match stats", i + 1, end="")
        curr_match_res = get_match(match_ids[i])
        dpms.append(
            calculate_dpm(
                get_total_damage_dealt_by_id(curr_match_res, get_participant_id(curr_match_res, summoner_id)),
                int(get_match_duration(curr_match_res) / 60)
            )
        )
        # print(get_champion_name(get_champ_id(curr_match_res, get_participant_id(curr_match_res, summoner_id))))

    return dpms


def crawl_avg_dpm(summoner_id):
    list_response = get_match_list(summoner_id)
    match_ids = get_matches_with_role(list_response, 'DUO_CARRY', NUM_OF_GAMES)
    total_game_secs = 0.0
    total_dmg = 0.0

    for i in range(0, len(match_ids)):
        print("Grabbing match stats", i + 1, end="")
        curr_match_res = get_match(str(match_ids[i]))
        total_game_secs += int(get_match_duration(curr_match_res))
        total_dmg += int(
            get_total_damage_dealt_by_id(
                curr_match_res, get_participant_id(curr_match_res, summoner_id)
            )
        )

    return calculate_dpm(total_dmg, total_game_secs / 60)