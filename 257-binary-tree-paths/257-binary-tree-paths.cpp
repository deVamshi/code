
class Solution {
    
public:
    void trav(TreeNode *node, vector<string> &ans, string curr){
        
        if(!node)return;
        
        curr += to_string(node -> val);
        
        if(!(node ->left) && !(node -> right))ans.push_back(curr);
        else {
            curr += "->"; 
            trav(node -> left, ans, curr);
            trav(node -> right, ans, curr);
        }
    }
    
    vector<string> binaryTreePaths(TreeNode* root) {
        vector<string> ans;
        string curr;
        trav(root, ans, curr);
        return ans;
    }
};