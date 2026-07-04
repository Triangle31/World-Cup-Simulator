import random

####################################################################
# Données initiales
####################################################################
EloDenominator_group = 300
EloDenominator_KO = 300
draw_min = 0.1
draw_max = 0.4
beta = 0.0005

Teams = [
# Group A
    {"Elo": 3697, "Team": "Mexico", "Position": "A1", "pts": 0},
    {"Elo": 3010, "Team": "South Africa", "Position": "A2", "pts": 0},
    {"Elo": 3281, "Team": "South Korea", "Position": "A3", "pts": 0},
    {"Elo": 3147, "Team": "Czechia", "Position": "A4", "pts": 0},
# Group B
    {"Elo": 3335, "Team": "Canada", "Position": "B1", "pts": 0},
    {"Elo": 3013, "Team": "Bosnia", "Position": "B2", "pts": 0},
    {"Elo": 2822, "Team": "Qatar", "Position": "B3", "pts": 0},
    {"Elo": 3639, "Team": "Switzerland", "Position": "B4", "pts": 0},

# Group C
    {"Elo": 3835, "Team": "Brazil", "Position": "C1", "pts": 0},
    {"Elo": 3674, "Team": "Morocco", "Position": "C2", "pts": 0},
    {"Elo": 2781, "Team": "Haiti", "Position": "C3", "pts": 0},
    {"Elo": 3236, "Team": "Scotland", "Position": "C4", "pts": 0},

# Group D
    {"Elo": 3488, "Team": "USA", "Position": "D1", "pts": 0},
    {"Elo": 3365, "Team": "Paraguay", "Position": "D2", "pts": 0},
    {"Elo": 3376, "Team": "Australia", "Position": "D3", "pts": 0},
    {"Elo": 3434, "Team": "Turkiye", "Position": "D4", "pts": 0},

# Group E
    {"Elo": 3634, "Team": "Germany", "Position": "E1", "pts": 0},
    {"Elo": 2723, "Team": "Curacao", "Position": "E2", "pts": 0},
    {"Elo": 3292, "Team": "Ivory Coast", "Position": "E3", "pts": 0},
    {"Elo": 3463, "Team": "Ecuador", "Position": "E4", "pts": 0},

# Group F
    {"Elo": 3746, "Team": "Netherlands", "Position": "F1", "pts": 0},
    {"Elo": 3561, "Team": "Japan", "Position": "F2", "pts": 0},
    {"Elo": 3256, "Team": "Sweden", "Position": "F3", "pts": 0},
    {"Elo": 2988, "Team": "Tunisia", "Position": "F4", "pts": 0},

# Group G
    {"Elo": 3666, "Team": "Belgium", "Position": "G1", "pts": 0},
    {"Elo": 3344, "Team": "Egypt", "Position": "G2", "pts": 0},
    {"Elo": 3373, "Team": "Iran", "Position": "G3", "pts": 0},
    {"Elo": 2803, "Team": "New Zealand", "Position": "G4", "pts": 0},

# Group H
    {"Elo": 4051, "Team": "Spain", "Position": "H1", "pts": 0},
    {"Elo": 3043, "Team": "Cabo Verde", "Position": "H2", "pts": 0},
    {"Elo": 3021, "Team": "Saudi Arabia", "Position": "H3", "pts": 0},
    {"Elo": 3475, "Team": "Uruguay", "Position": "H4", "pts": 0},

# Group I
    {"Elo": 4050, "Team": "France", "Position": "I1", "pts": 0},
    {"Elo": 3469, "Team": "Senegal", "Position": "I2", "pts": 0},
    {"Elo": 2965, "Team": "Iraq", "Position": "I3", "pts": 0},
    {"Elo": 3551, "Team": "Norway", "Position": "I4", "pts": 0},

# Group J
    {"Elo": 4055, "Team": "Argentina", "Position": "J1", "pts": 0},
    {"Elo": 3332, "Team": "Algeria", "Position": "J2", "pts": 0},
    {"Elo": 3419, "Team": "Austria", "Position": "J3", "pts": 0},
    {"Elo": 2978, "Team": "Jordan", "Position": "J4", "pts": 0},

# Group K
    {"Elo": 3800, "Team": "Portugal", "Position": "K1", "pts": 0},
    {"Elo": 3199, "Team": "DR Congo", "Position": "K2", "pts": 0},
    {"Elo": 3040, "Team": "Uzbekistan", "Position": "K3", "pts": 0},
    {"Elo": 3733, "Team": "Colombia", "Position": "K4", "pts": 0},

# Group L
    {"Elo": 3896, "Team": "England", "Position": "L1", "pts": 0},
    {"Elo": 3605, "Team": "Croatia", "Position": "L2", "pts": 0},
    {"Elo": 3136, "Team": "Panama", "Position": "L3", "pts": 0},
    {"Elo": 2962, "Team": "Ghana", "Position": "L4", "pts": 0}
]

