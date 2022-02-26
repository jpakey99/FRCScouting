endgame_conversion = {
    'None': 0,
    'Low': 2,
    'Mid': 4,
    'High': 10,
    'Traversal': 15
}
low_auto_points, high_auto_points, low_tele_points, high_tele_points = 2,4,1,2


def create_dict(team_dict, team):
    team_dict[team] = {
        'taxi': [],
        'auto_low': [],
        'auto_high': [],
        'tele_low': [],
        'tele_high': [],
        'endgame': []
    }


def add_team(team, team_dict):
    create_dict(team_dict, team)


def update_team(team, team_dict, taxi, auto_low, auto_high, tele_low, tele_high, endgame):
    team_dict[team]['taxi'].append(taxi)
    team_dict[team]['auto_low'].append(auto_low)
    team_dict[team]['auto_high'].append(auto_high)
    team_dict[team]['tele_low'].append(tele_low)
    team_dict[team]['tele_high'].append(tele_high)
    team_dict[team]['endgame'].append(endgame)


def calc_lower_hub_amount(match, color, match_time):
    lower_cargo = 0
    lower_cargo += int(match['score_breakdown'][color][match_time + 'CargoLowerBlue'])
    lower_cargo += int(match['score_breakdown'][color][match_time + 'CargoLowerFar'])
    lower_cargo += int(match['score_breakdown'][color][match_time + 'CargoLowerNear'])
    lower_cargo += int(match['score_breakdown'][color][match_time + 'CargoLowerRed'])
    return lower_cargo


def calc_upper_hub_amount(match, color, match_time):
    upper_cargo = 0
    upper_cargo += int(match['score_breakdown'][color][match_time + 'CargoUpperBlue'])
    upper_cargo += int(match['score_breakdown'][color][match_time + 'CargoUpperFar'])
    upper_cargo += int(match['score_breakdown'][color][match_time + 'CargoUpperNear'])
    upper_cargo += int(match['score_breakdown'][color][match_time + 'CargoUpperRed'])
    return upper_cargo


def scout_match(match, team_dict):
    blue = match['alliances']['blue']['team_keys']
    red = match['alliances']['red']['team_keys']
    bt = [match['score_breakdown']['blue']['taxiRobot1'], match['score_breakdown']['blue']['taxiRobot2'],match['score_breakdown']['blue']['taxiRobot3']]
    rt = [match['score_breakdown']['red']['taxiRobot1'], match['score_breakdown']['red']['taxiRobot2'],match['score_breakdown']['red']['taxiRobot3']]
    blue_taxi, red_taxi = [], []
    for t in range(3):
        if bt[t] == 'No':
            blue_taxi.append(0)
        else:
            blue_taxi.append(2)
        if rt[t] == 'No':
            red_taxi.append(0)
        else:
            red_taxi.append(2)
    red_auto_cargo_low = calc_lower_hub_amount(match, 'red', 'auto')
    red_tele_cargo_low = calc_lower_hub_amount(match, 'red', 'teleop')
    blue_auto_cargo_low = calc_lower_hub_amount(match, 'blue', 'auto')
    blue_tele_cargo_low = calc_lower_hub_amount(match, 'blue', 'teleop')
    red_auto_cargo_high = calc_upper_hub_amount(match, 'red', 'auto')
    red_tele_cargo_high = calc_upper_hub_amount(match, 'red', 'teleop')
    blue_auto_cargo_high = calc_upper_hub_amount(match, 'blue', 'auto')
    blue_tele_cargo_high = calc_upper_hub_amount(match, 'blue', 'teleop')
    blue_endgame = [match['score_breakdown']['blue']['endgameRobot1'], match['score_breakdown']['blue']['endgameRobot2'], match['score_breakdown']['blue']['endgameRobot3']]
    red_endgame = [match['score_breakdown']['red']['endgameRobot1'], match['score_breakdown']['red']['endgameRobot2'], match['score_breakdown']['red']['endgameRobot3']]
    for i in range(len(blue)):
        end_game = endgame_conversion[blue_endgame[i]]
        if blue[i] not in team_dict:
            add_team(blue[i], team_dict)
        update_team(blue[i], team_dict, blue_taxi[i], int(blue_auto_cargo_low), int(blue_auto_cargo_high), int(blue_tele_cargo_low), int(blue_tele_cargo_high), end_game)
        end_game = endgame_conversion[blue_endgame[i]]
        if red[i] not in team_dict:
            add_team(red[i], team_dict)
        update_team(red[i], team_dict, red_taxi[i], int(red_auto_cargo_low), int(red_auto_cargo_high), int(red_tele_cargo_low), int(red_tele_cargo_high), end_game)


def scouting2022(matches:list):
    team_dict = {}
    for match in matches:
        scout_match(match, team_dict)
    return team_dict


def team_point_contribution(team_dict):
    contributions = []
    for team in team_dict:
        taxi, auto_low, auto_high, tele_low, tele_high, endgame = 0,0,0,0,0,0
        matches = len(team_dict[team]['taxi'])
        for i in range(matches):
            taxi += team_dict[team]['taxi'][i]
            auto_low += team_dict[team]['auto_low'][i]
            auto_high += team_dict[team]['auto_high'][i]
            tele_low += team_dict[team]['tele_low'][i]
            tele_high += team_dict[team]['tele_high'][i]
            endgame += team_dict[team]['endgame'][i]
        total = (taxi)/matches + ((2*auto_low)/matches) + ((4*auto_high)/matches) + (tele_low/matches) + ((2*tele_high)/matches) + (endgame/matches)
        contributions.append([team, total, taxi/matches, ((auto_low*2)/matches + (auto_high *4)/matches), ((tele_low)/matches + (2*tele_high)/matches), endgame/matches])
    return contributions
