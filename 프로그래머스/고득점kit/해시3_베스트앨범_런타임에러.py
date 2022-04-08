def solution(genres, plays):
    answer = []
    #  장르별로 속한 노래가 많이 재생된 장르 순서로, 장르안에서 재생된 노래 2개씩 모아 앨범 출시
    #  위치 i, 재생 수, 장르 -> 최대 장르 찾은 후,
    genre_dict = dict()
    plays_dict = dict()
    for i in range(len(plays)):
        if genre_dict.get(genres[i]):
            genre_dict[genres[i]] += plays[i]
            genre_plays = plays_dict.get(genres[i])
            genre_plays.append([i, plays[i]])
        else:
            genre_dict[genres[i]] = plays[i]
            plays_dict[genres[i]] = [[i, plays[i]]]

    # print(genre_dict)
    # print(plays_dict)
    for result in sorted(genre_dict.items(), reverse=True):
        # print(result)
        candidates = plays_dict.get(result[0])
        candidates.sort(key=lambda x: (-x[1], x[0]))
        for i in range(2):
            # print(candidates[i][0])
            answer.append(candidates[i][0])
    return answer


print(solution(["classic", "pop", "classic", "classic", "pop"],
      [500, 600, 150, 800, 2500]))  # [4, 1, 3, 0]
