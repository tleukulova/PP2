def unique_elements(given_list):
    unique_list = []
    for i in given_list:
        if i not in unique_list:
            unique_list.append(i)
    return unique_list

given_list = list(map(int, input().split()))
print(unique_elements(given_list))