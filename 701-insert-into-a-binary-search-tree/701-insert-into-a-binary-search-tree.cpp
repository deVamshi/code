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
    
    TreeNode* findNode(TreeNode* node, int val){
        
        if(val < node -> val){
            if(!(node -> left)) return node;
            else return findNode(node -> left, val);
        }
        else {
            if(!(node -> right)) return node;
            else return findNode(node -> right, val);
        }
    }
    
    TreeNode* insertIntoBST(TreeNode* root, int val) {
        if(!root) return new TreeNode(val);
        
        TreeNode* nodeToInsert = findNode(root, val);
        
        if(val < nodeToInsert -> val) nodeToInsert -> left = new TreeNode(val);
        else nodeToInsert -> right = new TreeNode(val);
        
        return root;
    }
};