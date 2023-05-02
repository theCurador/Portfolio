import pandas as pd
import streamlit as sl 

# load the DF
results_df = pd.read_csv('/Users/jeanzayas/Desktop/Divergence/Portfolio/Sports Analysis/Basketball/NBA/Goat_results.csv')

# Define a function to display the box score for a single game
def display_boxscore(game_index):
    sl.write(f"### Game {game_index+1} Box Score")
    sl.write("Lebron")
    sl.write(f"Points: {results_df.iloc[game_index]['Lebron(PPG)']}")
    sl.write(f"Rebounds: {results_df.iloc[game_index]['LJ Total Reb']}")
    sl.write(f"3-Pts: {results_df.iloc[game_index]['LeBron 3PPGG']}")
    sl.write(f"Blocks: {results_df.iloc[game_index]['LeBron Blocks']}")
    sl.write(f"Steals: {results_df.iloc[game_index]['LeBron Steals']}")
    sl.write("")
    sl.write("Jordan")
    sl.write(f"Points: {results_df.iloc[game_index]['Jordan (PPG)']}")
    sl.write(f"Rebounds: {results_df.iloc[game_index]['MJ Total Reb']}")
    sl.write(f"3-Pointers: {results_df.iloc[game_index]['Jordan 3PPG']}")
    sl.write(f"Blocks: {results_df.iloc[game_index]['Jordan Blocks']}")
    sl.write(f"Steals: {results_df.iloc[game_index]['Jordan Steals']}")

# Define a function to display the overall recap
def display_recap():
    sl.write("### Overall Recap")
    sl.write(f"Simulated Games: {results_df.shape[0]}")
    sl.write(f"LeBron wins: {results_df['LeBron wins:'].sum()}")
    sl.write(f"Jordan wins: {results_df['Jordan wins:'].sum()}")
    sl.write(f"LJ WIN prob: {results_df['LJ WIN prob'].mean():.2%}")
    sl.write(f"MJ WIN prob: {results_df['MJ WIN prob'].mean():.2%}")
    
    
# Display the box score and overall recap for a selected game\
start_index = sl.slider("Select starting game:", 0, results_df.shape[0]-1) 
end_index = sl.slider("Select ending game:", 0, start_index, results_df.shape[0]-1)
for game_index in range(start_index, end_index+1):
    display_boxscore(game_index)
display_recap(start_index, end_index)
