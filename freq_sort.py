def frequencySort(self, s: str) -> str:
        freq=[[i,0] for i in range(62)]
        for i in range(len(s)):
            if s[i].isnumeric():
                freq[int(s[i])+52][1]+=1
            elif s[i].isupper():
                freq[ord(s[i])-65+26][1]+=1
            else :
                freq[ord(s[i])-97][1]+=1
        print(freq)
        ans=""
        freq.sort(key=lambda a:a[1],reverse=True)
        for i in range(62):
            ind=freq[i][0]
            if freq[i][1]==0:
                continue
            if ind<26:
                ans+=chr(ind+97)*freq[i][1]
            elif ind <52:
                ans+=chr(ind-26+65)*freq[i][1]
            else:
                ans+=(str(ind-52)*freq[i][1])
        return ans
