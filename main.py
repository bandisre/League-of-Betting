import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import statsmodels.api as sm
from collections import Counter
import random
import tkinter as tk

df = pd.read_csv("full_table_-_Sheet1.csv")
df1 = df[df['Games'] >= 7]
placeBet = 0

#TOP
def Top():
  print("Top Models")
  df_top = df1[df1['Position'] == "TOP"]
  df_top = df_top.reset_index()
  df_top = df_top.assign(Win_rate=0.00)
  for x in range(0, 10):
      temp = df_top.iloc[x, 4]
      df_top.at[x, 'Win_rate'] = float(temp[0:2]) + 0.00
  df_top = df_top.assign(kda=0.00)
  for x in range(0, 10):
      temp = df_top.iloc[x, 5]
      df_top.at[x, 'kda'] = float(temp[0:2]) + 0.00
  df_top = df_top.assign(dmp=0.00)
  for x in range(0, 10):
      temp = df_top.iloc[x, 12]
      df_top.at[x, 'dmp'] = temp

  x = df_top[['kda', 'dmp']]
  y = df_top['Win_rate']
  for col in x.columns:
      plt.figure()
      plt.scatter(x[col], y)
      sns.regplot(x[col], y)
      plt.ylabel('Win_rate')
      plt.xlabel(col)
      plt.show()
  return df_top

#JUNGLE
def Jungle():
  print("Jungle Models")
  df_jg = df1[df1['Position'] == "JUNGLE"]
  df_jg = df_jg.reset_index() 

  df_jg = df_jg.assign(Win_rate=0.00)
  for x in range(0, 10):
      temp = df_jg.iloc[x, 4]
      df_jg.at[x, 'Win_rate'] = float(temp[0:2]) + 0.00
  df_jg = df_jg.assign(kp=0.00)
  for x in range(0, 10):
      temp = df_jg.iloc[x, 11]
      df_jg.at[x, 'kp'] = float(temp[0:2]) + 0.00

  df_jg = df_jg.assign(fb=0.00)
  for x in range(0, 10):
      temp = df_jg.iloc[x, 12]
      df_jg.at[x, 'fb'] = temp

  x = df_jg[['kp', 'fb']]
  y = df_jg['Win_rate']
  for col in x.columns:
      plt.figure()
      plt.scatter(x[col], y)
      sns.regplot(x[col], y)
      plt.ylabel('Win_rate')
      plt.xlabel(col)
      plt.show()  
  return df_jg

#MID
def Mid():
  print("Mid Models")
  df_mid = df1[df1['Position'] == "MID"]
  df_mid = df_mid.reset_index()

  df_mid = df_mid.assign(Win_rate=0.00)
  for x in range(0, 10):
      temp = df_mid.iloc[x, 4]
      df_mid.at[x, 'Win_rate'] = float(temp[0:2]) + 0.00

  x = df_mid[['GPM', 'DPM']]
  y = df_mid['Win_rate']
  for col in x.columns:
      plt.figure()
      plt.scatter(x[col], y)
      sns.regplot(x[col], y)
      plt.ylabel('Win_rate')
      plt.xlabel(col)
      plt.show()
  return df_mid

#ADC
def ADC ():
  print("ADC Models")
  df_adc = df1[df1['Position']=="ADC"]
  df_adc = df_adc.reset_index()

  df_adc = df_adc.assign(Win_rate=0.00)
  for x in range(0, 10):
      temp = df_adc.iloc[x, 4]
      df_adc.at[x, 'Win_rate'] = float(temp[0:2]) + 0.00

  x = df_adc[['GPM', 'CSM']]
  y = df_adc['Win_rate']
  for col in x.columns:
      plt.figure()
      plt.scatter(x[col], y)
      sns.regplot(x[col], y)
      plt.ylabel('Win_rate')
      plt.xlabel(col)
      plt.show()
  return df_adc

#SUPPORT
def Support():
  print("Support Models")
  df_sup = df1[df1['Position'] == "SUPPORT"]
  df_sup = df_sup.reset_index()

  df_sup = df_sup.assign(Win_rate=0.00)
  for x in range(0, 10):
      temp = df_sup.iloc[x, 4]
      df_sup.at[x, 'Win_rate'] = float(temp[0:2]) + 0.00

  df_sup = df_sup.assign(kp=0.00)
  for x in range(0, 10):
      temp = df_sup.iloc[x, 11]
      df_sup.at[x, 'kp'] = float(temp[0:2]) + 0.00

  x = df_sup[['kp', 'VSPM']]
  y = df_sup['Win_rate']
  for col in x.columns:
      plt.figure()
      plt.scatter(x[col], y)
      sns.regplot(x[col], y)
      plt.ylabel('Win_rate')
      plt.xlabel(col)
      plt.show()
  return df_sup

df_sup = Support()
df_top = Top()
df_mid = Mid()
df_jg = Jungle()
df_adc = ADC
#Variables + Lists
winList = []
lossList = []
userDetails = []
myTeam = []
cmdList = [
    "View Team: Allows you to view your team",
    "Bet: Allows you to place a bet", "Exit: Exits the Game",
    "Make Team: Allows you to make your team"
]
cmd = "cmd list"
wallet = 500
Teams = {
  "GG" : 30, #Golden Guardians
  "EG" : 40, #Evil Geniuses
  "TL" : 60, #Team Liquid
  "100T" : 80, #100 Theives
  "TSM" : 80, #TeamSoloMid
  "FQ" : 30, #Flyquest
  "CLG" : 40, #Counter-logic Gaming
  "IMT" : 60, #Immortals
  "DIG" :  30, #Dignitas
  "C9" : 50, #Cloud9
}

