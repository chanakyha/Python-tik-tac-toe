from tkinter import *
from tkinter.messagebox import showinfo, showwarning
from tkinter import ttk
from Table import tk_table

clicked_ = []


def Play_with_Comp():
    global ply_turn
    button_Frame.pack(pady=5)
    print(ply_turn['text'].replace("Player Turn: ", ""))

    if not(play_with_comp_bt["text"] == "Play with Friend"):
        root.title("Playing with computer".upper())
        Player2_details.delete(0, END)
        Player2_details.insert(0, "Computer".upper())
        Player2_details.configure(state="disabled")
        play_with_comp_bt.config(text="Play with Friend")

        if ply_turn['text'].replace("Player Turn: ", "") == "COMPUTER":
            from random import randrange
            ind = randrange(0, 9)
            clicked(index=ind)

    else:
        root.title("ChanCap Tik Tok Toe Game")
        Player2_details.configure(state="enabled")
        Player2_details.delete(0, END)
        Player2_details.insert(0, "Enter Player 2 Details")
        play_with_comp_bt.config(text="Play with Computer")


clr = "lightblue"


match_results = []

root = Tk()
root.config(bg=clr)
root.title("ChanCap Tik Tok Toe Game")

Label(text="Welcome to ChanCap Tik Tok Toe Game",
      font=("Arial Bold", 32), bg=clr).pack(pady=10)
Label(text="Lets The Game Begin", font=("Arial Bold", 12), bg=clr).pack(pady=5)
turn = Label(text="Turn: X", font=("Arial Bold", 12), bg=clr)
turn.pack(pady=5)

Player_details = LabelFrame(text="Player Details",
                            padx=30, pady=20, bd=4, bg=clr)
Player_details.pack()

Player1_details = ttk.Entry(Player_details, width=25)
Player1_details.insert(0, "Enter Player 1 Details")
Player1_details.grid(row=0, column=0)

Player2_details = ttk.Entry(Player_details, width=25)
Player2_details.insert(0, "Enter Player 2 Details")
Player2_details.grid(row=0, column=1, padx=10)


def dele_1(e):
    Player1_details.delete(0, END)


def dele_2(e):
    Player2_details.delete(0, END)


Player1_details.bind("<Button-1>", dele_1)
Player2_details.bind("<Button-1>", dele_2)

ply_turn = Label(root, text=f"Player Turn: ---",
                 font=("Arial Bold", 12), bg=clr)
ply_turn.pack(pady=5)


def submit_clicked():
    global ply_turn
    if not(Player1_details.get() in ["Enter Player 1 Details", ""] and Player2_details.get() in ["Enter Player 2 Details", ""]):
        ply_turn.config(text=f"Player Turn: {Player1_details.get()}")
        button_Frame.pack(pady=5)

        def score_board():
            top = Toplevel(bg=clr)
            top.geometry("600x650")
            tl_results = Label(
                top, text=f"Total Results for {Player1_details.get() } and { Player2_details.get()}", bg=clr, font=("Arial Bold", 17))
            tl_results.pack(pady=5)
            score_tble_lst = []
            for i in range(len(match_results)):
                if not(match_results[i] == "Draw"):
                    score_tble_lst.append([i+1, f"{match_results[i]} (won)"])
                else:
                    score_tble_lst.append([i+1, "Draw"])
            score_tble = tk_table(
                top, header=["Matches", "Result"], list=score_tble_lst, colour=clr)
            score_tble.pack(pady=10)
            player_results = Label(
                top, text=f"Individual Results", bg=clr, font=("Arial Bold", 17))
            player_results.pack(pady=5)
            for i in range(len(match_results)):
                player_1_wins = match_results.count(Player1_details.get())
                player_2_wins = match_results.count(Player2_details.get())
                draws = match_results.count("Draw")
                player_1_lose = int(len(match_results)-draws-player_1_wins)
                player_2_lose = int(len(match_results)-draws-player_2_wins)
            player_results_lst = [
                ["Matches", len(match_results), len(match_results)],
                ["Wins", player_1_wins, player_2_wins],
                ["Lose", player_1_lose, player_2_lose],
                ["draws", draws, draws]
            ]

            ind_tble = tk_table(top, header=[
                                "Results", f"{Player1_details.get()}", f"{Player2_details.get()}"], list=player_results_lst, colour=clr)
            ind_tble.pack(pady=10)
        view_score_bt = ttk.Button(
            Player_details, text="View Score Board", width=20, command=score_board)
        view_score_bt.grid(row=0, column=3)
    else:
        showwarning("Ohh No", "Please Enter Player Names")


submit_bt = ttk.Button(Player_details, text="Submit ",
                       width=20, command=submit_clicked)
submit_bt.grid(row=0, column=2, padx=10)

play_with_comp_bt = ttk.Button(
    Player_details, text="Play With Computer", width=35, command=Play_with_Comp)
