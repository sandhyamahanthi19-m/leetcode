class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        s={v:i for i, v in enumerate(sorted(score,reverse=True),1)}
        return [
            "Gold Medal" if s[i] == 1 else
            "Silver Medal" if s[i] == 2 else 
            "Bronze Medal" if s[i] == 3 else
            str(s[i])
            for i in score
        ]