import csv

# with open("weather_data.csv") as file:
#     lst = file.readlines()
#     for row in lst[1:]:
#         data.append(row.strip())
#     print(data)


# using built in csv module
# with open("weather_data.csv") as file:
#     data = csv.reader(file)
#     temperatures = []
#     next(data)
#     for row in data:
#         print(row)
#         temperatures.append(int(row[1]))
#     print(temperatures)


# using pandas module
import pandas

data = pandas.read_csv("weather_data.csv")
data_dict = data.to_dict()
temp_list = data["temp"].to_list()
# print(f" Median {data["temp"].median()}")
# print(f" Average {data["temp"].mean()}")
# print(f" Max {data["temp"].max()}")
# print(f" Min {data["temp"].min()}")
# print(f" Min {data["temp"]()}")

# print(data[data.temp == data.temp.max()])
monday = data[data.day == "Monday"]
print(int(monday.temp[0]) * 1.8 + 32)

my_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
data = pandas.DataFrame(my_dict)
data.to_csv("new_data.csv")