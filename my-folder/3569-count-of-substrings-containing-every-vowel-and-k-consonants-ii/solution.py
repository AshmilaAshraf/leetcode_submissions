class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        if(len(word)< 5+k):
            return 0
        vowels = {'a','e','i','o','u'}
        # if(not vowels.issubset(set(word))):
        #     return 0
        
        n = len(word)
        con_pre = [0] * (n + 1)
        for i in range(n):
            con_pre[i + 1] = con_pre[i] + (1 if word[i] not in vowels else 0)

        # Precompute the next consonant index for each position
        next_consonant = [0] * n
        next_consonant_index = n
        for i in range(n - 1, -1, -1):
            next_consonant[i] = next_consonant_index
            if word[i] not in vowels:
                next_consonant_index = i

        # Sliding window approach
        vowel_count = {}  # Frequency map of vowels
        consonants = 0  # Current consonant count
        left = 0  # Left pointer for the window
        count = 0  # Count of valid substrings

        for right in range(n):
            # Expand window: process the new character
            if word[right] in vowels:
                vowel_count[word[right]] = vowel_count.get(word[right], 0) + 1
            else:
                consonants += 1
            
            # Shrink window if consonants exceed k
            while consonants > k:
                if word[left] in vowels:
                    vowel_count[word[left]] -= 1
                    if vowel_count[word[left]] == 0:
                        del vowel_count[word[left]]
                else:
                    consonants -= 1
                left += 1
            
            # Count valid substrings when conditions are met
            while left < n and len(vowel_count) == 5 and consonants == k:
                count += next_consonant[right] - right
                if word[left] in vowels:
                    vowel_count[word[left]] -= 1
                    if vowel_count[word[left]] == 0:
                        del vowel_count[word[left]]
                else:
                    consonants -= 1
                left += 1

        return(count)






        # v=0
        # con=0
        # setV = {}
        # for i in range(w):
        #     if(word[i] in vowels):
        #         v+=1
        #     else:
        #         con+=1

        # if(v==5 and con == k):
        #     count+=1
        # if(len(word) == w):
        #     return(count)
        # right = w
        # vow = v
        # conson = con
        # while(right<len(word)):
        #     # for i in range(right+1):
        #     if(word[right] in vowels):
        #         vow+=1
        #     else:
        #         conson+=1
        #     if(vow>=5 and conson == k):
        #         count+=1
        #     if(conson >k):
        #         break
        #     right+=1
            

        # for i in range(w,len(word)):
        #     # subWord = word[i:w]
        #     if(word[i-w] in vowels):
        #         v-=1
        #     else:
        #         con-=1
        #     # if(i+k <len(word)):
        #     if(word[i] in vowels):
        #         v+=1
        #     else:
        #         con+=1
        #     if(v>=5 and con == k):
        #         count+=1
        #     right = i+1
        #     vow = v
        #     conson = con
        #     while(right<len(word)):
        #         # for i in range(right+1):
        #         if(word[right] in vowels):
        #             vow+=1
        #         else:
        #             conson+=1
        #         if(vow>=5 and conson == k):
        #             count+=1
        #         if(conson >k):
        #             break
        #         right+=1
        # return(count)
        # left = 0
        # right = len(word)-1
        # mid = (left+right)//2
        # subWord1 = word[left:mid+1]
        # subWord2 =word[mid+1:right+1]
        # for i in range(w):
        # if(vowels.issubset(word[:5])):
        #     track = 5


        # v=0
        # con=0
        # for i in range(w):
        #     if(word[i] in vowels):
        #         v+=1
        #     else:
        #         con+=1
        
        # if(v>=5 and con == k):
        #     count+=1
        # if(len(word) == w):
        #     return count
        # while(w<len(word)):
        #     for i in range(w,len(word)):
        #         # subWord = word[i:w]
        #         if(word[i-w] in vowels):
        #             v-=1
        #         else:
        #             con-=1
        #         # if(i+k <len(word)):
        #         if(word[i] in vowels):
        #             v+=1
        #         else:
        #             con+=1
        #         if(v>=5 and con == k):
        #             count+=1
        #     w+=1
        # # if()
        # return count



        # for i in range(w):
        #     if(word[i] in vowels):
        #         v+=1
        #     else:
        #         con+=1
        
        # if(v==5 and con == k):
        #     count+=1
        # if(len(word) == w):
        #     return count
        # for i in range(w,len(word)):
        #     # subWord = word[i:w]
        #     if(word[i-w] in vowels):
        #         v-=1
        #     else:
        #         con-=1
        #     # if(i+k <len(word)):
        #     if(word[i] in vowels):
        #         v+=1
        #     else:
        #         con+=1
        #     if(v==5 and con == k):
        #         count+=1
        # if()
        # return count
            


