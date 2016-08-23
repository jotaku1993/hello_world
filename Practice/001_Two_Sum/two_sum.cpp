class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        
        int iLength = nums.size();
        map<int, int> Visited;
        //Visited.clear();
        vector<int> ret;
        
        for (int i=0; i<iLength; i++){
            //std::cout << nums[i] << std::endl;
            if ( Visited.find(target-nums[i]) != Visited.end() ){
                ret.push_back( Visited[target-nums[i]] );
                ret.push_back( i );
                return ret;
            }
            Visited[ nums[i] ] = i;
        }
        return ret;
    }
};
