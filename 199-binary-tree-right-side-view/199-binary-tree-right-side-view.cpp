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
    void traverse(TreeNode *node, int level, vector<int> &ds){
        if(!node) return;
        if(level == ds.size()){
            ds.push_back(node -> val);
        }
        traverse(node -> right, level + 1, ds);
        traverse(node -> left, level + 1, ds);
    }
    
    vector<int> rightSideView(TreeNode* root) {
        vector<int> ds;
        if(!root) return ds;
        traverse(root, 0, ds);
        
        return ds;
    }
};