string='swiss'
ans=''
for i in range(len(string)):
    count = 0
    for j in range(len(string)):
        if string[i] == string[j]:
            count = count + 1
    if count==1:
        ans = ans + string[i]
if len(ans) ==0:
    print(-1)
else:
    print(ans[0])
