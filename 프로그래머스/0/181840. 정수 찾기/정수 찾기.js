function solution(num_list, n) {
    var answer = 0
    num_list.map((val) => {
        if (val === n) {
            answer = 1
        }
            
    })
    return answer
}