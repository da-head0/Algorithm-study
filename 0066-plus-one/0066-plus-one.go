func plusOne(digits []int) []int {
    for i, _ := range digits {
        
        // 마지막부터 시작
        idx := len(digits) - 1 - i
        if digits[idx] == 9 {
            digits[idx] = 0
        } else {
            digits[idx]++
            return digits
        }
    }
    // 모든 숫자가 9
    return append([]int{1}, digits...)
}