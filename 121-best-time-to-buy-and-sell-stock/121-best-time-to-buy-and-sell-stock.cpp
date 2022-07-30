class Solution {
public:
    int maxProfit(vector<int>& prices) {
        
        int profit = 0;
        
        int minVal = INT_MAX;
        
        for(auto price : prices){
            minVal = min(price, minVal);
            profit = max(profit, price - minVal);
        }
        
        
        return profit;
        
    }
};