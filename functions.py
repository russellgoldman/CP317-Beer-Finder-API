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
            j+=1
    return sortedBeers, accuracies