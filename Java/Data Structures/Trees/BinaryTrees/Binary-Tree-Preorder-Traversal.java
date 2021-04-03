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
    List<Integer>values;
    
    public Solution(){
        this.values = new ArrayList<>();
    }
    public List<Integer> preorderTraversal(TreeNode root) {
        if(root==null){
            return this.values; 
        }
        if(root!=null){
            this.values.add(root.val);
        } 
        this.preorderTraversal(root.left);
        this.preorderTraversal(root.right);
        return this.values;
    }
}
