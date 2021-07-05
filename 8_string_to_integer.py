class Solution:
    def myAtoi(self, s: str) -> int:
        substr = ""
        for ch in s:
            if substr == "" and ch.isdigit() is False:
                if ch == "-" or ch == "+":
                    substr += ch
                elif ch == " ":
                    continue
                else:
                    break
            else:
                if ch.isdigit():
                    substr += ch
                else:
                    break

        if substr == "" or (len(substr) == 1 and substr.isdigit() is False):
            return 0

        if substr[0] == "-":
            i = int(substr[1:]) * -1
        elif substr[0] == "+":
            i = int(substr[1:])
        else:
            i = int(substr)

        if i >= int(2 ** 31 - 1):
            i = int(2 ** 31 - 1)
        elif i <= int(-2 ** 31):
            i = int(-2 ** 31)

        return i