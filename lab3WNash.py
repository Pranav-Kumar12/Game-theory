import numpy as np

pMatA = np.array([[2, 0], [1, 1]])

pMatB = np.array([[2, 1], [0, 1]])

num_strategies = len(pMatA)

nash_equilibria = []

choice = ["Deer", "Rabbit"]

for strategy_a in range(num_strategies):
    for strategy_b in range(num_strategies):
        expected_payoff_a = sum(pMatA[strategy_a] * np.array(
            [1 if i == strategy_b else 0 for i in range(num_strategies)]))
        expected_payoff_b = sum(pMatB[strategy_b] * np.array(
            [1 if i == strategy_a else 0 for i in range(num_strategies)]))

        if expected_payoff_a >= max(pMatA[:, strategy_b]) and expected_payoff_b >= max(pMatB[:, strategy_a]):
            nash_equilibria.append(
                ((strategy_a, strategy_b), (expected_payoff_a, expected_payoff_b)))

if len(nash_equilibria) == 0:
    print("No Nash Equilibrium")
else:
    print("Nash Equilibria:")
    for eq, payoffs in nash_equilibria:
        print(f"Hunter A's strategy: {choice[eq[0]]}")
        print(f"Hunter B's strategy: {choice[eq[1]]}")
        print(f"Payoff for Hunter A: {payoffs[0]}")
        print(f"Payoff for Hunter B: {payoffs[1]}")
