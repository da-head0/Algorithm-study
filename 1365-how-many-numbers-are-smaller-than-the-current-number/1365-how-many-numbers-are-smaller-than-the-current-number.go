func smallerNumbersThanCurrent(nums []int) []int {
    var answer []int
    for _, num := range nums {
        count := 0
        for _, n := range nums {
            if n < num {
                count++
            }
        }
        answer = append(answer, count)
    }
    return answer
}