####################################################################
# Fonctions
####################################################################

def play_game(elo_1, elo_2):
    abs_diff_elo = abs(elo_1 - elo_2)
    probD = max(draw_min, draw_max - beta * abs_diff_elo)
    probW = 1 / (1 + 10 ** ((elo_2 - elo_1) / EloDenominator_group))
    D = random.uniform(0, 1)
    W = random.uniform(0, 1)
    if probD > D:
        return 2   # Draw
    elif probW > W:
        return 1   # Team 1 wins
    else:
        return 0   # Team 2 wins.

def play_game_no_draws(elo_1, elo_2):
    probW = 1 / (1 + 10 ** ((elo_2 - elo_1) / EloDenominator_KO))
    W = random.uniform(0, 1)
    if probW > W:
        return 1     # Team 1 wins
    else:
        return 0    # Team 2 wins.

def play_game_pts(A1,A2):
    G = play_game(A1["Elo"],A2["Elo"])
    if G == 2:
        A1["pts"] += 1
        A2["pts"] += 1
    elif G == 1:
        A1["pts"] += 3
    elif G == 0:
        A2["pts"] += 3

def group_stage(A1, A2, A3, A4):
    Liste = [A1, A2, A3, A4]
    play_game_pts(A1, A2)
    play_game_pts(A1, A3)
    play_game_pts(A1, A4)
    play_game_pts(A2, A3)
    play_game_pts(A2, A4)
    play_game_pts(A3, A4)

    # Ajouter un petit nombre aléatoire pour briser l'égalité
    for equipe in Liste:
        equipe["pts_ajuste"] = equipe["pts"] + random.uniform(0, 0.05)

    # Trier les joueurs en fonction de 'pts_ajuste'
    Liste_trie = sorted(Liste, key=lambda x: x["pts_ajuste"], reverse=True)

    # Ajouter les rangs
    for rang, equipe in enumerate(Liste_trie, start=1):
        equipe["rang"] = rang

    # Supprimer la clé pts_ajuste
    for equipe in Liste_trie:
        del equipe["pts_ajuste"]

    return Liste_trie

def sort_teams_after_group_stage(lettre, rang):
    Team = next(team for team in Teams if team["rang"] == rang and team["Position"].startswith(lettre))
    return Team


def play_bracket(teams):
    round_number = 1
    all_winners_lists = []
    while len(teams) > 1:
        print(f"Round {round_number}:")
        next_round_teams = []
        winners_list = []

        for i in range(0, len(teams), 2):
            if i + 1 < len(teams):
                team1 = teams[i]
                team2 = teams[i + 1]
                R = play_game_no_draws(team1["Elo"], team2["Elo"])
                if R == 1:
                    winner = team1
                    loser = team2
                if R == 0:
                    winner = team2
                    loser = team1
                print(f"{winner["Team"]}  wins vs  {loser["Team"]}")
                next_round_teams.append(winner)
                winners_list.append(winner["Team"])
            else:
                print(f"{teams[i]} gets a bye to the next round")
                next_round_teams.append(teams[i])

        all_winners_lists.append(winners_list)
        teams = next_round_teams
        round_number += 1
        print()
    return all_winners_lists

