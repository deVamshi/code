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
    
    void f(TreeNode* node, vector<vector<int>> &ans, int level){
        if(!node) return;
        ans[level].push_back(node -> val);
        f(node -> left, ans, level - 1);
        f(node -> right, ans, level - 1);
    }
    
    int depth(TreeNode *node){
        if(!node) return 0;
        return 1 + max(depth(node -> left), depth(node -> right));
    } 
    
    vector<vector<int>> levelOrderBottom(TreeNode* root) {
        if(!root) return vector<vector<int>>();
        int d = depth(root); 
        vector<vector<int>> ans(d, vector<int> {}) ;
        f(root, ans, d - 1);
        return ans;
    }
};