class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int,int> hash;

        vector<int> result;

        for(int i = 0;i<nums.size();i++)
        {
            int find = target - nums[i];

            if(hash.count(nums[i])){
                result.push_back(hash[nums[i]]);
                result.push_back(i);
                return result;
            }

            hash[find] = i;
        }

        return {};
    }
};