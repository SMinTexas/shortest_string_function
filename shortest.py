# Write a function that accepts a list of strings as an argument.
# It should return the shortest string in the list.

def shortest(string_list):
    shortest_string = min(string_list, key=len)
    return shortest_string

list_of_strings = ["Howdy", "Aggies", "Clemson", "Going", "Down", "Saturday"]
 
print(" ")
print(f"Original List of Words: {list_of_strings}")
print(" ")
print(f"Shortest String: {shortest(list_of_strings)}")
print(" ")