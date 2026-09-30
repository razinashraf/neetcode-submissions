class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int l=0,r=numbers.size() - 1;
        int sum = 0;
        vector<int> result;
        while(l<r){
            sum = numbers[l]+numbers[r];

            if(sum==target){
                result.push_back(l+1);
                result.push_back(r+1);
                return result;
            }
            if(sum<target){
                l++;
            }
            else
                r--;
        }
        return {};
    }
};
