/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    bool isPalindrome(ListNode* head) {
        ListNode* first = head;
        ListNode* second = head;
        while(first!=nullptr&&first->next!=nullptr){
            first = first->next->next;
            second = second->next;
        }
        
        ListNode* prev = nullptr;
        while(second!=nullptr){
            ListNode* temp = second->next;
            second->next = prev;
            prev = second;
            second = temp;
        }
        
        ListNode* left = head;
        ListNode* right = prev;
        while(right!=nullptr){
            if(left->val!=right->val){
                return false;
            } 
            left = left->next;
            right = right->next;
        } 
        return true;
    }
};
