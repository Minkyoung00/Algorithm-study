hists = []

while True:
    test = input()
    if test == '0': break
    hists.append(list(map(int, test.split())))

for hist in hists:
    n = hist.pop(0)  
    heights = hist + [0]  
    stack = []
    max_area = 0

    for i in range(len(heights)):
        h = heights[i]
        while stack and heights[stack[-1]] > h:
            height = heights[stack.pop()]
            if stack:
                width = i - stack[-1] - 1
            else:
                width = i
            max_area = max(max_area, height * width)
        stack.append(i)

    print(max_area)

# for hist in hists:
#     n = hist.pop(0)
#     rectangles = [max(hist), n * min(hist)]

#     for i in range(2,n):  # 폭 
#         max_ = 0
#         for j in range(n-i+1):
#             max_ = max(max_, i * min(hist[j:j+i]))
        
#         if max_ == i: break
#         rectangles.append(max_)

#     print(max(rectangles))