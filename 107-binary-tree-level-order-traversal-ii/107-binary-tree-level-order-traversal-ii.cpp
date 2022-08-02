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
        if(level == ans.size()) {ans.push_back(vector<int>());}
        ans[level].push_back(node -> val);
        f(node -> left, ans, level + 1);
        f(node -> right, ans, level + 1);
    }
    
    
    vector<vector<int>> levelOrderBottom(TreeNode* root) {
        vector<vector<int>> ans;
        if(!root) return ans;
        f(root, ans, 0);
        reverse(ans.begin(), ans.end());
        return ans;
    }
};