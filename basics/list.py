people = ["Hanna", "Louisa", "Claudia", "Angela", "Geoffrey", "aparna"]

people[-1] = people[-1][0].upper() + people[-1][1::]

# print(people)

numbers = [1, 2, 3, 4]

# for of in JS
# for num in numbers:
#     print(num)
# # end of loop

for idx in range(len(numbers)):
    print(idx)
# end of loop


# List comprehension []

odd = [val for val in numbers if val % 2 != 0]
print(odd)
