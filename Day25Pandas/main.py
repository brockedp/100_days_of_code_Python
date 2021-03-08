# list_of_weather = []
# with open("./weather_data.csv") as data_file:
#     names = data_file.readlines()
#     for name in names:
#         list_of_weather.append(name)
#
# print(list_of_weather)

# import csv
# with open("./weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append((row[1]))
#         print(row)
#     print(temperatures)


import pandas
import math
# data = pandas.read_csv("weather_data.csv")
# # print(type(data))
# # # print(data)
# # print(type(data["temp"]))
# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# print(temp_list)
# average = sum(temp_list)/len(temp_list)
# print(average)
# print(data["temp"].mean())
#
# print(data["temp"].max())
# print(data.temp.max())
#
# #get data in a row
# print(data[data.temp == "Monday"])
# print(data[data.temp == data.temp.max()])
#
# #Create a dataframe from scratch
# data_dict = {
#     "students": ["Amy","James","Angela"],
#     "Scores":[76,56,65]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])

# make new csv with total and colors

data_dict = {
    "Fur Colors":["Gray","Cinnamon", "Black"],
    "Count":[gray_squirrels_count,cinnamon_squirrels_count,black_squirrels_count]
}
# print(data_dict)
df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_color_totals.csv")
