def smartcitytemp():
    K=3
    list_=[73, 74, 75, 71, 69, 72, 76, 73]
    result=[0]*len(list_)
    for i in range(len(list_)):
        count=0
        for j in range(i+1, len(list_)):
            if list_[j]>= list_[i]+K:
                result[i]=j
                break
            elif list_[j]<=list_[i]-K:
                result[i]=j
                break
        
    print(result)

smartcitytemp()

