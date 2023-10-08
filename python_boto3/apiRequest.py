import requests
import json
import pandas

response = requests.get("https://fakestoreapi.com/products")
# print(type(response.json())) #type is list

data_list = response.json()
# print(len(data_list))

jewels_list = []
for data in data_list:
    if data["category"] == "jewelery":
        jewels_list.append(data)

# print(len(jewels_list))

jewels_title_list = []
for each_data in jewels_list:
    jewels_title_list.append(each_data["title"])

# print(jewels_title_list)

table_data = pandas.DataFrame(jewels_list)
# print(table_data)

# nowe to convert it into excel file in local
file = table_data.to_excel('new_file.xlsx')

#now creating file with api data 
with open('api_result.txt', 'w', encoding='utf8') as f1:
    f1.write(str(jewels_list)) # it create a file api_result.txt in local with stringed content in it

# now to read content of a file 
read_content = ''
with open('api_result.txt', 'r', encoding='utf8') as f2:
    read_content = f2.read()

print(read_content)