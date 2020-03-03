def create_csv(event, team_dict):
    filename = event + '.csv'
    file = open(filename, 'w')
    header = 'team,'
    for i in range(0,10):
        for j in range(0,10):
            if i == 0 and j != 9:
                header = header + 'score' + str(j) + ','
            elif i == 1 and j != 9:
                header = header + 'auto_bottom' + str(j) + ','
            elif i == 2 and j != 9:
                header = header + 'auto_inner' + str(j) + ','
            elif i == 3 and j != 9:
                header = header + 'auto_outer' + str(j) + ','
            elif i == 4 and j != 9:
                header = header + 'control' + str(j) + ','
            elif i == 5 and j != 9:
                header = header + 'end_game' + str(j) + ','
            elif i == 6 and j != 9:
                header = header + 'tele_bottom' + str(j) + ','
            elif i == 7 and j != 9:
                header = header + 'tele_inner' + str(j) + ','
            elif i == 8 and j != 9:
                header = header + 'tele_outer' + str(j) + ','
            elif i == 9 and j != 9:
                header = header + 'auto_movement' + str(j) + ','
            elif j == 9:
                header = header + 'avg,,'
    file.write(header + '\n')
    buffer = ''
    for team in team_dict:
        buffer = buffer + team + ','
        for field in team_dict[team]:
            for thing in team_dict[team][field]:
                buffer = buffer + str(thing) + ','
            buffer = buffer + ','
        buffer = buffer + '\n'
    file.write(buffer)
    file.close()