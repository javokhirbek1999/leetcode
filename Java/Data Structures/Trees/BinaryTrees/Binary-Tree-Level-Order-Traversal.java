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
    public List<List<Integer>> levelOrder(TreeNode root) {
        if(root==null){
            return new ArrayList<>(); 
        }  
        List<List<Integer>> ans = new ArrayList<>();
        List<TreeNode> queue = new ArrayList<>();
        queue.add(root);
        while(queue.size()>0){
            ArrayList<Integer>temp = new ArrayList<>();
            int count = 0;
            int max_size = queue.size();
            while(count<max_size){
                count += 1;
                TreeNode node =  queue.get(0);
                queue.remove(0);
                temp.add(node.val);
                
                if(node.left!=null){
                    queue.add(node.left);
                }
                if(node.right!=null){
                    queue.add(node.right);
                }
            }
            ans.add(temp);
        }
        return ans;
    }
}
