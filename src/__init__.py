import tbapy  # gives access to TBA API


def create_dict(team_dict, team):
    team_dict[team] = {
        'scores': [0] * 10,
        'auto_bottom': [0] * 10,
        'auto_inner': [0] * 10,
        'auto_outer': [0] * 10,
        'control': [0] * 10,
        'end_game': [0] * 10,
        'tele_bottom': [0] * 10,
        'tele_inner': [0] * 10,
        'tele_outer': [0] * 10,
        'auto_movement': [0] * 10
    }


def add_team(team, team_dict):
    create_dict(team_dict, team)


def add_team_dict(team_dict, team, score, auto_bottom, auto_inner, auto_outer, control, end_game, tele_bottom,
                  tele_inner, tele_outer, index, auto_movement):
    team_dict[team]['scores'][index] = score
    team_dict[team]['auto_bottom'][index] = auto_bottom
    team_dict[team]['auto_inner'][index] = auto_inner
    team_dict[team]['auto_outer'][index] = auto_outer
    team_dict[team]['control'][index] = control
    team_dict[team]['end_game'][index] = end_game
    team_dict[team]['tele_bottom'][index] = tele_bottom
    team_dict[team]['tele_inner'][index] = tele_inner
    team_dict[team]['tele_outer'][index] = tele_outer
    team_dict[team]['auto_movement'][index] = auto_movement


def find_averages(team_dict):
    tot_score = 0
    index = 0
    for team in team_dict.keys():
        # Find average score for the team
        scores = team_dict[team]['scores']
        for score in scores:
            if index == 9:
                avg_score = tot_score / 9
                team_dict[team]['scores'][-1] = avg_score
            tot_score = tot_score + score
            index += 1
        # find the average auto_bottom for the team
        auto_bottom = team_dict[team]['auto_bottom']
        tot_score = 0
        index = 0
        for score in auto_bottom:
            if index == 9:
                avg_score = tot_score / 9
                team_dict[team]['auto_bottom'][-1] = avg_score
            tot_score = tot_score + score
            index += 1
        # find the average auto_inner for each team
        auto_inner = team_dict[team]['auto_inner']
        tot_score = 0
        index = 0
        for score in auto_inner:
            if index == 9:
                avg_score = tot_score / 9
                team_dict[team]['auto_inner'][-1] = avg_score
            tot_score = tot_score + score
            index += 1
        # Find the average auto_outer for each team
        auto_outer = team_dict[team]['auto_outer']
        tot_score = 0
        index = 0
        for score in auto_outer:
            if index == 9:
                avg_score = tot_score / 9
                team_dict[team]['auto_outer'][-1] = avg_score
            tot_score = tot_score + score
            index += 1
        # Find the average control score for each team
        control = team_dict[team]['control']
        tot_score = 0
        index = 0
        for score in control:
            if index == 9:
                avg_score = tot_score / 9
                team_dict[team]['control'][-1] = avg_score
            tot_score = tot_score + score
            index += 1
        # Find the average end_game score for each team
        endgame = team_dict[team]['end_game']
        tot_score = 0
        index = 0
        for score in endgame:
            if index == 9:
                avg_score = tot_score / 9
                team_dict[team]['end_game'][-1] = avg_score
            tot_score = tot_score + score
            index += 1
        # Find the average tele_bottom score for each team
        tele_bottom = team_dict[team]['tele_bottom']
        tot_score = 0
        index = 0
        for score in tele_bottom:
            if index == 9:
                avg_score = tot_score / 9
                team_dict[team]['tele_bottom'][-1] = avg_score
            tot_score = tot_score + score
            index += 1
        # Find the average tele_inner score for each team
        tele_inner = team_dict[team]['tele_inner']
        tot_score = 0
        index = 0
        for score in tele_inner:
            if index == 9:
                avg_score = tot_score / 9
                team_dict[team]['tele_inner'][-1] = avg_score
            tot_score = tot_score + score
            index += 1
        #Find the average tele-outer for each team
        tele_outer = team_dict[team]['tele_outer']
        tot_score = 0
        index = 0
        for score in tele_outer:
          if index == 9:
            avg_score = tot_score / 9
            team_dict[team]['tele_outer'][-1] = avg_score
          tot_score = tot_score + score
          index += 1
        #Find the average auto_movement for each team
        auto_movement = team_dict[team]['auto_movement']
        tot_score = 0
        index = 0
        for score in auto_movement:
          if index == 9:
            avg_score = tot_score / 9
            team_dict[team]['auto_movement'][-1] = avg_score
          tot_score = tot_score + score
          index += 1
        # resest the variables
        tot_score = 0
        index = 0


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


