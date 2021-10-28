from bisect import insort


# Find max and min value for each user id
class Solution1:
    def solve(self, logs):
        mp = dict()
        for log in logs:
            user = log[1]
            val = log[0]
            if user not in mp:
                mp[user] = [int(val), int(val)]
            else:
                mp[user][0] = max(mp[user][0], int(val))
                mp[user][1] = min(mp[user][1], int(val))
        return list(mp.items())


# Find which resource was called maximum times in 5 min interval
class Solution2:
    def solve(self, logs):
        mp = dict()
        for log in logs:
            resource = log[2]
            val = log[0]
            if resource not in mp:
                mp[resource] = list()
            insort(mp[resource], int(val))

        res = []
        for k, v in mp.items():
            idx = 0
            cnt = 1
            ret = 1
            for i in range(1, len(v)):
                if v[idx] <= v[i] <= v[idx] + 5:
                    cnt += 1
                else:
                    ret = max(cnt, ret)
                    for j in range(idx, i + 1):
                        if v[j] <= v[i] <= v[j] + 5:
                            idx = j
                            cnt += 1
                            break
                        else:
                            cnt -= 1
            ret = max(cnt, ret)
            res.append([k, ret])

        return res


logs1 = [
    ["58523", "user_1", "resource_1"],
    ["62314", "user_2", "resource_2"],
    ["54001", "user_1", "resource_3"],
    ["200", "user_6", "resource_5"],
    ["215", "user_6", "resource_4"],
    ["54060", "user_2", "resource_3"],
    ["53760", "user_3", "resource_3"],
    ["58522", "user_22", "resource_1"],
    ["53651", "user_5", "resource_3"],
    ["2", "user_6", "resource_1"],
    ["100", "user_6", "resource_6"],
    ["400", "user_7", "resource_2"],
    ["100", "user_8", "resource_6"],
    ["54359", "user_1", "resource_3"],
]
logs2 = [
    ["300", "user_1", "resource_3"],
    ["599", "user_1", "resource_3"],
    ["900", "user_1", "resource_3"],
    ["1199", "user_1", "resource_3"],
    ["1200", "user_1", "resource_3"],
    ["1201", "user_1", "resource_3"],
    ["1202", "user_1", "resource_3"]
]
sol1 = Solution1()
print(sol1.solve(logs1))
print(sol1.solve(logs2))
sol2 = Solution2()
print(sol2.solve(logs1))
print(sol2.solve(logs2))

import re


class StringMatch:
    def match(self, st):
        regex = re.compile('^[+]?[1-9][0-9]{1,14}$')
        mo = regex.search(st)
        print(mo)


sm = StringMatch()
print(sm.match("+919f2342f341"))
