def solution(video_len, pos, op_start, op_end, commands):
    op_start_time = int(op_start[:2]) * 60 + int(op_start[3:5])
    op_end_time = int(op_end[:2]) * 60 + int(op_end[3:5])
    time = int(pos[:2]) * 60 + int(pos[3:5])
    video_len_time = int(video_len[:2]) * 60 + int(video_len[3:5])
    
    if op_start_time <= time < op_end_time:
        time = op_end_time
        
    for command in commands:
        if command == 'next':
            if time >= video_len_time - 10:
                time = video_len_time
            else:
                time += 10
        else:
            if time <= 10:
                time = 0
            else:
                time -= 10
        
        # 광고 구간에 다시 진입하면 op_end_time으로 강제 이동
        if op_start_time <= time < op_end_time:
            time = op_end_time
        
    minute = time // 60
    if minute < 10:
        minute = '0' + str(minute)
    else:
        minute = str(minute)
        
    second = time % 60
    if second < 10:
        second = '0' + str(second)
    else:
        second = str(second)

    answer = f'{minute}:{second}'
    return answer