def main():
    team_dict = {}
    tba = tbapy.TBA('rzxV1jZwdmWsmJGakoQrdFmCVntwtcGtSPcaVCEjWXXW8wpoScnXWUsFCJ1mY3n9')
    matches = tba.event_matches('2020ohmv')
    # loop over teams and add them to the team_dict
    for team in tba.event_teams('2020ohmv', keys=True):
        add_team(team, team_dict)

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
            if match['score_breakdown']['blue']['stage3Activated'] == True:
                control = 3
            elif match['score_breakdown']['blue']['stage3Activated'] == True:
                control = 2
            elif match['score_breakdown']['blue']['stage3Activated'] == True:
                control = 1
            else:
                control = 0
            if match['match_number'] > 10 and match['match_number'] <= 20:
                index = 1
            elif match['match_number'] > 20 and match['match_number'] <= 30:
                index = 2
            elif match['match_number'] > 30 and match['match_number'] <= 40:
                index = 3
            elif match['match_number'] > 40 and match['match_number'] <= 50:
                index = 4
            elif match['match_number'] > 50 and match['match_number'] <= 60:
                index = 5
            elif match['match_number'] > 60 and match['match_number'] <= 70:
                index = 6
            elif match['match_number'] > 70 and match['match_number'] <= 80:
                index = 7
            elif match['match_number'] > 80 and match['match_number'] <= 90:
                index = 8
            else:
                index = 0
            auto_cell_bottom = match['score_breakdown']['blue']['autoCellsBottom']
            auto_cell_inner = match['score_breakdown']['blue']['autoCellsInner']
            auto_cell_outer = match['score_breakdown']['blue']['autoCellsOuter']
            tele_cell_bottom = match['score_breakdown']['blue']['teleopCellsBottom']
            tele_cell_inner = match['score_breakdown']['blue']['teleopCellsInner']
            tele_cell_outer = match['score_breakdown']['blue']['teleopCellsOuter']
            # Blue 1
            endgame = get_endgame(match['score_breakdown']['blue']['endgameRobot1'])
            auto_movement = get_auto_movement(match['score_breakdown']['blue']['initLineRobot1'])
            add_team_dict(team_dict, blue_alliance[0], blue_score, auto_cell_bottom, auto_cell_inner,
                          auto_cell_outer, control, endgame, tele_cell_bottom, tele_cell_inner,
                          tele_cell_outer, index, auto_movement)
            # blue 2
            endgame = get_endgame(match['score_breakdown']['blue']['endgameRobot2'])
            auto_movement = get_auto_movement(match['score_breakdown']['blue']['initLineRobot2'])
            add_team_dict(team_dict, blue_alliance[1], blue_score, auto_cell_bottom, auto_cell_inner,
                          auto_cell_outer, control, endgame, tele_cell_bottom, tele_cell_inner,
                          tele_cell_outer, index, auto_movement)
            # blue 3
            endgame = get_endgame(match['score_breakdown']['blue']['endgameRobot2'])
            auto_movement = get_auto_movement(match['score_breakdown']['blue']['initLineRobot2'])
            add_team_dict(team_dict, blue_alliance[2], blue_score, auto_cell_bottom, auto_cell_inner,
                          auto_cell_outer, control, endgame, tele_cell_bottom, tele_cell_inner,
                          tele_cell_outer, index, auto_movement)
            # Red Score Breakdown
            if match['score_breakdown']['red']['stage3Activated'] == True:
                control = 3
            elif match['score_breakdown']['red']['stage3Activated'] == True:
                control = 2
            elif match['score_breakdown']['red']['stage3Activated'] == True:
                control = 1
            else:
                control = 0
            auto_cell_bottom = match['score_breakdown']['red']['autoCellsBottom']
            auto_cell_inner = match['score_breakdown']['red']['autoCellsInner']
            auto_cell_outer = match['score_breakdown']['red']['autoCellsOuter']
            tele_cell_bottom = match['score_breakdown']['red']['teleopCellsBottom']
            tele_cell_inner = match['score_breakdown']['red']['teleopCellsInner']
            tele_cell_outer = match['score_breakdown']['red']['teleopCellsOuter']
            # Red 1
            endgame = get_endgame(match['score_breakdown']['red']['endgameRobot1'])
            auto_movement = get_auto_movement(match['score_breakdown']['red']['initLineRobot1'])
            add_team_dict(team_dict, red_alliance[0], red_score, auto_cell_bottom, auto_cell_inner,
                          auto_cell_outer, control, endgame, tele_cell_bottom, tele_cell_inner,
                          tele_cell_outer, index, auto_movement)
            # Red 2
            endgame = get_endgame(match['score_breakdown']['red']['endgameRobot2'])
            auto_movement = get_auto_movement(match['score_breakdown']['red']['initLineRobot2'])
            add_team_dict(team_dict, red_alliance[1], red_score, auto_cell_bottom, auto_cell_inner,
                          auto_cell_outer, control, endgame, tele_cell_bottom, tele_cell_inner,
                          tele_cell_outer, index, auto_movement)
            # Red 3
            endgame = get_endgame(match['score_breakdown']['red']['endgameRobot3'])
            auto_movement = get_auto_movement(match['score_breakdown']['red']['initLineRobot3'])
            add_team_dict(team_dict, red_alliance[2], red_score, auto_cell_bottom, auto_cell_inner,
                          auto_cell_outer, control, endgame, tele_cell_bottom, tele_cell_inner,
                          tele_cell_outer, index, auto_movement)
    find_averages(team_dict)
    print(team_dict)
    # Turn into CSV file


main()
