### Project X - Valorant Match Analyses (VCT Champions 2022 - Istanbul)

Hosted on Streamlit: [Check it out here](https://keith-ng-vct-analysis-overview-gm5wxq.streamlit.app/replay_system)

### TLDR:

- Extracted positional data of over 10 object classes from videos using YOLOv7
- Obtained information from over 20 data points using optical character recognition and computer vision
- Combined and cleaned both datasets before generating movement heatmaps using a density plot
- Created a replay system with features that address current pain points verified by KOLs

![Alt text](assets/examples/process.PNG?raw=true "Process Description")

### Description:

- As a veteran FPS gamer who currently plays Valorant, I find the current features offered by existing analytics & insights platforms lacking.
- This project seeks to bridge this gap and hopefully move this market segment towards a more exhaustive product offering by such platforms.

- It uses video analysis to gain insights into the strategies and playstyles of professional Valorant teams. 
    - The scope of games will tentatively be limited to the Valorant Tournament: VCT Champions 2022 - Istanbul.
- These insights can be interpreted through the display of movements, heatmaps, and a pseudo-replay system provided by this project.
    - The pseudo-replay system also provides an ability tracker that includes the abilities that were casted at the specified second including the past two seconds for reference.

### Process:

1. Verified pain points with industry experts such as (ex)professional coaches
2. Gameplay videos were downloaded for analysis purposes
3. Cropped portions of the video that will be analysed
4. Used YOLOv7 for frame-by-frame object detection for object coordinates
    - Annotated over 1400 images to train model
    - Parameters: 100 Epochs, batch size of 16
5. Used Tesseract OCR to extract time for frames
    - Preprocessed images differently to increase OCR accuracy
        - eg. greyscale, invert, adaptive thresholding
6. Used computer vision to determine the count of circles per frame to track abilities
7. Data Cleaning
    - Extensive data cleaning as dropping all null values is not an option
8. Launched an app as a proof of concept
    - [Streamlit](https://keith-ng-vct-analysis-overview-gm5wxq.streamlit.app/replay_system)


### A Simple Demonstration:

- Let's compare the difference in roles for both teams' duelist through the heatmaps.

**Team Liquid - Raze**
![Alt text](assets/examples/liq_atk_raze.PNG?raw=true "Liquid Attack Raze")
- Execution
    - Spends majority of time at Mid or towards A
    - Team's default is often include raze holding 'A Sewer' control
        - Opponents should expect raze's boom bot into sewers often
    - Common angles held as shown by dark red patches:
        - Mid Window
        - Deep A Lobby
    - A execute from 'A Sewer' likely slower than 'A Long'
        - Expect blast pack entries from 'A Long'
        - Expect a more traditional pop or contact entry from 'A Sewers'
- After site entry
    - Holds from 'graffiti'(wall close to A Link)

**Team Leviatán - Raze**
![Alt text](assets/examples/lev_atk_raze.PNG?raw=true "Leviatán Attack Raze")
- Execution
    - Spends majority of time at 'Mid'
    - Team's default include:
        - Raze holding 'C Garage' from 'Bottom Mid' (below mid door)
        - Raze holding 'A Link' from 'B Door' (B site entrance)
            - Opponents should be weary of Raze's utility at A Link based on position
    - Common angles held as shown by dark red patches:
        - Mid Window
        - Deep A Lobby
    - A execute often from 'A Long'
        - Expect an attempt at blast pack entries from 'A Long'
    - B execute often from 'Mid Courtyard'
        - Expect an attempt at blast pack towards 'B Top Site' or towards 'A Link' from Mid
        - Expect raze's grenade ability towards 'A Link'
- After site entry
    - If A, 'Hell'
    - If B, Near 'A Link'


### Challenges:

- Image Annotation
    - Objects of interest are not generic and had to be annotated from scratch.
    - Images are small, requiring the annotations to be precise which is time-consuming.
    - Due to nature of the images, there are many occluded images.

- Data Cleaning
    - Each data point is not 'independent' meaning some null values cannot be dropped without harming the integrity of the dataset.
        - This results in the necessity of extremely intensive data cleaning.
    - Images cleaning require various image preprocessing techniques in order to obtain a respectable accuracy.

### Limitations:

- Occluded Images
    - Input data have no means of identifying object that are significantly occluded
        - This occurrence however, is expected given the nature of the game Valorant.
            1. Grouping up as a team
            2. Maps with 'floors' (multiple spots from a vertical perspective)

### Future Improvements

1. Include Agent 'Astra' Abilities
2. More Matches
3. Introduce new relevant objects
    1. Abilities' Locations
    2. Ultimate Ability Tracker
    3. Through Offical API
        - Kill Feed
        - Round Economy
4. Larger Training Dataset of Images
    - inc. Parameter Tuning if necessary
 
### Files used:

- liq_lev_m1_md_final.csv -- Cleaned match data from Liquid vs Leviatán map 1.
- liq_lev_m1_pl_final.csv -- Cleaned location data from Liquid vs Leviatán map 1.
- liq_lev_m2_md_final.csv -- Cleaned match data from Liquid vs Leviatán map 2.
- liq_lev_m2_pl_final.csv -- Cleaned location data from Liquid vs Leviatán map 2.

### License:

- GNU General Public License v3.0

### Project Status:
- On Hiatus.
