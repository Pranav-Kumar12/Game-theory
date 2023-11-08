# Prisoner's Dilemma
# C,C : -3,-3     C,D : 0,-4      D,C : -4,0      D,D : -1,-1

import numpy as np
import nashpy as nash

print("First Strategy : Confess")
print("Second Strategy : Deny")
print("Enter Prisoner 1's payoff :")
Player_1 = []
for i in range(2):
    l2 = []
    for j in range(2):
        l2.append(int(input()))
    Player_1.append(l2)
print()
print("Enter Prisoner 2's payoff :")
Player_2 = []
for i in range(2):
    l4 = []
    for j in range(2):
        l4.append(int(input()))
    Player_2.append(l4)
print()  

# 1st strategy: confess
# 2nd strategy: deny
game = nash.Game(Player_1,Player_2)
nash_eq = game.support_enumeration()

print("Nash Equilibria:")
for eq in nash_eq:
    p1 = eq[0]
    p2 = eq[1]
    
    p1Payoff = game[eq][0]
    p2Payoff = game[eq][1]
    
    print("Prisoner 1 strategy: ", p1)
    print("Prisoner 2 strategy: ", p2)
    print("Prisoner 1 payoff: ", p1Payoff)
    print("Prisoner 2 payoff: ", p2Payoff)
