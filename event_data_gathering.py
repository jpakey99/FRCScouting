import tbapy  # gives access to TBA API
from Graph import LineGraph
import data2022
import VisCreation
from scouting.scouting2022 import scouting2022, team_point_contribution
tba = tbapy.TBA('rzxV1jZwdmWsmJGakoQrdFmCVntwtcGtSPcaVCEjWXXW8wpoScnXWUsFCJ1mY3n9')
from scouting.power_rankings import power_rankings2022


def qual_matches(event_matches):
    matches = []
    for match in event_matches:
        if match['comp_level'] == 'qm':
            matches.append(match)
    return matches


def playoff_matches(event_matches):
    matches = []
    for match in event_matches:
        if match['comp_level'] != 'qm':
            matches.append(match)
    return matches


data_dict = data2022.create_data_dict_2022()
event = "2022week0"
match = tba.event_matches(event)
match = qual_matches(match)
team_dict = scouting2022(match)
cont = team_point_contribution(team_dict)
print(cont)
power_rankings2022(cont)
# print(match)
# keys = match['score_breakdown']['blue']
# for m in match:
#     print(m['comp_level'], m['key'])
    # data2022.match_data_20222(m, data_dict)

# VisCreation.general_points_vis([data_dict])

# print([data_dict])
# print(len(data_dict['general']['autoPoints']))