play_with_comp_bt.grid(row=0, column=3)


button_Frame = LabelFrame(text="Turn: X", padx=30, pady=20, bd=4, bg=clr)


def check_win():
    events = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6],
    ]

    for x in events:
        if \
            ((total_bts[x[0]]['text'] == total_bts[x[1]]['text'] == total_bts[x[2]]['text']) and
             total_bts[x[0]]['text'] != "-" and total_bts[x[1]]['text'] != "-" and total_bts[x[2]]['text'] != "-"):
            total_bts[x[0]].config(bg="gold")
            total_bts[x[1]].config(bg="gold")
            total_bts[x[2]].config(bg="gold")
            return True
        else:
            pass


def refresh_game():
    global clicked_
    total_bts = [
        row0_col_0, row0_col_1, row0_col_2,
        row1_col_0, row1_col_1, row1_col_2,
        row2_col_0, row2_col_1, row2_col_2,
    ]

    clicked_ = []

    for i in total_bts:
        i.config(text="-", bg="white", padx=50)


def clicked(index):
    global ply_turn
    global clicked_
    if not(ply_turn['text'].replace("Player Turn: ", "") == "COMPUTER"):
        clicked_.append(index)
        total_bts = [
            row0_col_0, row0_col_1, row0_col_2,
            row1_col_0, row1_col_1, row1_col_2,
            row2_col_0, row2_col_1, row2_col_2,
        ]

        if total_bts[index]["text"] == "-":

            if button_Frame["text"].split(": ")[1] == "X":
                total_bts[index].config(text="X", padx=45)
                if check_win():
                    win = ply_turn["text"].replace("Player Turn: ", "")
                    showinfo("Game Over", f"Game Won by {win}")
                    match_results.append(win)
                    refresh_game()
                else:
                    button_Frame["text"] = "Turn: O"
                    turn["text"] = "Turn: O"
                    ply_turn.config(
                        text=f"Player Turn: {Player2_details.get()}")
                    for all in total_bts:
                        if all["text"] == "-":
                            break
                    else:
                        showwarning("Game Over", "The Game Tied")
                        match_results.append("Draw")
                        refresh_game()
            else:
                total_bts[index].config(text="O", padx=42)
                if check_win():
                    win = ply_turn["text"].replace("Player Turn: ", "")
                    showinfo("Game Over", f"Game Won by {win}")
                    match_results.append(win)
                    refresh_game()
                else:
                    button_Frame["text"] = "Turn: X"
                    turn["text"] = "Turn: X"
                    ply_turn.config(
                        text=f"Player Turn: {Player1_details.get()}")
                    for all in total_bts:
                        if all["text"] == "-":
                            break
                    else:
                        showwarning("Game Over", "The Game Tied")
                        match_results.append("Draw")
                        refresh_game()
    else:
        Play_with_Comp()


row0_col_0 = Button(button_Frame, text="-", padx=50, pady=50,
                    font=("Arial Bold", 20), command=lambda: clicked(0))
row0_col_1 = Button(button_Frame, text="-", padx=50, pady=50,
                    font=("Arial Bold", 20), command=lambda: clicked(1))
row0_col_2 = Button(button_Frame, text="-", padx=50, pady=50,
                    font=("Arial Bold", 20), command=lambda: clicked(2))

row1_col_0 = Button(button_Frame, text="-", padx=50, pady=50,
                    font=("Arial Bold", 20), command=lambda: clicked(3))
row1_col_1 = Button(button_Frame, text="-", padx=50, pady=50,
                    font=("Arial Bold", 20), command=lambda: clicked(4))
row1_col_2 = Button(button_Frame, text="-", padx=50, pady=50,
                    font=("Arial Bold", 20), command=lambda: clicked(5))

row2_col_0 = Button(button_Frame, text="-", padx=50, pady=50,
                    font=("Arial Bold", 20), command=lambda: clicked(6))
row2_col_1 = Button(button_Frame, text="-", padx=50, pady=50,
                    font=("Arial Bold", 20), command=lambda: clicked(7))
row2_col_2 = Button(button_Frame, text="-", padx=50, pady=50,
                    font=("Arial Bold", 20), command=lambda: clicked(8))

row0_col_0.grid(row=0, column=0)
row0_col_1.grid(row=0, column=1)
row0_col_2.grid(row=0, column=2)

row1_col_0.grid(row=1, column=0)
row1_col_1.grid(row=1, column=1)
row1_col_2.grid(row=1, column=2)

row2_col_0.grid(row=2, column=0)
row2_col_1.grid(row=2, column=1)
row2_col_2.grid(row=2, column=2)

total_bts = [
    row0_col_0, row0_col_1, row0_col_2,
    row1_col_0, row1_col_1, row1_col_2,
    row2_col_0, row2_col_1, row2_col_2,
]

root.mainloop()
