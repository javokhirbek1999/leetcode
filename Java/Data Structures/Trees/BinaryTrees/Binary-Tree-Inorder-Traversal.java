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
class Solution {
    ArrayList<Integer>list;
    
    public Solution(){
        this.list = new ArrayList<>();
    }
    public List<Integer> inorderTraversal(TreeNode root) {
        if (root==null){
            return this.list;
        }
        this.inorderTraversal(root.left);
        if(root!=null){
            this.list.add(root.val);
        }
        this.inorderTraversal(root.right);
        return this.list;
    }
}
