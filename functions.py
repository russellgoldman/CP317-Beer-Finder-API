def searchFunc(beers, filters):
    accuracies = []
    # accuracies is a list of the percentage matching to the filters
    # if beer #2 of 4 matches 3/5 of the filters passed in,
    # accuracies will be [0,0.6,0,0]

    numFilters = 0
    for filter in filters:
        if filter != "":
            numFilters += 1

    for beer in beers:
        # for now, beer.containerType and beer.taste do not exist
        i = 0
        accuracy = 0
        if beer.alcoholVolume == filters[0] and filters[0] != "":
            accuracy += 1
        if beer.brand == filters[1] and filters[1] != "":
            accuracy += 1
        if beer.bodyType == filters[2] and filters[2] != "":
            accuracy += 1
        if beer.containerType == filters[3] and filters[3] != "":
            accuracy += 1
        if beer.taste == filters[4] and filters[4] != "":
            accuracy += 1
        accuracies.append(accuracy / numFilters)

    # sort section
    high = 1
    sortedBeers = []

    # for each level of accuracy, from high to low,
    # checks all beers to see if it matches the level of accuracy and appends to sortedBeers
    # upgrade would be to skip over beers that are of a higher accuracy
    for i in range(numFilters, -1, -1):
        j = 0
        for beer in beers:
            if accuracies[j] == i / numFilters:
                sortedBeers.append(beer)

    return sortedBeers, accuracies
"""
-------------------------------------------------------
name: top_picksFunc
Author:  Jeremy Lickers
ID:      140246920
Email:   lick6920@mylaurier.ca
Version: 2018-08-07
-------------------------------------------------------
Description: Creates a list of the top picks of beers
inputs:  beers: a list of beers
return:   top_picks: a list of beers with max size 6
-------------------------------------------------------
"""
def top_picksFunc(beers):
    #The top picks are based on the highest alcoholVolume
    top_picks = []
    if not top_picks:
        i = 1
        n=len(beers)
        j = 0
        while i < n:
            while beers[i].alcoholVolume > beers[j].alcoholVolume and \
                j > -1:
                j = j - 1
            beers.insert(j,beers[i])
            i = i + 1
            beers.pop(i)
        for i in range(6):
            top_picks.append(beers[i])
    return top_picks