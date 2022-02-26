import Graph


def general_points_vis(data):
    week_data = [[],[],[],[]]
    for data_dict in data:
        auto_points = data_dict['general']['autoPoints']
        tele_points = data_dict['general']['teleopPoints']
        foul_points = data_dict['general']['foulPoints']
        auto, tele, foul, endgame = 0, 0, 0,0
        for i in range(len(auto_points)):
            endgame += data_dict['general']['totalPoints'][i] - auto_points[i] - tele_points[i] - foul_points[i]
            auto += auto_points[i]
            tele += tele_points[i]
            foul += foul_points[i]
        week_data[0].append(auto/len(auto_points))
        week_data[1].append(tele/len(tele_points))
        week_data[2].append(foul/len(foul_points))
        week_data[3].append(endgame/len(data_dict['general']['totalPoints']))
    graph = Graph.LineGraph(y=week_data[0], x=range(len(week_data[0])), other_lines=week_data[1:], labels=['auto', 'tele','foul','endgame'])
    g = graph.graph()
    g.show()