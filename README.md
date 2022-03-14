# Social exclusion experiment
In this repository, you can find the experiment for the social exclusion pilot and the data with analyses will come in separate folders. 

## How to work with the files?
You can download the files and manuanlly upload to the repository again, just like in GDrive and DB. Or you can use Github Desktop and first add the repository to your local computer. 
Afterwards you will see the differences between the online files and your local ones, you if you commit changes they will appear in both. Do not forget to write a summary for all commit so we can keep track. 

## Folders and files

In the folder "raw data" you can find the raw data from the treatment and control, in "processed data anad analyses" there are cleaned data files and analyses files in markdown form. 

*raw data :* The whole game is splitted into apps to avoid unnecessary data crowd. "exclusion", "exclusion_control" and "dictator" are the ones for beneficiary rounds and the DG. In exclusion, "player.points" is the outcome from the beneficiary rounds in terms of points (in total 40), "player.first_income" shows whether they were chosen as the beneficiary in the first round, so the total payoff is point+first_income. There are many variables for JS calculations, so they can be ignored. player.exclusion	player.inclusion	player.own_team	player.other_team	player.fair	player.fair_benef	player.fair_benef_own	player.fair_benef_other	player.rejected	player.happy	player.well_being are the survey questions at the end of beneficiary rounds. 

In *dictator*, there is a variable called "player.send_proxy" this if for the players who were not assigned to the dictator role. And "group.sent" is the sent amount by the dictator in that particular group. To find groups, check "group.id_in_subsession" and for roles "player.id_in_group", 1 if dictator 2 if recipient. 

When working with raw data, you should filter all datasets to "player.page=="submission_prolific" to have data from those who completed the game.

In the "processed data" you can find datasets reformulated and cleaned form extra variables and filtered to the ones who finished the game. 
