class Solution {
public:
    bool isValid(string s) {
        unordered_map<char, char> mp = { {')', '('}, {']', '['}, {'}', '{'} };
        stack<char> st;
        
        for(char ch : s){
            if(mp.find(ch) == mp.end()) st.push(ch);
            else {
                if(st.empty() || st.top() != mp[ch]) return false;
                st.pop();
            }
        }
        return st.empty();
    }
};