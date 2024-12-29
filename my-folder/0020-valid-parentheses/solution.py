class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        dictSet = {"(" : 1,"{" : 2,"[" : 3 , ")": -1, "}": -2, "]": -3}
        listSet = []
        for i in s:
            if dictSet[i] > 0:
                listSet.append(i)
            else:
                if (len(listSet) == 0):
                    return False
                if (abs(dictSet[i]) == dictSet[listSet[-1]]):
                    listSet.pop()
                else:
                    return False    

        return (len(listSet) == 0)
