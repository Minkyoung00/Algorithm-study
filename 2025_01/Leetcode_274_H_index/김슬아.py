# 답보고 이해했습니당..ㅠㅠ
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        h = 0
        for i, citation in enumerate(citations):
            if citation >= i + 1:  # 인용 횟수가 인덱스+1 이상이면
                h = i + 1         # h를 갱신
            else:
                break 
        return h            # 조건을 만족하지 않으면 종료
