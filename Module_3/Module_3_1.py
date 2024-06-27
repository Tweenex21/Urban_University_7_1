calls = 0
def cout_calls():
    global calls
    calls += 1
def string_info(string):
    cout_calls()
    lenght = len(string)
    upper_case = string.upper()
    lower_case = string.lower()
    return (lenght, upper_case, lower_case)
def is_contains(string, list_to_search):
    cout_calls()
    lowercase_string = string.lower()
    lowercase_list = [item.lower() for item in list_to_search]
    return lowercase_string in lowercase_list
result_info = string_info("Hello, world!")
print(result_info)
result_contains = is_contains("UrbaN", ["apple", "banana", "orange", "urban"])
result_contains1 = is_contains('cycle', ['recycling', 'cyclic'])
print(result_contains1)
print(result_contains)
print(calls)