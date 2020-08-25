lst = [1, 2, 3, 4]
sum = 0
var = []
for i in lst:

    sum = lst[1] + lst[3]
    var.append(sum)
    var.append(lst[1])
    var.append(lst[3])
    break

print(var)
