import csv
import datetime
import random


counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
            {"county":"Denver", "registered_voters": 463353},
            {"county":"Jefferson", "registered_voters": 432438}]

# # if "El Paso" not in counties:
# #     print("True")
# # else:
# #     print("False")

# if not("Arapahoe" in counties or "Durango" in counties):
#     print("Arapahoe and Durango are not in the list")
# else:
#     print("....yes they are")

# print("me" in "team")

# for county in range(len(counties)):
#     print(counties[county])

# for i in range(len(voting_data)):
#     print(voting_data[i])


# for i in voting_data:
#     for x in i.values():
#         print(f'{x} county has {x} registered voters')

# for i in voting_data:
#     print(i["county"] + " county has " + str(i["registered_voters"]) + " registered voters")
#     print()
#     print(f'{i["county"]} county has {i["registered_voters"]} registered voters')
#     print()

print(dir(random))