import pandas

# with open('weather_data.csv') as file:
#     data = file.readlines()
#
# print(data)

# import csv
#
# with open('weather_data.csv') as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
#         print(row)
# print(data)
# print(temperatures)

#
# data = pandas.read_csv('weather_data.csv')
#
# print(data)
# print(data['temp'])
# print(type(data))
#
# temperature_list = data['temp'].to_list()
# print(temperature_list)
#
# # print(sum(temperature_list) / len(temperature_list))
# print(data['temp'].mean())
# print(data['condition'].max())
# print(data.day)
#
# print(data[data.day == 'Monday'])
# print(data[data.temp == data.temp.max()])
#
# tuesday = data[data.day == 'Tuesday']
# print(tuesday.condition)
#
# t_temp = int(tuesday.temp)  # This way will be deprecated in the future and I'll need to access it by index
#
# print((t_temp * 1.8) + 32)


# Create a Dataframe from scratch without reading from a file
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
#
# data = pandas.DataFrame(data_dict)
# data.to_csv('new_data_file.csv')
# print(data)


# input_data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
# colors = input_data['Primary Fur Color'].value_counts()
# output_data = pandas.DataFrame(colors)
# output_data.to_csv('squirrel_count.csv')
