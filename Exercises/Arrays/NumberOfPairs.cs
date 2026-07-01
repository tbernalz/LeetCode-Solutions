public class Solution
{
    public int[] NumberOfPairs(int[] nums)
    {
        if (nums.Length == 1)
        {
            return [0, 1];
        }

        int[] result = [0, 0];
        Array.Sort(nums);

        for (int i = 0; i + 1 < nums.Length; i++)
        {
            if (nums[i] == nums[i + 1])
            {
                result[0]++;
                i++;
            }
            else
            {
                result[1]++;
            }

            if (i + 2 == nums.Length)
            {
                result[1]++;
            }
        }

        return result;
    }
}
