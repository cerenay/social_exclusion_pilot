# Social exclusion experiment
In this repository, you can find the experiment for the social exclusion pilot and the data with analyses will come in separate folders. 

## IMPORTANT PYCHARM COMMANDS

- *otree devserver* --> To see and try the demo version 

- *CTRL+C* --> To exit the demo




## How to work with the files?
You can download the files and manuanlly upload to the repository again, just like in GDrive and DB. Or you can use Github Desktop and first add the repository to your local computer. 
Afterwards you will see the differences between the online files and your local ones, you if you commit changes they will appear in both. Do not forget to write a summary for all commit so we can keep track. 

## Folders and files

In the folder "raw data" you can find the raw data from the treatment and control, in "processed data anad analyses" there are cleaned data files and analyses files in markdown form. 

*raw data :* The whole game is splitted into apps to avoid unnecessary data crowd. "exclusion", "exclusion_control" and "dictator" are the ones for beneficiary rounds and the DG. In exclusion, "player.points" is the outcome from the beneficiary rounds in terms of points (in total 40), "player.first_income" shows whether they were chosen as the beneficiary in the first round, so the total payoff is point+first_income. There are many variables for JS calculations, so they can be ignored. player.exclusion	player.inclusion	player.own_team	player.other_team	player.fair	player.fair_benef	player.fair_benef_own	player.fair_benef_other	player.rejected	player.happy	player.well_being are the survey questions at the end of beneficiary rounds. 

In *dictator*, there is a variable called "player.send_proxy" this if for the players who were not assigned to the dictator role. And "group.sent" is the sent amount by the dictator in that particular group. To find groups, check "group.id_in_subsession" and for roles "player.id_in_group", 1 if dictator 2 if recipient. 

When working with raw data, you should filter all datasets to "player.page=="submission_prolific" to have data from those who completed the game.

In the "processed data" you can find datasets reformulated and cleaned form extra variables and filtered to the ones who finished the game. 


# Updated design and analysis from Summer 2025 

From summer 2025, we use the folder 2020_design_and_experiment. All the relevant files are listed in that directory and can be used easily. 
## Folders 
Literature: Papers 
Design: Docs for the design 
Analysis: Just for the future data and analysis files. 
experiment_code: Code for the experiment

## Experiment structure and files 

To see the experiment code and make changes on the pages for into the **experiment_code** folder.

The experiment consists of 3 apps_ painting_choice, counting_matrix and dictator. 
The painting choice is the first stage of the experiments where participants choose painting, counting_matrix is the slider task that they are completing and dictator is the dictator game at the end. 

The pages are the html extensioned files and the instructions in them can be edited easily. Page structure is as follows:

### 1. Painting Choice App (painting_choice)

Pages:

Welcome

Introductory page.

Prepares participants for the painting preference task.

PaintingChoice

Shows 5 pairs of paintings (each with A and B, where A = Klee, B = Kandinsky).

Participants select a preferred painting in each pair.

Choices saved as painting_choice_1 to painting_choice_5.

Transition

Calculates how many "A" (Klee) choices were made.

If participant chose "A" at least 3 times, they are assigned to group Klee, otherwise Kandinsky.

Stored as participant.vars['painting_group'].

### 2. Counting Matrix App (counting_matrix)

Pages:

Instructions

Describes task: moving sliders to estimate correct value.

Tells about valid range and difficulty.

MatrixTask

Participants complete 5 sliders.

Slider ranges are based on task difficulty (easy: 40-60, hard: 50-55).

Slider values stored in slider1 to slider5.

The number of correct answers is saved in correct_zeros.

Results

Displays participant slider inputs.

Shows how many were within the correct range based on difficulty.

### 3. Dictator Game App (dictator_strategy)

Pages:

Introduction

Brief overview of the game and how decisions will be made.

Offer

Participants playing the role of allocator make 3 decisions upfront:

Round 1: Unconditional allocation.

Round 2: Based on recipient's group.

Round 3: Based on recipient's task difficulty.

Future extensions may include Rounds 4 and 5.

WaitForAll

Waits until all participants have submitted their decisions.

Randomly selects one round.

Sets payoffs based on the decision made in that round.

Results

Shows participants:

Which round was selected.

How much was sent and kept.

Their final payoff.

