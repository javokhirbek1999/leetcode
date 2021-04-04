/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class CBTInserter {
    TreeNode root;
    TreeNode left;
    TreeNode right;
    public CBTInserter(TreeNode root) {
        this.root = root;
        this.left = null;
        this.right = null;        
    }
    
    public int insert(int v) {
        TreeNode node = new TreeNode(v);
        if(this.root==null){
            this.root = node;
        }
        Queue<TreeNode>q = new LinkedList<>();
        TreeNode t = null;
        q.add(this.root);
        while(q.size()>0){
            TreeNode temp = q.remove();
            if(temp.left!=null){
                q.add(temp.left);
            } else{
                temp.left = node;
                return temp.val;
            }
            if(temp.right!=null){
                q.add(temp.right);
            }else{
                temp.right = node;
                return temp.val;
            }            
        }
        return this.root.val; 
    }
    
    public TreeNode get_root() {
        if(root==null){
            return null;
        }
        return this.root;
    }
}

/**
 * Your CBTInserter object will be instantiated and called as such:
 * CBTInserter obj = new CBTInserter(root);
 * int param_1 = obj.insert(v);
 * TreeNode param_2 = obj.get_root();
 */