def afficher_tables(L):
    print("-----------------------------")
    for i in range(len(L)):
        print(L[i]["rang"],L[i]["Team"],L[i]["pts"])
    print("-----------------------------")


####################################################################
# Initialisation
####################################################################

teams_positions = ["A1", "A2", "A3", "A4", "B1", "B2", "B3", "B4",
                   "C1", "C2", "C3", "C4", "D1", "D2", "D3", "D4",
                   "E1", "E2", "E3", "E4", "F1", "F2", "F3", "F4",
                   "G1", "G2", "G3", "G4", "H1", "H2", "H3", "H4",
                   "I1", "I2", "I3", "I4", "J1", "J2", "J3", "J4",
                   "K1", "K2", "K3", "K4", "L1", "L2", "L3", "L4"]

teams_dict = {position: next(team for team in Teams if team["Position"] == position) for position in teams_positions}

####################################################################
# Group Stage
####################################################################

A = group_stage(teams_dict["A1"], teams_dict["A2"], teams_dict["A3"], teams_dict["A4"])
B = group_stage(teams_dict["B1"], teams_dict["B2"], teams_dict["B3"], teams_dict["B4"])
C = group_stage(teams_dict["C1"], teams_dict["C2"], teams_dict["C3"], teams_dict["C4"])
D = group_stage(teams_dict["D1"], teams_dict["D2"], teams_dict["D3"], teams_dict["D4"])
E = group_stage(teams_dict["E1"], teams_dict["E2"], teams_dict["E3"], teams_dict["E4"])
F = group_stage(teams_dict["F1"], teams_dict["F2"], teams_dict["F3"], teams_dict["F4"])
G = group_stage(teams_dict["G1"], teams_dict["G2"], teams_dict["G3"], teams_dict["G4"])
H = group_stage(teams_dict["H1"], teams_dict["H2"], teams_dict["H3"], teams_dict["H4"])
I = group_stage(teams_dict["I1"], teams_dict["I2"], teams_dict["I3"], teams_dict["I4"])
J = group_stage(teams_dict["J1"], teams_dict["J2"], teams_dict["J3"], teams_dict["J4"])
K = group_stage(teams_dict["K1"], teams_dict["K2"], teams_dict["K3"], teams_dict["K4"])
L = group_stage(teams_dict["L1"], teams_dict["L2"], teams_dict["L3"], teams_dict["L4"])

print("Group A")
afficher_tables(A)
print("Group B")
afficher_tables(B)
print("Group C")
afficher_tables(C)
print("Group D")
afficher_tables(D)
print("Group E")
afficher_tables(E)
print("Group F")
afficher_tables(F)
print("Group G")
afficher_tables(G)
print("Group H")
afficher_tables(H)
print("Group I")
afficher_tables(I)
print("Group J")
afficher_tables(J)
print("Group K")
afficher_tables(K)
print("Group L")
afficher_tables(L)

####################################################################
# Knockout Stage
####################################################################



