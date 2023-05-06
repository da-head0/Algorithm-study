func numberOfSteps(num int) int {
   count := 0
   for num != 0 {
      if num % 2 == 1 {
      num -= 1
      count += 1
   } else if num % 2 == 0 {
      num /= 2
      count += 1
      } 
   }
   return count
}