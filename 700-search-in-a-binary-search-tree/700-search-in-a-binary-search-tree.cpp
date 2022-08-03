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
    void search(TreeNode *node,int val,TreeNode *&ans) {
        if(!node) return;
        
        if(node -> val == val) {
            ans = node;
            return;
        };
        
        if(node -> val < val) search(node -> right, val, ans);
        else search(node -> left, val, ans);
    }
    
    
    TreeNode* searchBST(TreeNode* root, int val) {
       TreeNode* ans = NULL;
       search(root, val, ans); 
       return ans;
    }
};