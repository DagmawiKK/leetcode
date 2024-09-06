class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        m_dict = {}
        m_nums = sorted(nums)
        for i in range(len(m_nums)):
            if m_nums[i] not in m_dict:
                m_dict[m_nums[i]] = i

        return [m_dict[num] for num in nums]