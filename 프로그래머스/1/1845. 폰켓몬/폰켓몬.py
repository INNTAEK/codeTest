def solution(nums):
    pickNum = int(len(nums)/2)
    tem = len(set(nums))
    if pickNum > tem:
        return tem
    return pickNum