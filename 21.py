"""
def average(a=10, b=10):
    print("Average : ", (a + b) / 2)


average()
average(10)
average(b=5)   """

"""
def name(fname, mname="Kumar", lname="Yadav"):
    print("Hi", fname, mname, lname)


name("Manoj", "Prakash")  """

"""
# def name(fname, mname="Kumar", lname="Yadav"):
def name(fname, mname, lname):
    print("Hi", fname, mname, lname)


name(fname="Manoj", lname="Verma", mname="Kumar")   """

"""
def name(fname, mname, lname):
    print("Hi", fname, mname, lname)


name(fname="Manoj", mname="Kumar")   """

#
# def average(*number):
#     # print(type(number))
#     sum = 0
#     for s in number:
#         sum = sum + s
#
#     print("Average is : ", sum/len(number))
#
#
# average(1, 2, 9, 13, 90)


# def average(*number):
#     print(type(number))
#     print(number[0], number[1], number[2], number[3], number[4])
#
#
# average(1, 2, 9, 13, 90)
#
# def average(**number):
#     print(type(number))
#     print(number["a"], number["b"], number["c"], number["d"], number["e"])
#
#
# average(a=10, b=15, c=60, d=40, e=63)


def average(*number):
    # print(type(number))
    sum = 0
    for s in number:
        sum = sum + s

    return sum/len(number)
    # return 10


avg = average(1, 2, 9, 5, 8)
print(avg)
