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
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>>t;
        if(root==nullptr){
            return t; 
        }
        vector<vector<int>> ans;
        vector<TreeNode*>queue;
        queue.push_back(root);
        while(queue.size()>0){
            vector<int>temp;
            int c = 0;
            int max_len = queue.size();
            while(c<max_len){
                c+=1;
                TreeNode *node = queue.front();
                queue.erase(queue.begin());
                temp.push_back(node->val);
                
                if(node->left!=nullptr){
                    queue.push_back(node->left);
                }
                if(node->right!=nullptr){
                    queue.push_back(node->right);
                }
            }
            ans.push_back(temp);
        }
        return ans;
    }
};
