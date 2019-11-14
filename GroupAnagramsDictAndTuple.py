class solution:
    def groupAnagrams(self,strs:List[str]) -> List[List[str]]:
        mydict={}

        for word in sorted(strs):
            key=tuple(sorted(word))
            mydict[key]=mydict.get(key,[])+[word]
        return mydict.values()