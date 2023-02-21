from collections import defaultdict

def solution(genres, plays):
    answer = []
    
    best_music = defaultdict(int)
    music_dict = defaultdict(list)
    
    for j in range(len(genres)):
        # 베스트 앨범에 들어갈 노래 장르 선별
        best_music[genres[j]] += plays[j]
        # dict로 장르, 고유 번호, 재생횟수 표현
        music_dict[genres[j]] += [(j, plays[j])]
    # 재생횟수 내림차순 정렬
    best_music = sorted(best_music.items(), key=lambda x: -x[1])
    
    # 각 장르 별로 기준에 따라 정렬
    for genre in best_music:
        play_index = sorted(music_dict[genre[0]], key=lambda x: (-x[1], x[0]))
        
        # 가장 많이 재생된 노래를 두 개씩 모아 베스트 앨범에 넣기
        for p in range(2):
            # 장르에 속한 곡이 하나일 때, 하나의 곡 선택
            if len(play_index) == 1:
                answer.append(play_index[p][0])
                break
            else:
                answer.append(play_index[p][0])
                
    return answer