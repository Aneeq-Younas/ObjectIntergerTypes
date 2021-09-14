
def nmbrs_add(num1, num2):
    if not (isinstance(num1, int) and isinstance(num2, int)):
        return "Your input is not an intergers numbers "
    else:
        return ("Total of these two numbers is ") ,  num1 + num2

print(nmbrs_add(13.2, 44))
print(nmbrs_add(545, 23))
print(nmbrs_add("654", 2))
print(nmbrs_add(152.232, 435))
print(nmbrs_add(15, 99))
print(nmbrs_add(1.5, 5))
print(nmbrs_add(54, "7"))
print(nmbrs_add(1, 4))





