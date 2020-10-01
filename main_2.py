start = int(input())
end = int(input())

first_even = start + start%2
last_even = end - end%2

first_odd = start + (1-start%2)
last_odd = end - (1-end%2)

sum_even = ((first_even - last_even) // 2 + 1) * (first_even + last_even) // 2
sum_odd = ((first_odd - last_odd) // 2 + 1) * (first_odd + last_odd) // 2

print(sum_even - sum_odd)