# students_dict = {
#     "students": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
#
# Looping through dictionaries
# for (key, value) in students_dict.items():
#     print(key)
#
# import pandas
#
# students_data_frame = pandas.DataFrame(students_dict)
# print(students_data_frame)
#
# When looping through a Dataframe as I did below, it gives me the values of each column altogether
# for (key, value) in students_data_frame.items():
#     print(value)
#
# # Looping through all the rows in a dataframe
# for (index, row) in students_data_frame.iterrows():
#     print(row)
#     print(row.students)
#     print(row.score)
