

import numpy as np
import nashpy as nash

payoff_matrix_a = np.array([[2, 0], [1, 1]])
payoff_matrix_b = np.array([[2, 1], [0, 1]])

game = nash.Game(payoff_matrix_a, payoff_matrix_b)

equilibria = list(game.support_enumeration())

for eq in equilibria:
    print("Nash Equilibrium:")
    print(f"Hunter A's mixed strategy: {eq[0]}")
    print(f"Hunter B's mixed strategy: {eq[1]}")

    payoff_a = np.dot(eq[0], np.dot(payoff_matrix_a, eq[1]))
    payoff_b = np.dot(eq[0], np.dot(payoff_matrix_b, eq[1]))

    print(f"Payoff for Hunter A: {payoff_a}")
    print(f"Payoff for Hunter B: {payoff_b}")
