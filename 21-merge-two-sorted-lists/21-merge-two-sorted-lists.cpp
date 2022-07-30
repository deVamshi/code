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
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        
        ListNode *newHead = new ListNode(2);
        
        ListNode *itr = newHead;
        
        while(list1 && list2){
            if(list1 -> val < list2 -> val){
                ListNode *newNode = new ListNode(list1 -> val);
                itr -> next = newNode;
                list1 = list1 -> next;

            } else {
                ListNode *newNode =  new ListNode(list2 -> val);
                itr -> next = newNode;
                list2 = list2 -> next;
            }
            itr = itr -> next;
        }
        
        if(list1){
            itr -> next = list1;
        } else {
            itr -> next = list2;
        }
     
        return newHead -> next;
        
    }
};