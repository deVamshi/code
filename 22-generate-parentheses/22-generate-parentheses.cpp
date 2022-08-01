class Solution {
public:
    
    void f(int &n, int &open,int &close, string &curr, vector<string> &ans) {
        
         if(open == n && close == n) {
             ans.push_back(curr);
             return;
         }
          
         if(open < n) {
             curr += "(";
             open++;
             f(n, open, close, curr, ans);
             curr.pop_back();
             open--;
         } 
        
         if(close < open) {
             curr += ")";
             close++;
             f(n, open, close, curr, ans);
             close--;
             curr.pop_back();
         }
    }
    
    vector<string> generateParenthesis(int n) {
        vector<string> ans;
        string curr;
        int open = 0, close = 0;
        f(n, open, close, curr, ans);
        return ans;
    }
};