class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        w=re.findall(r'\w+', paragraph.lower())
        d1=Counter(w)
        d1 = dict(sorted(d1.items(), key=lambda x: x[1], reverse=True))
        for i in d1:
            if i not in banned:
                return i