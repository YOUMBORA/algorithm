def solution(routes):
    answer = []
    
    # 진출 지점, 진입 지점 오름차순으로 정렬하기
    routes.sort(key=lambda x: (x[1], x[0]))
    
    # 카메라가 범위 안에 없으면 진출 지점에 설치해주기
    for camera in routes:
        if not answer:
            answer.append(camera[1])
        elif answer[-1] < camera[0]:
            answer.append(camera[1])

    return len(answer)