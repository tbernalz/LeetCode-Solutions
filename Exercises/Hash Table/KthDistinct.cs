public class Solution
{
    public string KthDistinct(string[] arr, int k)
    {
        int count = 0;

        Dictionary<string, int> countsDictionary = arr.Distinct()
            .ToDictionary(key => key, value => 0);

        foreach (string item in arr)
        {
            countsDictionary[item]++;
        }

        for (int i = 0; i < arr.Length; i++)
        {
            if (countsDictionary[arr[i]] == 1)
                count++;

            if (count == k)
                return arr[i];
        }

        return "";
    }
}
