class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(" ", "")
        st = []
        j = 0
        for i in range(len(s) + 1):
            if i == len(s):
                if st and st[-1] == "*":
                    st.pop(-1)
                    st.append(str(int(st.pop(-1)) * int(s[j:])))
                elif st and st[-1] == "/":
                    st.pop(-1)
                    st.append(str(int(int(st.pop(-1)) / int(s[j:]))))
                else:
                    st.append(s[j:])
                break

            if s[i] == "*" or s[i] == "/" or s[i] == "+" or s[i] == "-":
                if st and st[-1] == "*":
                    st.pop(-1)
                    st.append(str(int(st.pop(-1)) * int(s[j:i])))
                elif st and st[-1] == "/":
                    st.pop(-1)
                    st.append(str(int(int(st.pop(-1)) / int(s[j:i]))))
                else:
                    st.append(s[j:i])
                st.append(s[i])
                j = i + 1

        res = int(st[0])
        i = 1
        while i < len(st):
            if st[i] == '+':
                res += int(st[i + 1])
                i += 2
            elif st[i] == '-':
                res -= int(st[i + 1])
                i += 2

        return res


sol = Solution()
print(sol.calculate("3+2*2"))
print(sol.calculate("3/2 "))
print(sol.calculate("3+5 / 2"))
