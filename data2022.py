endgame_conversion = {
    'None': 0,
    'Low': 2,
    'Mid': 4,
    'High': 10,
    'Traversal': 15
}
BLUE, RED = 'blue', 'red'
AUTO, TELE = 'auto', 'teleop'
low_auto_points, high_auto_points, low_tele_points, high_tele_points = 2,4,1,2
CARGO_LOW, CARGO_HIGH, TAXI, CLIMBING = 'scoring0', 'scoring1', 'scoring2', 'scoring3'

def create_data_dict_2022():
    return {
        'general':{
            'autoPoints': [],
            'teleopPoints': [],
            'foulPoints': [],
            'totalPoints': []
        },
        'auto': {
            CARGO_LOW: [],
            CARGO_HIGH: [],
            TAXI: 0
        },
        'teleop': {
            CARGO_LOW: [],
            CARGO_HIGH: [],
        },
        'endgame': {
            CLIMBING: []
        }
    }


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


def general_points(match, data_dict):
    data_dict['general']['autoPoints'].append(match['score_breakdown']['blue']['autoPoints'])
    data_dict['general']['autoPoints'].append(match['score_breakdown']['red']['autoPoints'])
    data_dict['general']['teleopPoints'].append(match['score_breakdown']['red']['teleopPoints'])
    data_dict['general']['teleopPoints'].append(match['score_breakdown']['blue']['teleopPoints'])
    data_dict['general']['foulPoints'].append(match['score_breakdown']['red']['foulPoints'])
    data_dict['general']['foulPoints'].append(match['score_breakdown']['blue']['foulPoints'])
    data_dict['general']['totalPoints'].append(match['score_breakdown']['red']['totalPoints'])
    data_dict['general']['totalPoints'].append(match['score_breakdown']['blue']['totalPoints'])


def auto_points(match, data_dict):
    data_dict['auto'][CARGO_LOW].append(calc_lower_hub_amount(match, BLUE, AUTO))
    data_dict['auto'][CARGO_LOW].append(calc_lower_hub_amount(match, RED, AUTO))
    data_dict['auto'][CARGO_HIGH].append(calc_upper_hub_amount(match, BLUE, AUTO))
    data_dict['auto'][CARGO_HIGH].append(calc_upper_hub_amount(match, RED, AUTO))
    data_dict['auto'][TAXI] += int(match['score_breakdown'][BLUE]['autoTaxiPoints']) / 2
    data_dict['auto'][TAXI] += int(match['score_breakdown'][RED]['autoTaxiPoints']) / 2


def tele_points(match, data_dict):
    data_dict['teleop'][CARGO_LOW].append(calc_lower_hub_amount(match, BLUE, TELE))
    data_dict['teleop'][CARGO_LOW].append(calc_lower_hub_amount(match, RED, TELE))
    data_dict['teleop'][CARGO_HIGH].append(calc_upper_hub_amount(match, BLUE, TELE))
    data_dict['teleop'][CARGO_HIGH].append(calc_upper_hub_amount(match, RED, TELE))


def endgame_points(match, data_dict):
    data_dict['endgame'][CLIMBING].append(endgame_conversion[match['score_breakdown'][RED]['endgameRobot1']])
    data_dict['endgame'][CLIMBING].append(endgame_conversion[match['score_breakdown'][RED]['endgameRobot2']])


def match_data_20222(match, data_dict):
    if match['score_breakdown'] is not None:
        general_points(match, data_dict)
        auto_points(match, data_dict)
        tele_points(match, data_dict)
        endgame_points(match, data_dict)

