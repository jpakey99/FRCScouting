"""
The purpose of this file is to generate a "Pick List" / "Overall Ranking" regardless of RP
"""
from tkinter import *
from tkinter import ttk


def treeview_sort_column(treeview: ttk.Treeview, col, reverse: bool):
    """
    to sort the table by column when clicking in column
    """

    data_list = [(treeview.set(k, col), k) for k in treeview.get_children("")]

    data_list.sort(reverse=reverse)
    print(data_list)

    # rearrange items in sorted positions
    for index, (val, k) in enumerate(data_list):
        treeview.move(k, "", index)

    # reverse sort next time
    treeview.heading(
        column=col,
        text=col,
        command=lambda _col=col: treeview_sort_column(
            treeview, _col, not reverse
        ),
    )


def power_rankings2022(data):
    w = 110
    H = len(data)
    ws  = Tk()
    ws.title('Power Rankings')
    ws.geometry(str((90*8))+'x'+str(20*H))
    ws['bg'] = '#000000'

    game_frame = Frame(ws)
    game_frame.pack()

    columns = ('team', 'total_contribution', 'taxi%', 'auto%', 'teleop%', 'endgame%')
    my_game = ttk.Treeview(game_frame, columns=columns, show='headings')

    for col in columns:
        my_game.column(col, width=w)
        my_game.heading(col,anchor=CENTER, text=col, command=lambda _col=col: \
            treeview_sort_column(my_game, _col, False))

    i = 0
    for d in data:
        tc = round((d[1])/100,4)
        taxi = round(d[2]/d[1] , 2)
        auto = round(d[3] / d[1] , 2)
        tele = round(d[4] / d[1] , 2)
        end = round(d[5] / d[1] , 2)
        my_game.insert(parent='', index='end', iid=i, text='', values=(d[0], tc, taxi, auto, tele, end))
        i += 1

    my_game.pack()

    ws.mainloop()

