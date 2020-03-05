import tbapy  # gives access to TBA API
import writer

tba = tbapy.TBA('rzxV1jZwdmWsmJGakoQrdFmCVntwtcGtSPcaVCEjWXXW8wpoScnXWUsFCJ1mY3n9')


def create_dict(team_dict, team):
    team_dict[team] = {
        'scores': [0] * 10,
        'end_game': [0] * 10,
        'auto_movement': [0] * 10,
        'ranking': 0
    }


def add_team(team, team_dict):
    create_dict(team_dict, team)


def add_team_dict(team_dict, team, score, end_game, index, auto_movement):
    team_dict[team]['scores'][index] = score
    team_dict[team]['end_game'][index] = end_game
    team_dict[team]['auto_movement'][index] = auto_movement


def get_average(list, team_dict, team, key):
    tot_score = 0
    index = 0
    for score in list:
        if index == 9:
            avg_score = tot_score / 9
            team_dict[team][key][-1] = avg_score
        tot_score = tot_score + score
        index += 1


def find_averages(team_dict):
    for team in team_dict.keys():
        # Find average score for the team
        scores = team_dict[team]['scores']
        get_average(scores, team_dict, team, 'scores')
        # Find the average end_game score for each team
        endgame = team_dict[team]['end_game']
        get_average(endgame, team_dict, team, 'end_game')
        # Find the average auto_movement for each team
        auto_movement = team_dict[team]['auto_movement']
        get_average(auto_movement, team_dict, team, 'auto_movement')


def get_endgame(endgame):
    if endgame == 'None':
        return 0
    elif endgame == 'Park':
        return 5
    elif endgame == 'Hang':
        return 25
    else:
        return -1


def get_auto_movement(movement):
    if movement == 'Exited':
        return 1
    elif movement == 'None':
        return 0
    else:
        return -1


def get_index(match_number):
    if match_number > 10 and match_number <= 20:
        return 1
    elif match_number > 20 and match_number <= 30:
        return 2
    elif match_number > 30 and match_number <= 40:
        return 3
    elif match_number > 40 and match_number <= 50:
        return 4
    elif match_number > 50 and match_number <= 60:
        return 5
    elif match_number > 60 and match_number <= 70:
        return 6
    elif match_number > 70 and match_number <= 80:
        return 7
    elif match_number > 80 and match_number <= 90:
        return 8
    else:
        return 0


def get_control(match, color):
    if match['score_breakdown'][color]['stage3Activated'] == True:
        return 3
    elif match['score_breakdown'][color]['stage3Activated'] == True:
        return 2
    elif match['score_breakdown'][color]['stage3Activated'] == True:
        return 1
    else:
        return 0


def get_rankings(team_dict, event, tba):
    rankings = tba.event_rankings(event)
    for i in rankings['rankings']:
        team = i['team_key']
        rank = i['rank']
        team_dict[team]['ranking'] = rank


def main():
    team_dict = {}
    matches = tba.event_matches('2020ohmv')
    writer.create_match_csv('2020ohmv', matches)
    # loop over teams and add them to the team_dict
    for team in tba.event_teams('2020ohmv', keys=True):
        add_team(team, team_dict)
    get_rankings(team_dict, '2020ohmv', tba)
    # loop over qualification matches, adding info to the team_dict
    for match in matches:
        if match['comp_level'] == 'qm':
            blue_alliance = [match['alliances']['blue']['team_keys'][0], match['alliances']['blue']['team_keys'][1],
                             match['alliances']['blue']['team_keys'][2]]
            blue_score = match['alliances']['blue']['score']
            red_alliance = [match['alliances']['red']['team_keys'][0], match['alliances']['red']['team_keys'][1],
                            match['alliances']['red']['team_keys'][2]]
            red_score = match['alliances']['red']['score']
            # Score breakdown for Blue
            # control = get_control(match, 'blue')
            index = get_index(match['match_number'])

            # Blue 1
            endgame = get_endgame(match['score_breakdown']['blue']['endgameRobot1'])
            auto_movement = get_auto_movement(match['score_breakdown']['blue']['initLineRobot1'])
            add_team_dict(team_dict, blue_alliance[0], blue_score, endgame, index, auto_movement)
            # blue 2
            endgame = get_endgame(match['score_breakdown']['blue']['endgameRobot2'])
            auto_movement = get_auto_movement(match['score_breakdown']['blue']['initLineRobot2'])
            add_team_dict(team_dict, blue_alliance[1], blue_score, endgame, index, auto_movement)
            # blue 3
            endgame = get_endgame(match['score_breakdown']['blue']['endgameRobot2'])
            auto_movement = get_auto_movement(match['score_breakdown']['blue']['initLineRobot2'])
            add_team_dict(team_dict, blue_alliance[2], blue_score, endgame, index, auto_movement)
            # Red Score Breakdown
            # control = get_control(match, 'red')
            # Red 1
            endgame = get_endgame(match['score_breakdown']['red']['endgameRobot1'])
            auto_movement = get_auto_movement(match['score_breakdown']['red']['initLineRobot1'])
            add_team_dict(team_dict, red_alliance[0], red_score, endgame, index, auto_movement)
            # Red 2
            endgame = get_endgame(match['score_breakdown']['red']['endgameRobot2'])
            auto_movement = get_auto_movement(match['score_breakdown']['red']['initLineRobot2'])
            add_team_dict(team_dict, red_alliance[1], red_score, endgame, index, auto_movement)
            # Red 3
            endgame = get_endgame(match['score_breakdown']['red']['endgameRobot3'])
            auto_movement = get_auto_movement(match['score_breakdown']['red']['initLineRobot3'])
            add_team_dict(team_dict, red_alliance[2], red_score, endgame, index, auto_movement)
    find_averages(team_dict)

    # Turn into CSV file
    writer.create_csv('2020ohmv', team_dict)


def create_stats_dict(stats_dict, team):
    stats_dict[team] = {
        'opr': -1,
        'dpr': -1
    }


def add_value(stats_dict, is_opr, value, team):
    if is_opr:
        stats_dict[team]['opr'] = value
    else:
        stats_dict[team]['dpr'] = value


def get_opr():
    stats_dict = {}
    event = '2020ohmv'
    statistics = tba.event_oprs(event)
    for item in statistics['oprs']:
        team = item
        opr = statistics['oprs'][item]
        create_stats_dict(stats_dict, team)
        add_value(stats_dict, True, opr, team)
    for item in statistics['dprs']:
        team = item
        dpr = statistics['dprs'][item]
        add_value(stats_dict, False, dpr, team)
    writer.create_pr_csv(event, stats_dict)


main()
get_opr()
writer.update_google_sheets()
