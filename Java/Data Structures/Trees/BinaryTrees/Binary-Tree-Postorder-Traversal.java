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
    public List<Integer> postorderTraversal(TreeNode root) {
        if(root==null){
            return this.values;
        }
        this.postorderTraversal(root.left);
        this.postorderTraversal(root.right);
        if(root!=null){
            this.values.add(root.val);
        }
        return this.values;
    }
}
