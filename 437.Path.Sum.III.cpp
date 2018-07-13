/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    int go(TreeNode* root, int target)
    {
        if (root == NULL) return 0;
        else
        {
            return go(root->left, target - root->val) + go(root->right, target - root->val) + (root->val == target);
        }
    }
    int pathSum(TreeNode* root, int sum) 
    {
        if(root == NULL) return 0;
        else return go(root, sum) + pathSum(root->left, sum) + pathSum(root->right, sum);
    }
};