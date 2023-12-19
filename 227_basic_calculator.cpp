#include <string>
#include <stack>

using namespace std;

class Solution
{
public:
    int calculate(string s)
    {
        stack<int> res_stack;
        int curr_num = 0;
        char curr_sign = '+';
        for (int i = 0; i < s.length(); i++)
        {
            char curr_ch = s[i];
            if (isdigit(curr_ch))
                curr_num = curr_num * 10 + (curr_ch - '0');

            // at the end, or a new operator is encountered
            if (!isdigit(curr_ch) && !iswspace(curr_ch) || i == s.length() - 1)
            {
                if (curr_sign == '+')
                {
                    res_stack.push(curr_num);
                }
                else if (curr_sign == '-')
                {
                    res_stack.push(-curr_num);
                }
                else if (curr_sign == '*')
                {
                    int last_num = res_stack.top();
                    res_stack.pop();
                    res_stack.push(last_num * curr_num);
                }
                else if (curr_sign == '/')
                {
                    int last_num = res_stack.top();
                    res_stack.pop();
                    res_stack.push(last_num / curr_num);
                }
                curr_num = 0;
                curr_sign = curr_ch;
            }
        }
        int result = 0;
        while (res_stack.size() > 0)
        {
            result += res_stack.top();
            res_stack.pop();
        }
        return result;
    }
};