#include <iostream>
#include <vector>
using namespace std;
class Solution {
public:
    vector<vector<int> > greaterElement(vector<int>& nums, const vector<vector<int> > &prev) {
    vector<int> ms;
    vector<vector<int> > pprev(nums.size());
    for (int i = nums.size() - 1; i >= 0; --i) {
        for (int j : prev.empty() ? vector<int>{i} : prev[i]) {
            auto it = upper_bound(rbegin(ms), rend(ms), j, [&](int i, int j){ return nums[i] < nums[j]; });
            if (it != rend(ms))
                pprev[*it].push_back(j);
        }
        while(!ms.empty() && nums[ms.back()] < nums[i])
            ms.pop_back();
        ms.push_back(i);
    }
        return pprev;
    }
    vector<int> secondGreaterElement(vector<int>& nums, int k = 2) {
        vector<int> res(nums.size(), -1);
        vector<vector<int>> prev;
        while (--k >= 0)
            prev = greaterElement(nums, prev);
        for (int i = nums.size() - 1; i >= 0; --i)
            for (int j : prev[i])
                res[j] = nums[i];
        return res;
    }
};
int main() {
    Solution a;
    vector<int> nums = {2,4,0,9,6};
    vector<vector<int>> a1 = a.secondGreaterElement(&nums);
}
