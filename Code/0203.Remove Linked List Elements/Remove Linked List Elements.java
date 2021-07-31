/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode removeElements(ListNode head, int val) {
        // 当要删除的节点为第一个元素时
        while(head != null && head.val == val){
            head = head.next;
        }
        if(head == null){
            return null;
        }
        ListNode cur = head;
        ListNode pre = null;

        while(cur != null){
            if(cur.val != val){
                pre = cur;
            }else{
                pre.next = cur.next;
            }
            cur = cur.next;
        }

        return head;

    }
}