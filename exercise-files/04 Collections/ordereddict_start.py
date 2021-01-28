# Demonstrate the usage of OrderedDict objects
"""
An OrderedDict remembers the order in which items are inserted
"""

from collections import OrderedDict


def main():
    # list of sport teams with wins and losses
    sportTeams = [("Royals", (18, 12)), ("Rockets", (24, 6)), 
                ("Cardinals", (20, 10)), ("Dragons", (22, 8)),
                ("Kings", (15, 15)), ("Chargers", (20, 10)), 
                ("Jets", (16, 14)), ("Warriors", (25, 5))]

    # sort the teams by number of wins
    sortedTeams = sorted(sportTeams, key=lambda t: t[1][0], reverse=True)
    print(sortedTeams)

    # TODO: create an ordered dictionary of the teams
    teams = OrderedDict(sortedTeams)
    print(teams)

    # TODO: Use popitem to remove the top item
    # tm = team, wl = win-loss record
    tm, wl = teams.popitem(False)
    print("Top team: ", tm, wl)

    # TODO: What are next the top 4 teams?
    for i, team in enumerate(teams, start=1):
        print(i, team)
        if i == 4:
            break

    # TODO: test for equality, including order
    a = OrderedDict({"a": 1, "b": 2, "c": 3})
    b = OrderedDict({"a": 1, "b": 2, "c": 3})
    print("Equality test:", a == b)

if __name__ == "__main__":
    main()
