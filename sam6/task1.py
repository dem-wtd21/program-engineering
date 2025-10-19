user_input = input()
data_list_str = user_input.split()
data_list = [int(item) for item in data_list_str]
data_tuple = tuple(data_list)
print(data_list)
print(data_tuple)