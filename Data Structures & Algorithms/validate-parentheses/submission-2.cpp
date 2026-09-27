class Solution {
public:
    bool isValid(string s) {
        unordered_map<char,char> check = {{'}','{'},{']','['},{')','('}};
        stack<char> brackets;
        for(char i: s){
            if(check.count(i)){
                if(!brackets.empty() && brackets.top() == check[i])
                    brackets.pop();
                else
                    return false;
            }
            else
                brackets.push(i);
        }
        if(!brackets.empty()){
            return false;
        } 
        else 
            return true;

    }
};
