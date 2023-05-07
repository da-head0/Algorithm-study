/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func middleNode(head *ListNode) *ListNode { 
    cnt := 0
    // Count the total number of nodes in the linked-list
    for node := head; node != nil; node = node.Next {
        cnt ++
    }
    
    
    // get the middle index from the count
    middle := cnt / 2
    
    // Traverse the linked-list from the middle index
    answer := head
    for i := 0 ; i < middle ; i++ {
        answer = answer.Next
    }
    return answer
}