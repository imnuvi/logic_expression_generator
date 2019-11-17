import string


n = int(input("enter the dimension : "))
b = int(input("enter the number of data points : "))
print("enter the input and output")

data_list = []
thestr = ""

def expression_gen(thearr,n):
    expression = ""
    for i in range(n):
        if thearr[i]:
            expression += chr(65+i)
        else:
            expression += chr(65+i) + "\'"
    return str(expression)

for j in range(b):
    data = input("enter data point {} : ".format(j))
    hell = list(map(int,data.rstrip().split()))
    data_list.append(hell)


final_list = []
for x in data_list:
    if x[-1]:
        final_list.append(expression_gen(x[:-1], n))
    else:
        continue

print(" + ".join(final_list))
