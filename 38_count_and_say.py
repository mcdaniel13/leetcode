class Solution:
    def countAndSayInternal(self, n: int, step: int, s: str) -> str:
        if step >= n:
            return s

        ch = s[0]
        cnt = 1
        sn = ""
        for i in range(1, len(s)):
            # print("s[i]=",s[i],"ch=",ch)
            if s[i] == ch:
               cnt += 1
               # print("cnt=",str(cnt))
            else:
                sn += str(cnt)
                sn += ch
                ch = s[i]
                cnt = 1
                # print(sn)

        if cnt != 0:
            sn += str(cnt)
            sn += ch
            # print(sn)

        return self.countAndSayInternal(n, step + 1, sn)

    def countAndSay(self, n: int) -> str:
        step = 1
        s = "1"
        if step == n:
            return "1"

        return self.countAndSayInternal(n, step, s)





sol = Solution()
print(sol.countAndSay(1))
print(sol.countAndSay(6))