for tt, pctn in Teams.items():
  rndnum = random.randint(1,101)
  if (pctn >= rndnum):
    winList.append(tt)
  else:
    lossList.append(tt)


  
#Command Functions
def ViewTeam():
    global myTeam
    for i in myTeam:
        print(i)
    cc = str(input("Please select an option from above to view stats for "))
    count = 0
    ind = 0
    for i in myTeam:
        print(i)
        if (cc == i):
            ind = count
        count += 1
    indp = myTeam[ind].find("_")

    if (cc[indp + 1:-1] == "jg"):
        dftttt = df_jg[df_jg['Player'] == cc[0:indp]]
        print("kp: " + str(dftttt.iloc[0, 11]))
        print("fb: " + str(dftttt.iloc[0, 12]))
    elif (cc[indp + 1:-1] == "top"):
        dftttt = df_top[df_top['Player'] == cc[0:indp]]
        print("kda: " + str(dftttt.iloc[0, 5]))
        print("DMP: " + str(dftttt.iloc[0, 12]))
    elif (cc[indp + 1:-1] == "mid"):
        dftttt = df_mid[df_mid['Player'] == cc[0:indp]]
        print("GPM: " + str(dftttt.iloc[0, 10]))
        print("DMP: " + str(dftttt.iloc[0, 12]))
    elif (cc[indp + 1:-1] == "adc"):
        dftttt = df_adc[df_adc['Player'] == cc[0:indp]]
        print("CSM: " + str(dftttt.iloc[0, 9]))
        print("DMP: " + str(dftttt.iloc[0, 12]))
    elif (cc[indp + 1:-1] == "sup"):
        dftttt = df_sup[df_sup['Player'] == cc[0:indp]]
        print("kp: " + str(dftttt.iloc[0, 11]))
        print("VSPM: " + str(dftttt.iloc[0, 13]))


def MakeTeam():
    global wallet
    global myTeam
    #Displaying names based on positon chosen by user
    pst = str(
        input("What position would you like to find the player list in ? "))
    if (pst == "mid"):
        temptt = df_mid
        for x in range(0, 10):
            print(df_mid.iloc[x, 1])
    elif (pst == "top"):
        temptt = df_top
        for x in range(0, 10):
            print(df_top.iloc[x, 1])
    elif (pst == "jg"):
        temptt = df_jg
        for x in range(0, 10):
            print(df_jg.iloc[x, 1])
    elif (pst == "adc"):
        temptt = df_adc
        for x in range(0, 10):
            print(df_adc.iloc[x, 1])
    elif (pst == "sup"):
        temptt = df_sup
        for x in range(0, 10):
            print(df_sup.iloc[x, 1])

    player_choice = str(input("Please select a player from the list above "))
    tempdf = temptt[temptt['Player'] == player_choice]
    ttttttttt = tempdf.iloc[0, 4]
    ttttttttt = ttttttttt[0:2]
    ww = int(ttttttttt)
    
    ss = player_choice + "_" + pst + " "
    if (ww >= 80):
        if (wallet >= 50):
            wallet -= 50
            myTeam.append(ss)
            print("Player has been successfully added to your team roster")
        else:
            print("You do not have enough points in your wallet")
    elif (ww >= 60):
        if (wallet >= 40):
            wallet -= 40
            myTeam.append(ss)
            print("Player has been successfully added to your team roster")
        else:
            print("You do not have enough points in your wallet")
    elif (ww >= 40):
        if (wallet >= 30):
            wallet -= 30
            myTeam.append(ss)
            print("Player has been successfully added to your team roster")
        else:
            print("You do not have enough points in your wallet")
    elif (ww >= 40):
        if (wallet >= 20):
            wallet -= 20
            myTeam.append(ss)
            print("Player has been successfully added to your team roster")
        else:
            print("You do not have enough points in your wallet")
    elif (ww >= 0):
        if (wallet >= 10):
            wallet -= 10
            myTeam.append(ss)
            print("Player has been successfully added to your team roster")
        else:
            print("You do not have enough points in your wallet")
    
def Bet():
  global lossList
  global winList
  global wallet
  global placeBet
  print("You currently have " + str(wallet) + " Points")
  print("How much would you like to bet?")
  placeBet = int(input("Enter Amount:"))
  if placeBet > wallet:
    print("Insufficient Points")
  else:
    print("What team would you like to bet on, please enter the offical abbrevation?")
    print("Offical abbreviations: GG, EG, TL, 100T, TSM, FQ, CLG, IMT, DIG, C9")
    bet = input("Enter team name: ")
    status = False
    st1 = 0
    for i in winList:
         if (st1!=0):
                if(bet == i):
                    status = True
                    st1+=1
    if status == True:
        wallet = wallet + placeBet
        print("You have won! Your new balance is: " + str(wallet))
    else:
        wallet = wallet - placeBet
        print("You have lost! Your new balance is: " + str(wallet))
    
      
        


#GamePlay
print("Insert Name of Game")
userName = input("Please input your UserName: ")

def onclick():
    MakeTeam()

def onclick2():
    ViewTeam()

def onclick3():
    Bet()
    
def onclick4():
    exit()
        
root = tk.Tk()
root.title("League of Legends Betting App")

but1 = tk.Button(root, text="Make Team",command=onclick)
but2 = tk.Button(root, text="View Team",command=onclick2)
but3 = tk.Button(root, text="Place Bet",command=onclick3)
but4 = tk.Button(root, text="Exit",command=onclick4)
T = tk.Text(root, height=2, width=30)

but1.pack()
but2.pack()
but3.pack()
but4.pack()
T.pack()
T.insert(tk.END, "  Starting Wallet Balance: " + str(wallet))
root.configure(background='white')
root.mainloop()





