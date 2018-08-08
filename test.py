from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from models includes db
from models import *
from functions import searchFunc
testFilter = {
    "alcoholVolume": 4.7,
    "brandName": "Scottish & Newcastle Breweries Ltd",
    "bodyTypeName": "Medium",
    "containerType": ["Can"],
    "taste": ["Malty"]
}
class Beer(object):
    alcoholVolume =0.0
    brandName = ""
    bodyTypeName = ""
    containerType = []
    taste = []
    def __init__(self, alcoholVolume, brandName, bodyTypeName, containerType, taste):
        self.alcoholVolume = alcoholVolume
        self.brandName = brandName
        self.bodyTypeName = bodyTypeName
        self.containerType = containerType
        self.taste = taste
beers = []
beer1 = Beer(4.7, "Scottish & Newcastle Breweries Ltd", "Medium", ["Can"], ["Malty"])
beer2 = Beer(4.8, "Scottish & Newcastle Breweries Ltd", "Medium", ["Can"], ["Not Malty"])
beers.append(beer1)
beers.append(beer2)
print(searchFunc(beers, testFilter))
