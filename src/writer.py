def create_csv(event, team_dict):
    filename = event + '.csv'
    file = open(filename, 'w')
    header = 'team,'
    for i in range(0, 4):
        for j in range(0, 10):
            if i == 0 and j != 9:
                header = header + 'score' + str(j) + ','
            elif i == 1 and j != 9:
                header = header + 'end_game' + str(j) + ','
            elif i == 2 and j != 9:
                header = header + 'auto_movement' + str(j) + ','
            elif i == 3:
                header = header + 'rank,'
            elif j == 9:
                header = header + 'avg,,'
    file.write(header + '\n')
    buffer = ''
    for team in team_dict:
        buffer = buffer + team + ','
        for field in team_dict[team]:
            print(field)
            if field == 'ranking':
                buffer = buffer + str(team_dict[team]['ranking']) + ','
            else:
                for thing in team_dict[team][field]:
                    buffer = buffer + str(thing) + ','
                buffer = buffer + ','
        buffer = buffer + '\n'
    file.write(buffer)
    file.close()


def create_match_csv(event, matches):
    filename = event + '_matches.csv'
    file = open(filename, 'w')
    header = 'match_num, red1, red2, red3, blue1, blue2, blue3, red_score, blue_score'
    file.write(header + '\n')
    buffer = ''
    full_buffer = [''] *91
    for match in matches:
        if match['comp_level'] == 'qm':
            buffer = buffer + str(match['match_number']) + ','
            buffer = buffer + match['alliances']['blue']['team_keys'][0] + ','
            buffer = buffer + match['alliances']['blue']['team_keys'][1] + ','
            buffer = buffer + match['alliances']['blue']['team_keys'][0] + ','
            buffer = buffer + match['alliances']['red']['team_keys'][0] + ','
            buffer = buffer + match['alliances']['red']['team_keys'][1] + ','
            buffer = buffer + match['alliances']['red']['team_keys'][2] + ','
            buffer = buffer + str(match['alliances']['blue']['score']) + ',' + str(match['alliances']['red']['score']) + '\n'
            full_buffer[match['match_number']] = buffer
            buffer = ''
    for match in full_buffer:
        file.write(match)