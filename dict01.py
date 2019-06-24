#!/usr/bin/env python3
example = {"key" : "value"}
cars = {
        "rental"  : "sentra",
        "real"    : "soul"
        }

print("keys:  ", cars.keys())
print("Rental: ", cars["rental"])

cars["dream"] = "VW Bug"
print("keys:  ", cars.keys())
print("Dream: ", cars["dream"])

cars.update({"dream2": "VW Bus", "dream3": "Volvo"})
print("keys:  ", cars.keys())
print("Dream2: ", cars["dream2"])

cars["trucks"] = ["F150","F250","F350","F450","F550"]
print("My Truck: ", cars["trucks"][3], "\n")

print(cars)


