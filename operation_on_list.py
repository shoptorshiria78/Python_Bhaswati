lst = ["Apple", "Banana", "Kiwi", "Mango", "Guava"]

print("length of list", len(lst))
print("First element", lst[0])
print("last element", lst[-1])

lst.append("Papaya")

print("Append list", lst)

lst.remove("Guava")

print("Removed list", lst)

lst.sort()
print("Sorted List", lst)

lst.pop(3)
print("Poped list", lst)

lst.reverse()
print("Reversed list", lst)

print("Multiplication of list", lst * 2)

lst[:4]
print("sliced list", lst)

lst.clear()

print(lst)