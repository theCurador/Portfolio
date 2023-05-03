import pandas as pd
import streamlit as sl 

# load the DF
results_df = pd.read_csv('/Users/jeanzayas/Desktop/Divergence/Portfolio/Sports_Analysis/Basketball/NBA/Goat_results.csv')

# Define a function to display the box score for a single game
def display_boxscore(game_index):
    sl.write(f"### Game {game_index+1} Box Score")
    sl.write("Lebron")
    sl.write(f"Points: {results_df.iloc[game_index]['Lebron Pts']}")
    sl.write(f"Rebounds: {results_df.iloc[game_index]['LJ Total Reb']}")
    sl.write(f"3-Pts: {results_df.iloc[game_index]['LeBron 3PPGG']}")
    sl.write(f"Blocks: {results_df.iloc[game_index]['LeBron Blocks']}")
    sl.write(f"Steals: {results_df.iloc[game_index]['LeBron Steals']}")
    sl.write("")
    sl.write("Jordan")
    sl.write(f"Points: {results_df.iloc[game_index]['MJ pts']}")
    sl.write(f"Rebounds: {results_df.iloc[game_index]['MJ Total Reb']}")
    sl.write(f"3-Pointers: {results_df.iloc[game_index]['Jordan 3PPG']}")
    sl.write(f"Blocks: {results_df.iloc[game_index]['Jordan Blocks']}")
    sl.write(f"Steals: {results_df.iloc[game_index]['Jordan Steals']}")

# Define a function to display the overall recap
def display_recap():
    sl.write("### Overall Recap")
    sl.write(f"Simulated Games: {results_df.shape[0]}")
    sl.write(f"LeBron wins: {results_df['LeBron wins:']}")
    sl.write(f"Jordan wins: {results_df['Jordan wins:']}")
    sl.write(f"LJ WIN prob: {results_df['LJ WIN prob'].mean():.2%}")
    sl.write(f"MJ WIN prob: {results_df['MJ WIN prob'].mean():.2%}")
    
# Add a search bar for game number 
game_number = sl.text_input("Enter a game number (1 and 20,000) :", "1")
try: 
    game_index = int(game_number) - 1 # Convert to 0- based index
    if game_index >= 0 and game_index < results_df.shape[0]:
        display_boxscore(game_index)
    else:
        sl.write("Invalid game number")  
except: 
    sl.write("Please enter a valid integer for the game number")
display_recap()
