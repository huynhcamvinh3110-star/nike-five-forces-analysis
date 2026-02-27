# Five Forces scores for Nike

forces = {
    "Competitive Rivalry": 5,
    "Threat of New Entrants": 2,
    "Bargaining Power of Suppliers": 3,
    "Bargaining Power of Buyers": 4,
    "Threat of Substitutes": 3
}

average_score = sum(forces.values()) / len(forces)

print("Five Forces Analysis - Nike")
print("-----------------------------")

for force, score in forces.items():
    print(f"{force}: {score}")

print("\nAverage Industry Pressure:", round(average_score, 2))

if average_score >= 4:
    level = "Very High Competition"
elif average_score >= 3:
    level = "High Competition"
elif average_score >= 2:
    level = "Moderate Competition"
else:
    level = "Low Competition"

print("Industry Level:", level)
