class Solution {
    
public:
    
    TreeNode* findLeftMostChild(TreeNode* node){
        if(node -> right == NULL) return node;
        return findLeftMostChild(node -> right);
    }
    
    TreeNode* helper(TreeNode* node){
        
        if(node -> left == NULL) return node -> right;
        if(node -> right == NULL) return node -> left;
        
        TreeNode *rightChild = node -> right;
        TreeNode *nodeToInsert = findLeftMostChild(node -> left); 
        nodeToInsert -> right = rightChild;
        return node -> left;
    }
    
    TreeNode* deleteNode(TreeNode* root, int key) {
        
        if(!root) return root;
        
        if(root -> val == key) return helper(root);
        
        TreeNode* dummy = root;
        
        while(dummy){
            if(dummy -> val > key){
               if(dummy -> left && dummy -> left -> val == key){
                   dummy -> left = helper(dummy -> left);
                   break; 
               }
               dummy = dummy -> left;
            } else {
                if(dummy -> right && dummy -> right -> val == key){
                    dummy -> right = helper(dummy -> right);
                    break;
                }
                dummy = dummy -> right;
            }
        }
        
        return root;
    }
    
};
















