def predict_playoff_matches(contributions, alliances):
    """
    1v8, 2v7, 3v6, 4v5
    1/8 v 4/5, 3/6 v 2/7
    """
    pass


def pick_order(allainces, snake=True, picks=24):
    p_order = []
    for i in range(8):
        for k in range(2):
            p_order.append(allainces[i][k])
    for k in reversed(range(8)):
        p_order.append(allainces[k][-1])
    return p_order


def convert_cont_list_to_dict(contributions):
    t_dict = {}
    for team in contributions:
        t_dict[team[0]] = team[1]
    return t_dict


def draft_efficiency(contributions, alliances, event):
    """See how many points team could have drafted instead
    receive + if they drafted best team.  Amount based on next best team available
    receive - if they do not choose best team available. Amount is based on best team available"""
    if not alliances:
        return
    print(event, alliances)
    draftpick_order = pick_order(alliances)
    alliance_eff = [0]*len(alliances)
    pick_eff = []
    t_dict = convert_cont_list_to_dict(contributions)
    alliance_num = 0
    for i, pick in enumerate(draftpick_order):
        if pick in t_dict:
            if not (i <= 15 and i % 2 == 0):
                pick_contr = t_dict[pick]
                current_champ = 0
                for t in t_dict:
                    if t not in draftpick_order[:i+1] and (t_dict[t] > pick_contr or t_dict[t] > current_champ):
                        current_champ = t_dict[t]
                p_eff = pick_contr - current_champ
                pick_eff.append(p_eff)
                alliance_eff[alliance_num] += p_eff
        else:
            pick_eff.append(0)
            alliance_eff[alliance_num] = 0
        mod = i % 2
        if i <= 14 and mod == 1:
            alliance_num += 1
        elif i <= 15:
            i = i
        else:
            alliance_num -= 1
    print(draftpick_order)
    print(pick_eff)
    print(alliance_eff)
    f = open('scouting/' + event + '_draft_efficiency.csv', 'w')
    f.write('alliance,alliance_efficiency,captain,pick1,pick1_efficiency,pick2,pick2_efficiency\n')
    for i in range(8):
        captain = alliances[i][0]
        a_eff = alliance_eff[i]
        pick1, pick1_eff = alliances[i][1], pick_eff[i]
        pick2, pick2_eff = alliances[i][2], pick_eff[len(pick_eff)-1-i]
        f.write("{},{},{},{},{},{},{}\n".format((str(i+1)),str(a_eff),captain,pick1,str(pick1_eff),pick2,str(pick2_eff)))
    f.close()
    return alliance_eff, pick_eff
