def sum(a, b):  # func defination with func_name and parameters
    s = a + b
    return s  # return statement


print(sum(2, 3))  # function call

# print(sum(4,5))
# print(sum(9,6))
# func are used to do specific task of work and avoid code reduntancy


# def mul(a,b):
#     return (a * b)
# print(mul(2,5))


# def calc_avg(a,b,c):
#     sum = a+b+c
#     avg = sum/3
#     return avg
# print(calc_avg(95,97,95))

# Practice questions
# Write a function to print the length of the list (list is the parameter)
cities = ["Nodia", "pune", "gurgaon", "mumbai", "london"]
heroes = ["captain marvel", "captain ameriaca", "ironman", "krish"]


def print_len(list):
    print(len(list))

# print(len(cities))
# print(len(heroes))


# write a function to print elements of list to print in single line(use the same list as the parameter)
def print_el(list):
    for el in list:
        print(el, end=" ")

print_el(cities)
