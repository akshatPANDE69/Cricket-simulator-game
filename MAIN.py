import csv

# Batsmen data
batsmen_data = [
    ["name", "average", "strike_rate", "runs"],
    ["Virat Kohli", 53.2, 92.4, 12040],
    ["Rohit Sharma", 48.9, 88.7, 9205],
    ["Kane Williamson", 47.5, 81.8, 6173],
    ["Steve Smith", 43.3, 86.8, 4378],
    ["Joe Root", 50.1, 86.7, 6207],
    ["Babar Azam", 56.9, 88.3, 3985],
    ["David Warner", 45.1, 95.5, 5445],
    ["Quinton de Kock", 45.6, 94.5, 5135],
    ["Jonny Bairstow", 47.4, 103.0, 3454],
    ["Faf du Plessis", 47.5, 88.6, 5507],
    ["Aaron Finch", 41.9, 89.3, 5232],
    ["Shai Hope", 50.3, 75.5, 3547],
    ["Shikhar Dhawan", 45.6, 94.0, 5808],
    ["Ross Taylor", 48.2, 83.3, 8376],
    ["Jos Buttler", 40.8, 119.5, 3186],
    ["Eoin Morgan", 39.3, 93.5, 7701],
    ["KL Rahul", 44.2, 88.7, 1831],
    ["Nicholas Pooran", 42.1, 98.3, 1186],
    ["Shubman Gill", 52.6, 101.2, 1311],
    ["Tom Banton", 42.0, 95.0, 1042]
]

# Bowlers data
bowlers_data = [
    ["name", "average", "economy_rate", "wickets"],
    ["Jasprit Bumrah", 24.6, 4.5, 113],
    ["Mitchell Starc", 20.8, 5.1, 195],
    ["Kagiso Rabada", 27.3, 4.9, 126],
    ["Pat Cummins", 28.8, 5.2, 111],
    ["Trent Boult", 25.2, 5.0, 169],
    ["Shaheen Afridi", 21.8, 5.1, 62],
    ["Rashid Khan", 18.5, 4.2, 140],
    ["Yuzvendra Chahal", 25.3, 5.2, 92],
    ["Adil Rashid", 30.0, 5.6, 159],
    ["Imran Tahir", 24.8, 4.6, 173],
    ["Bhuvneshwar Kumar", 26.1, 4.9, 141],
    ["Mitchell Santner", 36.0, 4.8, 75],
    ["Nathan Coulter-Nile", 29.0, 5.5, 83],
    ["Chris Woakes", 30.5, 5.5, 155],
    ["Hasan Ali", 30.0, 5.4, 89],
    ["Jofra Archer", 23.3, 4.6, 30],
    ["Lungi Ngidi", 25.0, 5.5, 54],
    ["Mustafizur Rahman", 23.6, 5.0, 119],
    ["Mohammad Shami", 25.3, 5.6, 140],
    ["Shadab Khan", 31.5, 5.1, 62]
]

