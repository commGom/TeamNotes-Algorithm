def solution(clothes):
    answer = 1
    clothes_dict = {}
    for cloth in clothes:
        if clothes_dict.get(cloth[1]):
            clothes_dict[cloth[1]] += 1
        else:
            clothes_dict[cloth[1]] = 1
    for val in clothes_dict.values():
        answer *= (val+1)
    answer -= 1
    return answer


print(solution([["yellowhat", "headgear"], [
      "bluesunglasses", "eyewear"], ["green_turban", "headgear"]]))
print(solution([["crowmask", "face"], [
      "bluesunglasses", "face"], ["smoky_makeup", "face"]]))
