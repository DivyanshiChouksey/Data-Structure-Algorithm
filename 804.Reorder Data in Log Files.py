# Reorder Data in Log Files


logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        return sorted(logs,key = self.sort)
    def sort(self,logs):
            a,b = logs.split(' ', 1)
            if b[0].isalpha():
                return (0,b,a)
            else:
                return (1,None,None)
