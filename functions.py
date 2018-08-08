"""
-------------------------------------------------------
name: searchFunc
Author:  Matthew Wong, Kevin Tang
ID:      160624580, 110511280
Email:   wong4580@mylaurier.ca, tang1280@mylaurier.ca
Version: 2018-08-08
-------------------------------------------------------
Description: Creates a list of the top picks of beers
inputs:
    beers: a list of unsorted beers
    filters: a dictionary object of the filters that are sent in
return:
    sortedBeers: a list of tuples sorted by accuracy [beer, accuracy]
-------------------------------------------------------
"""
def searchFunc(beers, filters):
    tempBeers = []
    # print(beers)
    # print(filters)
    numFilters = len(filters)
    for beer in beers:
        # for now, beer.containerType and beer.taste do not exist
        accuracy = 0
        if filters["alcoholVolume"] != "":
            difference = abs(filters["alcoholVolume"] - beer.alcoholVolume)
            accuracy += 1 - difference / (filters["alcoholVolume"]+beer.alcoholVolume)
        if beer.brandName == filters["brandName"] and filters["brandName"] != "":
            accuracy += 1
        #if beer.countryOfOrigin == filters["countryOfOrigin"] and filters["countryOfOrigin"]!="":
         #   accuracy+=1
        if beer.bodyTypeName == filters["bodyTypeName"] and filters["bodyTypeName"] != "":
            accuracy += 1
        #if beer.colourName == filters["colourName"] and filters["colourName"] !="":
         #   accuracy +=1

        if beer.containerType == filters["containerType"] and len(filters["containerType"]) != 0:
            numTypes = len(filters["containerType"])
            for containerType in filters["containerType"]:
                for beerContainerType in beer.containerType:
                    if beerContainerType == containerType:
                        accuracy += 1/numTypes


        if beer.taste == filters["taste"] and len(filters["taste"])!=0:
            numTaste = len(filters["taste"])
            for taste in filters["taste"]:
                for beerTaste in beer.taste:
                    if beerTaste == taste:
                        accuracy += 1 / numTaste

        # -2 because we don't have containerType and taste working yet
        tempBeers.append([beer, accuracy/(numFilters)])

    insertionSort(tempBeers)
    sortedBeers = []
    sortedAccuracies =[]
    for beer in tempBeers:
        sortedBeers.append(beer[0])
        sortedAccuracies.append(beer[1])

    return {"beers":sortedBeers, "accuracy":sortedAccuracies}

def insertionSort(alist):
   for index in range(1,len(alist)):

    currentvalue = alist[index]
    position = index

    while position>0 and alist[position-1][1]<currentvalue[1]:
        alist[position]=alist[position-1]
        position -=1

    alist[position]=currentvalue
   return
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
<<<<<<< HEAD
return:   top_picks: a  2dlist of beer objects, and theirs ratings
            with max size 6x2.

=======
return:   top_picks: a 2d list of beers with max size 6x2.
            the beer_id then the rating
>>>>>>> c2d59e8054f7659ea8930505e21692a21072a374
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
