import pandas as pd
import streamlit as st
import time
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

st.set_page_config(page_title="Project X", layout="wide")

### import all the functions in deployment_draft.ipynb
from ipynb.fs.full.Deployment import *

### variable declaration and initialisation ###
input_match = 'VCT Champions 2022: Liquid vs Leviathan'

# variable will be used to map to the relevant csv file
input_map = 1 
input_game = input_match + '_m' + str(input_map) 

# Load default relevant templates
game_map = 'assets/haven.png' 
abil_box = 'assets/abilities/template_long.png'

# Retrieve default max round of each game
full = pd.read_csv('liq_lev_m' + str(input_map) + '_md_final.csv')
positions = pd.read_csv('liq_lev_m' + str(input_map) + '_pl_final.csv')
input_round = int(full['round'].max())

# function to retrieve max duration of each round
def min_time(user_inputted_round):
    return int(full.loc[full['round'] == user_inputted_round]['secs'].max())

def max_time(user_inputted_round):
    return int(full.loc[full['round'] == user_inputted_round]['secs'].min())

### user interface creation ###
st.title("Game Analysis")
st.subheader("Select your details:")

# divide web page into 2 columns
col1, col2 = st.columns([1,2])

with col1:
    ### To create a dropdown list for match input
    match_input = st.selectbox(
    'Select Match:', # input hint
    (input_match, 'More options in future')) #input options

    ### To create a dropdown list for map input
    map_input = st.selectbox(
    'Select Map:', # input hint
    (1, 2)) #input options 
    
    # Display final score of the map
    t1s = full['team1_score'].max()
    t2s = full['team2_score'].max()
    # Final frame may be cleaned due to noise, < 12 necessary in case of OT
    if t1s == 12 and t2s < 12:
        t1s +=1
    elif t2s == 12 and t1s < 12:
        t2s +=1   
    st.write("Final Score: Leviathan: {} - Team Liquid: {}".format(int(t1s), int(t2s))) 

    ### To create a dropdown list for team input
    team_input = st.selectbox(
    'Select Team:', # input hint
    ('team_liquid', 'leviathan')) #input options  

    ### To create a dropdown list for side input
    side_input = st.selectbox(
    'Select Side:', # input hint
    ('atk', 'def')) #input options  

    ### To create a dropdown list for agent input
    if map_input == 1:
        agent_input = st.selectbox(
        'Select Agent', # input hint
        ('omen', 'fade', 'raze', 'breach', 'chamber')) #input options
        
#     elif map_input == 2:
    else:
        if team_input == 'team_liquid':
            agent_input = st.selectbox(
            'Agent', # input hint
            ('omen', 'fade', 'phoenix', 'kayo', 'chamber')) #input options
        else:
#         if team_input == 'leviathan':
            agent_input = st.selectbox(
            'Agent', # input hint
            ('astra', 'fade', 'kayo', 'sova', 'chamber')) #input options
            
    image_input = st.selectbox(
    'Image Type:', # input hint
    ('Heatmap', 'Positions'))  
        
with col2:

    if image_input == 'Positions':
        img = Image.open('preload/pos_m' + str(map_input)+ '_' + str(team_input) + '_'+str(side_input) + '_'+str(agent_input)+'.png')
        st.image(img, use_column_width = True)

    if image_input == 'Heatmap':
        img = Image.open('preload/hm_m' + str(map_input)+ '_' + str(team_input) + '_'+str(side_input) + '_'+str(agent_input)+'.png')
        st.image(img, use_column_width = True)

       
