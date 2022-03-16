/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

var Vals []int = []int{}

func preorderTraversal(root *TreeNode) []int {
    temp := preorder(root)
    Vals = []int{}

    return temp
}

func preorder(root *TreeNode) []int{
    if root == nil {
        return Vals
    }
    Vals = append(Vals, root.Val)
    preorder(root.Left)
    preorder(root.Right)
    return Vals
}
