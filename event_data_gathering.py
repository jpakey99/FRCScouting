import tbapy  # gives access to TBA API
from Graph import LineGraph
import data2022
import year_specific_data
import VisCreation
tba = tbapy.TBA('rzxV1jZwdmWsmJGakoQrdFmCVntwtcGtSPcaVCEjWXXW8wpoScnXWUsFCJ1mY3n9')


def qual_matches(event_matches):
    matches = []
    return event_matches


def playoff_matches(event_matches):
    matches = []
    return event_matches


data_dict = data2022.create_data_dict_2022()
event = "2022week0"
match = tba.event_matches(event)
# print(match)
# keys = match['score_breakdown']['blue']
for m in match:
    data2022.match_data_20222(m, data_dict)

VisCreation.general_points_vis([data_dict])

# print([data_dict])
# print(len(data_dict['general']['autoPoints']))

