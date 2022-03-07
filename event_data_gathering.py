import tbapy  # gives access to TBA API
from Graph import LineGraph
import data2022
import VisCreation
from scouting.scouting2022 import scouting2022, team_point_contribution
from scouting.drating_data import draft_efficiency
tba = tbapy.TBA('rzxV1jZwdmWsmJGakoQrdFmCVntwtcGtSPcaVCEjWXXW8wpoScnXWUsFCJ1mY3n9')

from scouting.power_rankings import power_rankings2022


def get_team_contributions(qual_matches):
    team_dict = scouting2022(qual_matches)
    return team_point_contribution(team_dict)


def get_matches_for_event(event):
    return tba.event_matches(event)


def draft_eff_for_event(event):
    alliances = get_playoff_allainces(event)
    match = get_matches_for_event(event)
    q_matches = qual_matches(match)
    cont = get_team_contributions(q_matches)
    draft_efficiency(cont, alliances, event)


def draft_eff_for_week(events):
    for event in events:
        draft_eff_for_event(event)


def get_event_keys_by_week(year:str, week:int):
    events = tba.events(year)
    keys = []
    for event in events:
        if event['week'] == week and not event['key'][-2].isdigit():
            keys.append(event['key'])
    return keys


def get_event_keys(year:str):
    events = tba.events(year)
    keys = []
    for event in events:
        keys.append(event['key'])
    return keys


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


# data_dict = data2022.create_data_dict_2022()
events = get_event_keys_by_week("2022", 0)
# event = "2022bcvi"
# event = "2022flwp"
# print(events)
# draft_eff_for_event(event)
draft_eff_for_week(events)


# print(cont)
# power_rankings2022(cont)
# print(match)


