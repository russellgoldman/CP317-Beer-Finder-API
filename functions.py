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
Version: 2018-08-08
-------------------------------------------------------
Description: Creates a list of the top picks of beers
inputs:  beers: a list of beers
        db: a database connection
return:   top_picks: a  2dlist of beer objects, and theirs ratings
            with max size 6x2. 
            
-------------------------------------------------------
"""
def top_picksFunc(beers,db):
    #The top picks are based on the highest rating from the home_rating table
    sql = """SELECT * from home_rating where beer_id = """
    i = 0
    n=len(beers)
    #assuming ratings, and ids cannot be negative

    top_picks = [[]]
    while i < n:
        ratingsTable = db.engine.execute(sql + str(beers[i].id))
        ratings = []
        j = 0
        for row in ratingsTable:
            ratings.append(row)
        m = len(ratings)
        total = 0
        while j < m:
            total = total + ratings[j].ratingValue
            j = j+1
        if m > 0:
            total = total/m
        for k in range(6):
            if not top_picks[k] or total > top_picks[k][1]:
                top_picks.insert(k, [beers[i], total])
                break

        i = i + 1
    return top_picks[:6]
