#ChiSquared
#This code will calculate chi squared
#I did something similar to this for my A level geography / Computer Science Project
#I may have to break some of my anti ai rules and use a randomly generated AI dataset

import pandas as pd
df = pd.read_csv('rts_match_data.csv')
print(df.head())
#So for this example we will see if console choice affects civ choice since the structure is weird lets begin by giving "opponent" and "player" their own rows
player_df = df[['Player_Device','Player_Civ']].copy()
#change column names for when we union the data 
player_df.columns = ['Device', 'Civ']
#same steps but now for opponent
opponent_df = df[['Opponent_Device', 'Opponent_Civ']].copy()
opponent_df.columns = ['Device', 'Civ']
#Time to union

combined_df = pd.concat([player_df,opponent_df],ignore_index= True)
print(combined_df.head())

#A contingency table is used to help in the determination of chi squared
conting_table = pd.crosstab(combined_df['Device'],combined_df['Civ'])

print('====================== Contingency Table ======================')
print(conting_table)
print('================================================================')
#Notes for Me later to make sure my implementation is correct
#Console Row Total - 1177 (Civ with higest usage : Bio-Swarm - 20.47%)
#Handheld Row Total - 801 (Civ with highest usage: Aether Guard - 21.10%)
#PC Row Total - 1608 (Civ with highest usage: Bio-Swarm - 26.68%)
#I think this are quite balanced numbers and there will be relationship between civ and console