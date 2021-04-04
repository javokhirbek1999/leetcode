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
class CBTInserter {
public:  
    TreeNode* head;
    vector<TreeNode*>nodes;
    CBTInserter(TreeNode* root){
      head=root;
      nodes.push_back(NULL);
      queue<TreeNode*>q;
      q.push(head);
      while(!q.empty()){
        TreeNode* cur=q.front();
        q.pop();
        if(cur->left)q.push(cur->left);
        if(cur->right)q.push(cur->right);     
        nodes.push_back(cur);
      }      
    }    
    int insert(int v){
      TreeNode *newnode=new TreeNode(v);
      nodes.push_back(newnode);
      queue<TreeNode*>q;
      q.push(head);
      while(!q.empty()){
        TreeNode* temp=q.front();
        q.pop();
        if(!temp->left){
          temp->left=newnode;
          return temp->val;
        }
        else q.push(temp->left);
        if(!temp->right){
          temp->right=newnode;
          return temp->val;
        }
        else q.push(temp->right);
      } 
      return v;
    }    
    TreeNode* get_root() {
        return head;
    }
};

/**
 * Your CBTInserter object will be instantiated and called as such:
 * CBTInserter* obj = new CBTInserter(root);
 * int param_1 = obj->insert(v);
 * TreeNode* param_2 = obj->get_root();
 */
