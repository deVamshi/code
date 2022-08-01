class Solution {
public:
    
    void f(int n, int open, int close,string curr ,vector<string> &ans){
         if(open == n && close == n) {
             ans.push_back(curr);
             return;
         }
          
         if(open < n){
             f(n, open + 1, close, curr + "(", ans);
         } 
        
         if(close < open){
             f(n, open, close + 1, curr + ")", ans);
         }
        
    }
    
    vector<string> generateParenthesis(int n) {
        vector<string> ans;
        f(n, 0, 0, "", ans);
        return ans;
    }
};