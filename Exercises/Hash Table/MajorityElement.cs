public class Solution
{
    public int MajorityElement(int[] nums)
    {
        int mostRepeatedNum = 0;
        int mostRepeatedNumCount = 0;

        Dictionary<int, int> countsDictionary = nums.Distinct()
            .ToDictionary(key => key, value => 0);

        foreach (int num in nums)
        {
            countsDictionary[num]++;
        }

        foreach (var (num, count) in countsDictionary)
        {
            if (countsDictionary[num] > mostRepeatedNumCount)
            {
                mostRepeatedNum = num;
                mostRepeatedNumCount = countsDictionary[num];
            }
        }

        return mostRepeatedNum;
    }
}
