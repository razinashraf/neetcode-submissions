class Solution {
public:
    bool isPalindrome(string s) {
        stack<char> a;
        string reverse;
        string cleaned;

        for(char i: s){
            if (isalnum(i)){
                i = tolower(i);
                cleaned+=i;
            }
        }

        for(char i: cleaned){
            a.push(i);
        }

        while (!a.empty()){
            reverse += a.top();
            a.pop();
        }

        if (cleaned==reverse){
            return true;
        }
        return false;
    }
};