# Write batsmen data to CSV file
with open('batsmen.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(batsmen_data)

# Write bowlers data to CSV file
with open('bowlers.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(bowlers_data)
import csv
import random

# Load players from CSV files
def load_players(filename):
    players = []
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            players.append(row)
    return players

# Function to conduct the toss
def toss():
    return random.choice(['Team 1', 'Team 2'])

# Function to simulate a ball
def simulate_ball(batsman, bowler):
    run_prob = float(batsman['strike_rate']) / 100
    wicket_prob = 1 / float(bowler['average'])
    
    if random.random() < wicket_prob:
        return 'W'
    elif random.random() < run_prob:
        return random.choice([1, 2, 3, 4, 6])
    else:
        return 0

# Function to simulate an over
def simulate_over(batsman, bowler):
    over_result = []
    for ball in range(6):
        result = simulate_ball(batsman, bowler)
        over_result.append(result)
    return over_result

# Function to simulate an innings
def simulate_innings(batting_order, bowling_order):
    innings_result = []
    for over in range(20):
        batsman = batting_order[over % len(batting_order)]
        bowler = bowling_order[over]
        over_result = simulate_over(batsman, bowler)
        innings_result.append(over_result)
    return innings_result

# Function to display innings results
def display_innings(innings_result):
    for over, over_result in enumerate(innings_result):
        runs = [ball if isinstance(ball, int) else 0 for ball in over_result]
        print(f"Over {over + 1}: ", runs)

# Load players
batsmen = load_players('batsmen.csv')
bowlers = load_players('bowlers.csv')

# Randomly assign players to teams
random.shuffle(batsmen)
random.shuffle(bowlers)

team1_batsmen = batsmen[:5]
team2_batsmen = batsmen[5:10]
team1_bowlers = bowlers[:5]
team2_bowlers = bowlers[5:10]

# Input team names
team1_name = input("Enter the name for Team 1: ")
team2_name = input("Enter the name for Team 2: ")

# Display team players with their initials and numbers
print(f"\n{team1_name} Batsmen:")
for i, player in enumerate(team1_batsmen, 1):
    print(f"{i}. {player['name']} ({player['name'][:3]})")
print(f"\n{team1_name} Bowlers:")
for i, player in enumerate(team1_bowlers, 1):
    print(f"{i}. {player['name']} ({player['name'][:3]})")
print(f"\n{team2_name} Batsmen:")
for i, player in enumerate(team2_batsmen, 1):
    print(f"{i}. {player['name']} ({player['name'][:3]})")
print(f"\n{team2_name} Bowlers:")
for i, player in enumerate(team2_bowlers, 1):
    print(f"{i}. {player['name']} ({player['name'][:3]})")

# Conduct toss
toss_winner = toss()
toss_loser = team1_name if toss_winner == team2_name else team2_name
print(f"\n{toss_winner} wins the toss and decides to...")

# Let the toss winner decide whether to bat or bowl first
decision = input(f"{toss_winner}, do you want to bat or bowl first? (bat/bowl): ").strip().lower()
if decision == "bat":
    batting_team = team1_batsmen if toss_winner == team1_name else team2_batsmen
    bowling_team = team2_bowlers if toss_winner == team1_name else team1_bowlers
else:
    batting_team = team2_batsmen if toss_winner == team1_name else team1_batsmen
    bowling_team = team1_bowlers if toss_winner == team1_name else team2_bowlers

# Create a dictionary for quick lookup by initials or number
def create_initials_dict(players):
    initials_dict = {}
    for i, player in enumerate(players, 1):
        initials_dict[str(i)] = player
        initials_dict[player['name'][:3].strip()] = player
    return initials_dict

batting_dict = create_initials_dict(batting_team)
bowling_dict = create_initials_dict(bowling_team)

# Default batting and bowling orders in case of wrong input
default_batting_order = batting_team[:5]
default_bowling_order = bowling_team[:5] * 4

# Input batting order
print(f"\nChoose the batting order for {toss_winner} (use initials or number):")
batting_order = []
for i in range(5):
    player_input = input(f"Enter batsman {i + 1} initials or number: ").strip()
    batsman = batting_dict.get(player_input)
    if batsman:
        batting_order.append(batsman)
    else:
        print(f"No player found. Using default sequence for batting order.")
        batting_order = default_batting_order
        break  # Exit loop if default sequence is used

# Input bowling order
print(f"\nChoose the bowling order for {toss_loser} (use initials or number):")
bowling_order = []
for i in range(20):
    player_input = input(f"Enter bowler for over {i + 1} initials or number: ").strip()
    bowler = bowling_dict.get(player_input)
    if bowler:
        bowling_order.append(bowler)
    else:
        print(f"No player found. Using default sequence for bowling order.")
        bowling_order = default_bowling_order
        break  # Exit loop if default sequence is used

# Display batting and bowling orders
print(f"\n{toss_winner} Batting Order:")
for player in batting_order:
    print(f"{player['name']} ({player['name'][:3]})")
print(f"\n{toss_loser} Bowling Order:")
for player in bowling_order:
    print(f"{player['name']} ({player['name'][:3]})")

# Simulate match
innings_result = simulate_innings(batting_order, bowling_order)
print(f"\n{toss_winner} Innings:")
display_innings(innings_result)

# Swap teams for the second innings
batting_team_second = team2_batsmen if toss_winner == team1_name else team1_batsmen
bowling_team_second = team1_bowlers if toss_winner == team1_name else team2_bowlers

# Create new initials dictionaries for the second innings
batting_dict_second = create_initials_dict(batting_team_second)
bowling_dict_second = create_initials_dict(bowling_team_second)

# Input batting order for the second innings
print(f"\nChoose the batting order for {toss_loser} (use initials or number):")
batting_order_second = []
for i in range(5):
    player_input = input(f"Enter batsman {i + 1} initials or number: ").strip()
    batsman = batting_dict_second.get(player_input)
    if batsman:
        batting_order_second.append(batsman)
    else:
        print(f"No player found. Using default sequence for batting order.")
        batting_order_second = default_batting_order
        break  # Exit loop if default sequence is used

# Input bowling order for the second innings
print(f"\nChoose the bowling order for {toss_winner} (use initials or number):")
bowling_order_second = []
for i in range(20):
    player_input = input(f"Enter bowler for over {i + 1} initials or number: ").strip()
    bowler = bowling_dict_second.get(player_input)
    if bowler:
        bowling_order_second.append(bowler)
    else:
        print(f"No player found. Using default sequence for bowling order.")
        bowling_order_second = default_bowling_order
        break  # Exit loop if default sequence is used

# Display batting and bowling orders for the second innings
print(f"\n{toss_loser} Batting Order:")
for player in batting_order_second:
    print(f"{player['name']} ({player['name'][:3]})")
print(f"\n{toss_winner} Bowling Order:")
for player in bowling_order_second:
    print(f"{player['name']} ({player['name'][:3]})")

# Simulate second innings
innings_result_second = simulate_innings(batting_order_second, bowling_order_second)
print(f"\n{toss_loser} Innings:")
display_innings(innings_result_second)

# Function to calculate total runs scored in an innings
def calculate_total_runs(innings_result):
    total_runs = sum(sum(ball if isinstance(ball, int) else 0 for ball in over) for over in innings_result)
    return total_runs 

# Calculate total runs for both teams
team1_runs = calculate_total_runs(innings_result)
team2_runs = calculate_total_runs(innings_result_second)

# Determine the winner
if team1_runs > team2_runs:
    winner = team1_name
elif team2_runs > team1_runs:
    winner = team2_name
else:
    winner = "Match Tied"

# Display winner message and final scores
print(f"\nFinal Scores:")
print(f"{team1_name}: {team1_runs}")
print(f"{team2_name}: {team2_runs}")

print(f"\n{winner} wins the match!")

