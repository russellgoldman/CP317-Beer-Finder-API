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
    sortedBeers = []
    # accuracies is a list of the percentage matching to the filters
    # if beer #2 of 4 matches 3/5 of the filters passed in,
    # accuracies will be [0,0.6,0,0]

    numFilters = len(filters)

    for beer in beers:
        # for now, beer.containerType and beer.taste do not exist
        i = 0
        accuracy = 0
        if filters[alcoholVolume] != "":
            accuracy += 1 - abs(int(filters[alcoholVolume])-int(beer.alcoholVolume))/int(filters[alcoholVolume])
        if beer.brandName == filters[brandName] and filters[brandName] != "":
            accuracy += 1
        if beer.countryOfOrigin == filters[countryOfOrigin] and filters[countryOfOrigin]!="":
            accuracy+=1
        if beer.bodyTypeName == filters[bodyTypeName] and filters[bodyTypeName] != "":
            accuracy += 1
        if beer.colourName == filters[colourName] and filters[colourName] !="":
            accuracy +=1
        if beer.containerType == filters[containerType] and len(filters[containerType]) != 0:
            numTypes = len(filters[containerType])
            accuracy += 1
        if beer.taste == filters[4] and len(filters[taste])!=0:
            accuracy += 1
        sortedBeers.append([beer, accuracy/numFilters])
    # sort section


    # for each level of accuracy, from high to low,
    # checks all beers to see if it matches the level of accuracy and appends to sortedBeers
    # upgrade would be to skip over beers that are of a higher accuracy

    return insertionSort(sortedBeers)

def insertionSort(alist):
   for index in range(1,len(alist)):

     currentvalue = alist[index]
     position = index

     while position>0 and alist[position-1][1]>currentvalue[1]:
         alist[position]=alist[position-1]
         position = position-1

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
return:   top_picks: a 2d list of beers with max size 6x2.
            the beer_id then the rating
-------------------------------------------------------
"""
def top_picksFunc(beers,db):
    #The top picks are based on the highest rating from the home_rating table
    sql = """SELECT * from home_rating where beer_id = """
    i = 0
    n=len(beers)
    #assuming ratings, and ids cannot be negative
    first = [-1,-1]
    second = [-1,-1]
    third = [-1,-1]
    fourth = [-1,-1]
    fifth = [-1,-1]
    sixth =[-1,-1]
    top_picks = [first,second,third,fourth,fifth,sixth]
    while i < n:
        ratingsTable = db.engine.execute(sql + str(beers[i].id))
        ratings = []
        j=0
        for row in ratingsTable:
            ratings.append(row)
        m=len(ratings)
        total = 0
        while j<m:
            total = total + ratings[j].ratingValue
            j=j+1
        if m > 0:
            total = total/m
        if total > top_picks[0][1]:
            top_picks[0][0] = beers[i].id
            top_picks[0][1] = total
        elif total > top_picks[1][1]:
            top_picks[1][0] = beers[i].id
            top_picks[1][1] = total
        elif total > top_picks[2][1]:
            top_picks[2][0] = beers[i].id
            top_picks[2][1] = total
        elif total > top_picks[3][1]:
            top_picks[3][0] = beers[i].id
            top_picks[3][1] = total
        elif total > top_picks[4][1]:
            top_picks[4][0] = beers[i].id
            top_picks[4][1] = total
        elif total > top_picks[5][1]:
            top_picks[5][0] = beers[i].id
            top_picks[5][1] = total
        i=i+1
    return top_picks
