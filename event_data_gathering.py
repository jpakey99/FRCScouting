import tbapy  # gives access to TBA API
from Graph import LineGraph
import data2022
import VisCreation
from scouting.scouting2022 import scouting2022, team_point_contribution
tba = tbapy.TBA('rzxV1jZwdmWsmJGakoQrdFmCVntwtcGtSPcaVCEjWXXW8wpoScnXWUsFCJ1mY3n9')

from scouting.power_rankings import power_rankings2022


def get_playoff_allainces(event):
    alliances = []
    raw_alliances = tba.event_alliances(event)
    for a in raw_alliances:
        alliance = []
        for team in a['picks']:
            alliance.append(team)
        alliances.append(alliance)
    return alliances


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
event = "2022flwp"
print(get_playoff_allainces(event))
# match = tba.event_matches(event)
# match = qual_matches(match)
# team_dict = scouting2022(match)
# cont = team_point_contribution(team_dict)
# print(cont)
# power_rankings2022(cont)
# print(match)


# print([data_dict])
# print(len(data_dict['general']['autoPoints']))

