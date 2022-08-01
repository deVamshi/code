class Solution {
public:
    
    void f(int n, int open,int close, string &curr, vector<string> &ans) {
        
         if(open == n && close == n) {
             ans.push_back(curr);
             return;
         }
          
         if(open < n) {
             curr += "(";
             f(n, open + 1, close, curr, ans);
             curr.pop_back();
         } 
        
         if(close < open) {
             curr += ")";
             f(n, open, close + 1, curr, ans);
             curr.pop_back();
         }
    }
    
    vector<string> generateParenthesis(int n) {
        vector<string> ans;
        string curr;
        f(n, 0, 0, curr, ans);
        return ans;
    }
};