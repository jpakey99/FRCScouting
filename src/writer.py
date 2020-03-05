import gspread
from oauth2client.service_account import ServiceAccountCredentials

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
            elif i == 3 and j == 0:
                header = header + 'rank,'
            elif j == 9 and i != 3:
                header = header + 'avg,'
    file.write(header + '\n')
    buffer = ''
    full_buffer = [''] * 61
    for team in team_dict:
        buffer = buffer + team[3:] + ','
        for field in team_dict[team]:
            if field == 'ranking':
                buffer = buffer + str(team_dict[team]['ranking']) + ','
            else:
                for thing in team_dict[team][field]:
                    buffer = buffer + str(thing) + ','
        buffer = buffer + '\n'
        full_buffer[team_dict[team]['ranking']] = buffer
        buffer = ''
    for team in full_buffer:
        file.write(team)
    file.close()


def create_match_csv(event, matches):
    filename = event + '_matches.csv'
    file = open(filename, 'w')
    header = 'match_num, red1, red2, red3, blue1, blue2, blue3, red_score, blue_score'
    file.write(header + '\n')
    buffer = ''
    full_buffer = [''] * 91
    for match in matches:
        if match['comp_level'] == 'qm':
            buffer = buffer + str(match['match_number']) + ','
            buffer = buffer + match['alliances']['blue']['team_keys'][0][3:] + ','
            buffer = buffer + match['alliances']['blue']['team_keys'][1][3:] + ','
            buffer = buffer + match['alliances']['blue']['team_keys'][0][3:] + ','
            buffer = buffer + match['alliances']['red']['team_keys'][0][3:] + ','
            buffer = buffer + match['alliances']['red']['team_keys'][1][3:] + ','
            buffer = buffer + match['alliances']['red']['team_keys'][2][3:] + ','
            buffer = buffer + str(match['alliances']['blue']['score']) + ',' + str(
                match['alliances']['red']['score']) + '\n'
            full_buffer[match['match_number']] = buffer
            buffer = ''
    for match in full_buffer:
        file.write(match)

def create_pr_csv(event, stats_dict):
    filename = event + 'pr.csv'
    file = open(filename, 'w')
    header = 'team,opr,dpr\n'
    file.write(header)
    for team in stats_dict:
        buffer = team[3:] + ',' + str(stats_dict[team]['opr']) + ',' + str(stats_dict[team]['dpr']) + '\n'
        file.write(buffer)
        buffer = ''

def update_google_sheets():
    scope = ['https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/drive']

    credentials = ServiceAccountCredentials.from_json_keyfile_name('frc1-270019-1901cd8234bb.json', scope)

    gc = gspread.authorize(credentials)

    wks = gc.open("Sheets_API_Test")
    file1 = '2020ohmv.csv'
    file2 = '2020ohmv_matches.csv'
    file3 = '2020ohmvpr.csv'
    content = open(file1, 'r').read()
    content = content + open(file2, 'r').read()
    content = content + open(file3, 'r').read()
    gc.import_csv('1zai9_t9VZikNr594JIlGy6PBNQ3tipCi-_mOraNGzPk', content)

