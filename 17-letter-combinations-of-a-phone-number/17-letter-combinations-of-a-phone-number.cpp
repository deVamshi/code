class Solution {
public:
    unordered_map<char, string> mp = {
        {'2', "abc"},
        {'3', "def"},
        {'4', "ghi"},
        {'5', "jkl"},
        {'6', "mno"},
        {'7', "pqrs"},
        {'8', "tuv"},
        {'9', "wxyz"}
    };
    
    void f(int ind, string &digits, string &curr, vector<string> &ans){
        
        if(curr.size() == digits.size()) {
            ans.push_back(curr);
            return;
        } 
        
        string chars = mp[digits[ind]];
        
        for(char ch : chars) {
            curr += ch;
            f(ind + 1, digits, curr, ans);
            curr.pop_back();
        }
    }
    
    vector<string> letterCombinations(string digits) {
        vector<string> ans;
        
        if(!digits.size()) return ans;
        
        string curr = ""; 
        
        f(0, digits, curr, ans);
       
        return ans;
    }
};