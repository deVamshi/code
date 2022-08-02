/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
    
public:
    
    void trav(TreeNode *node, vector<string> &ans, string curr){
        
        if(!node)return;
        
        if(!(node ->left) && !(node -> right)){
            ans.push_back(curr + to_string(node -> val));
            return;
        }
        
        trav(node -> left, ans, curr + to_string(node -> val) + "->");
        trav(node -> right, ans, curr + to_string(node -> val) + "->");
    }
    
    vector<string> binaryTreePaths(TreeNode* root) {
        vector<string> ans;
        string curr;
        trav(root, ans, curr);
        return ans;
    }
};