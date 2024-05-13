from collections import Counter

Target = ['yes', 'no', 'no', None, 'yes', 'yes', 'no', 'yes']
new_target = Counter(Target)

poll_1 = {'yes': 140, 'no': 120, None: 12}
poll_2 = {'yes': 113, 'no': 132, None: 9}
poll_3 = {'yes': 16, 'no': 14}

c1 = Counter(poll_1)
c2 = Counter(poll_2)
c3 = Counter(poll_3)
cnt_total =  c1 + c2 + c3

print("Yes voters are: ", cnt_total['yes'])
print(cnt_total)
print(new_target)
