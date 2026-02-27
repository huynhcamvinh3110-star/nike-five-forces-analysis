companies = {
    "Nike": {
        "Competitive Rivalry": 5,
        "Threat of New Entrants": 2,
        "Bargaining Power of Suppliers": 3,
        "Bargaining Power of Buyers": 4,
        "Threat of Substitutes": 3
    },
    "Adidas": {
        "Competitive Rivalry": 5,
        "Threat of New Entrants": 2,
        "Bargaining Power of Suppliers": 3,
        "Bargaining Power of Buyers": 4,
        "Threat of Substitutes": 3
    }
}

def calculate_average(forces):
    return sum(forces.values()) / len(forces)

print("Five Forces Comparison")
print("----------------------")

for company, forces in companies.items():
    avg = calculate_average(forces)
    print(f"{company} Average Score: {round(avg, 2)}")