A1 = sort_teams_after_group_stage("A",1)
A2 = sort_teams_after_group_stage("A",2)
B1 = sort_teams_after_group_stage("B",1)
B2 = sort_teams_after_group_stage("B",2)
C1 = sort_teams_after_group_stage("C",1)
C2 = sort_teams_after_group_stage("C",2)
D1 = sort_teams_after_group_stage("D",1)
D2 = sort_teams_after_group_stage("D",2)
E1 = sort_teams_after_group_stage("E",1)
E2 = sort_teams_after_group_stage("E",2)
F1 = sort_teams_after_group_stage("F",1)
F2 = sort_teams_after_group_stage("F",2)
G1 = sort_teams_after_group_stage("G", 1)
G2 = sort_teams_after_group_stage("G", 2)
H1 = sort_teams_after_group_stage("H", 1)
H2 = sort_teams_after_group_stage("H", 2)
I1 = sort_teams_after_group_stage("I", 1)
I2 = sort_teams_after_group_stage("I", 2)
J1 = sort_teams_after_group_stage("J", 1)
J2 = sort_teams_after_group_stage("J", 2)
K1 = sort_teams_after_group_stage("K", 1)
K2 = sort_teams_after_group_stage("K", 2)
L1 = sort_teams_after_group_stage("L", 1)
L2 = sort_teams_after_group_stage("L", 2)
Z1 = {'Elo': 0, 'Team': 'bye', 'Position': 'Z1', 'pts': 0, 'rang': 1}
Z2 = {'Elo': 0, 'Team': 'bye', 'Position': 'Z2', 'pts': 0, 'rang': 2}
Z3 = {'Elo': 0, 'Team': 'bye', 'Position': 'Z3', 'pts': 0, 'rang': 3}
Z4 = {'Elo': 0, 'Team': 'bye', 'Position': 'Z4', 'pts': 0, 'rang': 4}
Y1 = {'Elo': 0, 'Team': 'bye', 'Position': 'Y1', 'pts': 0, 'rang': 1}
Y2 = {'Elo': 0, 'Team': 'bye', 'Position': 'Y2', 'pts': 0, 'rang': 2}
Y3 = {'Elo': 0, 'Team': 'bye', 'Position': 'Y3', 'pts': 0, 'rang': 3}
Y4 = {'Elo': 0, 'Team': 'bye', 'Position': 'Y4', 'pts': 0, 'rang': 4}



# KO_Stage_Teams = [E1, Z1, I1, Z2, A2, B2, F1, C2, C1, F2, E2, I2, A1, Z3, L1, Z4,
#                   K2, L2, H1, J2, D1, Y1, G1, Y2, J1, H2, D2, G2, B1, Y3, K1, Y4]

KO_Stage_Teams = [A2, B2, F1, C2, E1, Z1, I1, Z2, G1, Z3, D1, Z4, H1, J2, K2, L2,
                  C1, F2, E2, I2, A1, Y1, L1, Y2, B1, Y3, K1, Y4, D2, G2, J1, H2]

WW = play_bracket(KO_Stage_Teams)



print(f"""
    {A2["Team"]:<10}{C1["Team"]:>122}
    {B2["Team"]:<10}{F2["Team"]:>122}
    {WW[0][0]:>25}{WW[0][8]:>83}
    {F1["Team"]:<10}{WW[0][1]:>15}{WW[0][9]:>83}{E2["Team"]:>22}
    {C2["Team"]:<10}{I2["Team"]:>122}
    {WW[1][0]:>35}{WW[4][0]:>22}{WW[1][4]:>34}
    {E1["Team"]:<10}{WW[1][1]:>25}{WW[1][5]:>55}{A1["Team"]:>42}
    {Z1["Team"]:<10}{Y1["Team"]:>122}
    {WW[0][2]:>25}{WW[3][0]:>30}{WW[0][10]:>54}
    {I1["Team"]:<10}{WW[0][3]:>15}{WW[3][1]:>30}{WW[0][11]:>54}{L1["Team"]:>22}
    {Z2["Team"]:<10}{Y2["Team"]:>122}
    
    {G1["Team"]:<10}{WW[2][0]:>35}{WW[2][2]:>27}{B1["Team"]:>60}
    {Z3["Team"]:<10}{WW[0][4]:>15}{WW[2][1]:>20}{WW[2][3]:>25}{WW[0][12]:>38}{Y3["Team"]:>25}
    {WW[0][5]:>25}{WW[0][13]:>84}
    {D1["Team"]:<10}{K1["Team"]:>122}
    {Z4["Team"]:<10}{WW[1][2]:>25}{WW[1][6]:>55}{Y4["Team"]:>45}
    {WW[1][3]:>35}{WW[1][7]:>55}
    {H1["Team"]:<10}{D2["Team"]:>122}
    {J2["Team"]:<10}{WW[0][6]:>15}{WW[0][14]:>83}{G2["Team"]:>25}
    {WW[0][7]:>25}{WW[0][15]:>84}
    {K2["Team"]:<10}{J1["Team"]:>122}
    {L2["Team"]:<10}{H2["Team"]:>122}
    
    
""")