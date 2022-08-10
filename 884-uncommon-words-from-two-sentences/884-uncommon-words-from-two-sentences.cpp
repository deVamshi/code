class Solution {
public:
    vector<string> uncommonFromSentences(string s1, string s2) {
        unordered_map<string, int> freq;
        stringstream ss(s1);
        string temp;
        
        while(getline(ss, temp, ' ')) {
            if(freq.find(temp) == freq.end()) freq[temp] = 1;
            else freq[temp] = -1;
        }
        
        stringstream X(s2);
        vector<string> ans;
        
        while(getline(X, temp, ' ')) {
            if(freq.find(temp) == freq.end()) freq[temp] = 1;
            else freq[temp] = -1;
        }
        
        for(auto ele : freq){
            if(ele.second != -1) ans.push_back(ele.first);
        }
        
        return ans;
    }
};