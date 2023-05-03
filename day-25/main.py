# # with open("weather_data.csv") as file:
# #     data = file.readlines()
# # print(data)
#
#
# # import csv
# # with open("weather_data.csv") as file:
# #     data = csv.reader(file)
# #     temperature = []
# #     for row in data:
# #         if row[1] != 'temp':
# #             temperature.append(int(row[1]))
# #     print(temperature)
#
#
# """But this is so much tough when there are too much columns and data. So, we use pandas library!"""
# import pandas
# data = pandas.read_csv("weather_data.csv")
# # print(data["temp"])
# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# print(temp_list)
#
# average_temp = sum(temp_list)/len(temp_list)
# print(f"Average Temp: {average_temp}")
# # This average can be calculated easily using a pandas series method called mean
# print(f"Average Temp: {data['temp'].mean()}")
#
# print(f"Maximum Temp: {data['temp'].max()}")
#
# # Get Data in Column
# print(data["condition"])
# print(data.condition)
#
# # Get Data in Row
# print(data[data.day == "Monday"])
# #or
# print(data[data["day"] == "Monday"])
# print(data[data["day"] == data.day.max()])
#
# #Create dataframe from scratch
#


# data_dict = {
#     "students" : ["Amy", "James", "Angela"],
#     "scores" : [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("data.csv")
# print(data)
import pandas
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
fur_color = data["Primary Fur Color"]
print(fur_color.value_counts().to_dict())
color_dict = fur_color.value_counts().to_dict()
data_dict = {
    "Fur Color" : color_dict.keys(),
    "Count": color_dict.values()
}
data = pandas.DataFrame(data_dict)
data.to_csv("squirrel_counts.csv")