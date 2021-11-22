a = [14.2,16.4,11.9,15.2,18.5,22.1,19.4,25.1,23.4,18.1,22.6,17.2]
b = [215,325,185,332,406,522,412,614,544,421,445,408]
averagea,averageb = 0,0
for i in range(12):
    averagea+=i
    averageb+=i
averagea,averageb = averagea/12,averageb/12

total = 0
left,right = 0,0
for i in range(12):
    total+= (a[i]-averagea)*(b[i]-averageb)
    left+= (a[i]-averagea)**2
    right+=(b[i]-averageb)**2
left,right = left**0.5,right**0.5
ans = total/(left*right)    
print(ans)