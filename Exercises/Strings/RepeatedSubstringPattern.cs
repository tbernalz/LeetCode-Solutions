public class Solution
{
    public bool RepeatedSubstringPattern(string s)
    {
        int len = s.Length;

        for (int i = 1; i <= len / 2; i++)
        {
            if (len % i != 0)
                continue;

            string pattern = s[0..i];
            bool isMatch = true;
            for (int j = i; j < len; j += i)
            {
                if (s[j..(j + i)] != pattern)
                {
                    isMatch = false;
                    break;
                }
            }

            if (isMatch)
                return true;
        }

        return false;
    }
}
