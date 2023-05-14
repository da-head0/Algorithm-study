func minimumSum(num int) int {
    var numlist []string
    numStr := strconv.Itoa(num)
    
    for _, n := range numStr {
        numlist = append(numlist, string(n))
    }
    
    sort.Strings(numlist)
    num1, _ := strconv.Atoi(numlist[0]+numlist[2])
    num2, _ := strconv.Atoi(numlist[1]+numlist[3])
    return num1+num2
}