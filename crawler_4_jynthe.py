from crawler import get_match, get_champion_name
import config

KEY = config.key
region = "na"

# snownobo match ids. match ids are always first
# newest to oldest
match_ids = [2151814134, 2151746897, 2151117303, 2151113256, 2151068241, 2151070857,
             2148985988, 2148939120, 2148931983, 2148854194]
participants_ids = [1, 3, 5, 8, 1, 1, 8, 8, 1, 7]
champions_ids = [22, 81, 202, 96, 236, 236, 42, 42, 15, 202]
# count : 10

for i in range(0, len(match_ids)):
    current_match_response = get_match(region, str(match_ids[i]))
    print("Game: " + str(i + 1) + " - " + get_champion_name(champions_ids[i]) + " - Total damage dealt",
          current_match_response['participants'][participants_ids[i]]['stats']['totalDamageDealtToChampions'])
