from collections import defaultdict

def dfs(start, visited, graph):
    global count
    visited[start] = True
    for neighbor in graph[start]:
        if not visited[neighbor]:
            dfs(neighbor, visited, graph)
            count += 1

def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()

    # 첫 번째 줄: 공급책 수 N, 관계 수 M
    n, m = map(int, data[0].split())
    graph = defaultdict(list)
    in_degree = [0] * n  # 각 노드로 들어오는 간선 수 계산

    # 관계 정보 입력
    for i in range(1, m + 1):
        a, b = data[i].split()
        a_idx = ord(a) - ord('A')  # A~Z를 0부터 시작하는 인덱스로 변환
        b_idx = ord(b) - ord('A')
        graph[a_idx].append(b_idx)
        in_degree[b_idx] += 1

    # 마지막 줄: 경찰이 파악한 공급책 정보
    last_line = data[m + 1].split()
    tracked_count = int(last_line[0])  # 경찰이 파악한 수
    tracked = [ord(x) - ord('A') for x in last_line[1:]]  # 인덱스로 변환

    # 그래프에서 경찰이 파악한 공급책 제거
    for node in tracked:
        graph[node].clear()  # 해당 노드에서 나가는 모든 간선 제거
        for key in graph.keys():
            if node in graph[key]:
                graph[key].remove(node)

    # 방문 여부 확인
    visited = [False] * n
    global count
    count = 0

    # DFS 탐색 시작
    for i in range(n):
        if in_degree[i] == 0 and not visited[i]:  # 들어오는 간선이 없고 방문하지 않은 노드
            dfs(i, visited, graph)

    print(count)

if __name__ == "__main__":
    main()
