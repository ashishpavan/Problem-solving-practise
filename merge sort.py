arr=[int(x)for x in input().split()]
def merge_sort(start,end):
    if start==end or start<0 or end<0:
        return
    elif end-start+1==2:
        if arr[start]>arr[end]:
            arr[start],arr[end]=arr[end],arr[start]
    elif start<end:
        mid=(start+end)//2
        merge_sort(start,mid)
        merge_sort(mid+1,end)
        merge(start,end)
def merge(start,end):
    s1=start
    md=(start+end)//2
    s2=md+1
    ans=[]
    while s1<=md and s2<=end:
        if arr[s1]<arr[s2]:
            ans.append(arr[s1])
            s1+=1
        else:
            ans.append(arr[s2])
            s2+=1
    if s1==md+1:
        ans.extend(arr[s2:end+1])
    elif s2==end+1:
        ans.extend(arr[s1:md+1])
    arr[start:end+1]=ans
merge_sort(0,len(arr)-1)
print(' '.join([str(i) for i in arr]))
        
    
    
