# # with open("weather_data.csv") as data_file:
# #     data = data_file.readlines()
# #     print(data)
#
# # import csv
# #
# # with open("weather_data.csv") as data_file:
# #     data = csv.reader(data_file)
# #     temperatures = []
# #     for row in data:
# #         if row[1] != 'temp':
# #             temperatures.append(int(row[1]))
# #     print(temperatures)
#
# import pandas
#
# data = pandas.read_csv("weather_data.csv")
#
# # Get Data in row
# monday = data[data.day == "Monday"]
# monday_temp = monday.temp[0]
# # print(monday_temp)
#
# monday_temp_f = monday_temp * 9/5 + 32
# # print(monday_temp_f)
#
# # Create a dataframe from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")




