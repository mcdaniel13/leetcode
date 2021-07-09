from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) == 0:
            return 0
        st = [(height[0], 0)]
        volume = 0
        for i in range(1, len(height)):
            if len(st) == 0 or st[len(st) - 1][0] >= height[i]:
                st.append((height[i], i))
            else:
                while len(st) != 0 and st[len(st) - 1][0] < height[i]:
                    st_top = st[len(st) - 1]
                    st = st[:-1]
                    while len(st) != 0 and st_top[0] >= st[len(st) - 1][0]:
                        st = st[:-1]
                    if len(st) != 0:
                        volume += (min(st[len(st) - 1][0], height[i]) - st_top[0])* (i - st[len(st) - 1][1] - 1)
                        # print(volume)
                st.append((height[i], i))
                # print(st)

        return volume

sol = Solution()
print(sol.trap([0,1,0,2,1,0,1,3,2,1,2,1]))
print(sol.trap([4,2,0,3,2,5]))