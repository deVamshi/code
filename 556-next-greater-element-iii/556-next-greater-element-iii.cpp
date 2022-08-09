class Solution {
public:
    int nextGreaterElement(int n) {
        
        // Algorithm that can be use to solve this problem
        // This question is most similar to the next  permutation of the given digits
        // find the break point
        // find the number that is greater than the number at break point
        // swap it with the number that is at the break point
        // reverse the entire number that starts from the break point
        
        string s = to_string(n);
        
        int i;
        
        for(i = s.size() - 2; i >= 0; i--){
            if(s[i] - '0' < s[i + 1] - '0') break;
        }
        
        if(i == -1) return i;
        
        cout << i << endl;
        
        for(int j = s.size() - 1; j > i; j--){
            if(s[j] - '0' > s[i] - '0') {
                swap(s[j], s[i]);
                break;
            }
        }
        
        sort(s.begin() + i + 1, s.end());
        
        cout << s << endl;
        
        if(stol(s) < INT_MIN || stol(s) > INT_MAX) return -1;
        return stoi(s);
    }
};