# http://adriann.github.io/programming_problems.html
# Write a program that prints a multiplication table for numbers up to 12.

multi_table_12 = []
for x in range(1, 13):
    multi_table_row = []
    for y in range(1, 13):
        multi_table_row.append(x * y)
    multi_table_12.append(multi_table_row)

for i in range(len(multi_table_12)):
    print(multi_table_12[i])
