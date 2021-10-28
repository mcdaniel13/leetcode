from bisect import insort
from typing import List


class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        n = len(keyName)
        mp = dict()
        for i in range(n):
            if keyName[i] not in mp:
                mp[keyName[i]] = list()
            insort(mp[keyName[i]], int(keyTime[i].replace(":", "")))

        res = []
        for k, v in mp.items():
            cnt = 1
            cur = v[0]
            for i in range(1, len(v)):
                if cnt >= 3:
                    break
                if cur <= v[i] <= cur + 100:
                    cnt += 1
                else:
                    if v[i - 1] <= v[i] <= v[i - 1] + 100:
                        cnt = 2
                        cur = v[i - 1]
                    else:
                        cnt = 1
                        cur = v[i]
            if cnt >= 3:
                insort(res, k)
        return res


sol = Solution()
keyName = ["daniel", "daniel", "daniel", "luis", "luis", "luis", "luis"]
keyTime = ["10:00", "10:40", "11:00", "09:00", "11:00", "13:00", "15:00"]
print(sol.alertNames(keyName, keyTime))
keyName = ["alice", "alice", "alice", "bob", "bob", "bob", "bob"]
keyTime = ["12:01", "12:00", "18:00", "21:00", "21:20", "21:30", "23:00"]
print(sol.alertNames(keyName, keyTime))
keyName = ["john", "john", "john"]
keyTime = ["23:58", "23:59", "00:01"]
print(sol.alertNames(keyName, keyTime))
keyName = ["leslie", "leslie", "leslie", "clare", "clare", "clare", "clare"]
keyTime = ["13:00", "13:20", "14:00", "18:00", "18:51", "19:30", "19:49"]
print(sol.alertNames(keyName, keyTime))

# Karat Version
# class Solution:
#     def alertNames(self, badges: List[str]) -> List[str]:
#         mp = dict()
#         for badge in badges:
#             name = badge[0]
#             time = int(badge[1])
#             if name not in mp:
#                 mp[name] = list()
#             insort(mp[name], time)
#         res = []
#         print(mp)
#         for k, v in mp.items():
#             cur = v[0]
#             ret = [cur]
#             flag = False
#             for i in range(1, len(v)):
#                 if cur <= v[i] <= cur + 100:
#                     ret.append(v[i])
#                 else:
#                     if len(ret) >= 3:
#                         flag = True
#                         res.append([k, ret])
#                         break
#                     else:
#                         if v[i - 1] <= v[i] <= v[i - 1] + 100:
#                             cur = v[i - 1]
#                             ret = [cur, v[i]]
#                         else:
#                             cur = v[i]
#                             ret = [cur]
#             if not flag and len(ret) >= 3:
#                 res.append([k, ret])
#
#         return res
#
#
# sol = Solution()
# badge_times = [
# ["Paul", "1355"], ["Jennifer", "1910"], ["Jose", "835"],
# ["Jose", "830"], ["Paul", "1315"], ["Chloe", "0"],
# ["Chloe", "1910"], ["Jose", "1615"], ["Jose", "1640"],
# ["Paul", "1405"], ["Jose", "855"], ["Jose", "930"],
# ["Jose", "915"], ["Jose", "730"], ["Jose", "940"],
# ["Jennifer", "1335"], ["Jennifer", "730"], ["Jose", "1630"],
# ["Jennifer", "5"], ["Chloe", "1909"], ["Zhang", "1"],
# ["Zhang", "10"], ["Zhang", "109"], ["Zhang", "110"],
# ["Amos", "1"], ["Amos", "2"], ["Amos", "400"],
# ["Amos", "500"], ["Amos", "503"], ["Amos", "504"],
# ["Amos", "601"], ["Amos", "602"],
# ]
# print(sol.alertNames(badge_times))
