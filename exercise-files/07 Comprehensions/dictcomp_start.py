# Demonstrate how to use dictionary comprehensions


def main():
    # define a list of temperature values
    ctemps = [0, 12, 34, 100]

    # TODO: Use a comprehension to build a dictionary
    tempDict = {t: (t*9/5) +32 for t in ctemps if t < 100}
    print(tempDict)
    print(tempDict[12])

    # TODO: Merge two dictionaries with a comprehension
    team1 = {"Jones": 24, "Jameson": 18, "Smith": 58, "Burns": 7}
    team2 = {"White": 12, "Macke": 88, "Perce": 4}

    # The items () method returns a view object.
    # The view object contains the key-value pairs of the dictionary,
    # as tuples in a list
    newTeam = {k:v for team in (team1, team2) for k,v in team.items()}
    print(newTeam)

if __name__ == "__main__":
    main()
