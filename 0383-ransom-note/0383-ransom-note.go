func check_and_remove(s []string, str string) ([]string, bool) {
    for idx, v := range s {
        if v == str {
            s = append(s[:idx], s[idx+1:]...)
            return s, true
        }
    }
    return s, false
}

func canConstruct(ransomNote string, magazine string) bool {
    ransomNote_splited_strings := strings.Split(ransomNote, "")
    magazine_splited_strings := strings.Split(magazine, "")
    
    for i := 0; i < len(ransomNote_splited_strings); i++ {
        var answer bool
        magazine_splited_strings, answer = check_and_remove(magazine_splited_strings, ransomNote_splited_strings[i])
        if answer == false {
            return false
        }
    }
    return true
}