class Solution {
public:
    bool isPalindrome(string s) {
        
        transform(s.begin(), s.end(), s.begin(), ::tolower);
        
        int left = 0, right = s.size() - 1;
        
        while(left <= right){
            while( left <= right && !isalpha(s[left]) && !isdigit(s[left])) left++;
            while(right >= left && !isalpha(s[right]) && !isdigit(s[right])) right--;
            if(right < left) break;
            if(s[left++] != s[right--]) return false;
        }
        
        return true;
        
    }
};