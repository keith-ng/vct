import pandas as pd
import streamlit as st
import time
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import io

st.set_page_config(page_title="Project X", layout="wide")

### import all the functions in deployment.ipynb 
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

# retrieve max duration of each round
def min_secs(user_inputted_round):
    return int(full.loc[full['round'] == user_inputted_round]['secs'].min())

def max_secs(user_inputted_round):
    return int(full.loc[full['round'] == user_inputted_round]['secs'].max())

def min_secs_spike(user_inputted_round):
    return int(full.loc[full['round'] == user_inputted_round]['secs_spike'].min())

def max_secs_spike(user_inputted_round):
    return int(full.loc[full['round'] == user_inputted_round]['secs_spike'].max())

# next frame function
def next_frame():
    count = 0
    try:
        # increase time count by 1
        st.session_state.time_slider +=1
        count += 1

        # Empty the containers, so images do not accumulate
        abox.empty()
        mm.empty()

        # Execute function to get the frame of the current time on the slider
        abil(map_input, round_input,time_input+count, spike_planted_input)
        minimap(map_input, round_input,time_input+count, spike_planted_input)

        # Display minimap image
        with col2:
            img = Image.open('mm_m' + str(map_input)+'_r' + str(round_input) + '_t'+str(time_input+count) + '_sp'+str(spike_planted_input)+'.png')
            with mm:
                st.image(img, use_column_width = True)

         # Display abilities tracker image
        with col3:
            img = Image.open('at_m'+str(map_input)+'_r' + str(round_input)+'_t'+str(time_input+count)+'_sp'+str(spike_planted_input)+'.png')
            with abox:
                st.image(img, use_column_width = True)
    except:
        pass
    
# previous frame function
def prev_frame():
    count = 0
    try:
        # increase time count by 1
        st.session_state.time_slider -=1
        count += 1

        # Empty the containers, so images do not acculumate
        abox.empty()
        mm.empty()

        # Execute function to get the frame of the current time on the slider
        abil(map_input, round_input,time_input-count, spike_planted_input)
        minimap(map_input, round_input,time_input-count, spike_planted_input)

        # Display minimap image
        with col2:
            img = Image.open('mm_m' + str(map_input)+'_r' + str(round_input) + '_t'+str(time_input-count) + '_sp'+str(spike_planted_input)+'.png')
            with mm:
                st.image(img, use_column_width = True)

         # Display abilities tracker image
        with col3:
            img = Image.open('at_m'+str(map_input)+'_r' + str(round_input)+'_t'+str(time_input-count)+'_sp'+str(spike_planted_input)+'.png')
            with abox:
                st.image(img, use_column_width = True)
    except:
        pass
    

# play function to reduce 1 from time_input every second
def play():
    count = 0
    # Define boundaries for the loop
    if spike_planted_input == False:
        min_range = min_secs(round_input)
        max_range = max_secs(round_input)
    else:
#     if spike_planted_input == True:
        min_range = min_secs_spike(round_input)
        max_range = max_secs_spike(round_input)
    # Loop through range until slider reaches min value
    for i in range(min_range+1, max_range):
        if st.session_state['time_slider'] > min_range:
            st.session_state.time_slider -=1
            count += 1

            # Empty the containers, so images do not acculumate
            abox.empty()
            mm.empty()

            # Execute function to get the frame of the current time on the slider
            abil(map_input, round_input,time_input-count, spike_planted_input)
            minimap(map_input, round_input,time_input-count, spike_planted_input)

            # Display minimap image
            with col2:
                img = Image.open('mm_m' + str(map_input)+'_r' + str(round_input) + '_t'+str(time_input-count) + '_sp'+str(spike_planted_input)+'.png')
                with mm:
                    st.image(img, use_column_width = True)

             # Display abilities tracker image
            with col3:
                img = Image.open('at_m'+str(map_input)+'_r' + str(round_input)+'_t'+str(time_input-count)+'_sp'+str(spike_planted_input)+'.png')
                with abox:
                    st.image(img, use_column_width = True)
            
            # Sleep to prevent epilepsy
            time.sleep(2)
        else:
            break

### user interface creation ###
st.title("Match Replay System")
# st.subheader("Select the details:")

# divide web page into 2 columns
col1, col2, col3 = st.columns([1,2,1])

with col1:
    
    st.subheader("Select the details:")
    
    ### To create a dropdown list for match input
    match_input = st.selectbox(
    'Select Match:', # input hint
    (input_match, 'More options in future')) #input options

    ### To create a dropdown list for map input
    map_input = st.selectbox(
    'Select Map:', # input hint
    (1, 2)) #input options  
    
    # Retrieve max possible rounds for the game
    input_round = int(full['round'].max())

    ### To create a slider for round input   
    round_input = st.slider("Select Round:", min_value=1, max_value=input_round, value = 1)   

    ### To create a dropdown list for map input
    
    # Show possible options for spike_planted: check whether rows in relevant rounds have false AND true and 
    if len(full.loc[full['round'] == input_round]['spike_planted'].unique().tolist()) == 1:
        spike_planted_input = st.selectbox('Is Spike Planted:', False) #input options 
    else:
        spike_planted_input = st.selectbox('Is Spike Planted:', (False, True))
        
    # Show possible values for time_input
    if spike_planted_input == False:
        time_input = st.slider("Select Time in Secs:", min_value=min_secs(round_input), max_value=max_secs(round_input), key='time_slider')
    else:
#     elif spike_planted_input == True:
        try:
            time_input = st.slider("Select Time in Secs:", min_value=min_secs_spike(round_input), max_value=max_secs_spike(round_input), key='time_slider')
        except:
            st.write('Spike was not planted this round.')
            
    st.write('Code not adjusted for first two seconds yet.')
    
#     # Create button that will be used to 'play' the images (countdown to round end)
#     result = st.button('Previous Frame', on_click=play) 
    st.button('Next Frame', on_click=next_frame)
    st.button('Previous Frame', on_click=prev_frame)
    st.write('Play button removed due to slow platform processing speed.')
    st.write('Demonstration can be found at: https://youtu.be/vfWOBPOA-zc')
    

    # Execute functions to generate initial images
    minimap(map_input,round_input,time_input, spike_planted_input)
    abil(map_input,round_input,time_input, spike_planted_input)

with col2:
    # Display current game score based on specified round
    t1s = full.loc[full['round'] == round_input].iloc[0]['team1_score']
    t2s = full.loc[full['round'] == round_input].iloc[0]['team2_score']
    st.subheader("Current Score: Leviathan: {} - Team Liquid: {}".format(int(t1s), int(t2s))) 
    
    # create st container as placeholder for minimap
    mm = st.empty()  

    # Display Positional Data Image
    
    # function saves image in specified link, thus we open the saved image
    img = Image.open('mm_m' + str(map_input)+'_r' + str(round_input) + '_t'+str(time_input) + '_sp'+str(spike_planted_input)+'.png')
    
    # display image with container we created earlier
    with mm:
        st.image(img, use_column_width = True)
    

with col3:
    st.subheader("Abilities Casted:") 
    
    # create st container as placeholder for ability box
    abox = st.empty()

    # Display Ability Tracking Image
    # st.write(abil(map_input, round_input,time_input, spike_planted_input))
    img = Image.open('at_m'+str(map_input)+'_r' + str(round_input)+'_t'+str(time_input)+'_sp'+str(spike_planted_input)+'.png')
    
    # display image with container we created earlier
    with abox:
        st.image(img, use_column_width = True)

