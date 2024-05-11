func search(nums []int, target int) int {
    for i, e := range nums {
        if target == e {
            return i
        }
    }
    return -1
}