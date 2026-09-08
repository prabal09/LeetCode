from collections import deque, defaultdict

def canFinish(numCourses: int, prerequisites: list[list[int]]) -> bool:
    # 1. Build the adjacency list and in-degree array
    adj_list = defaultdict(list)
    in_degree = [0] * numCourses

    for course, prereq in prerequisites:
        adj_list[prereq].append(course)
        in_degree[course] += 1

    # 2. Add all courses with 0 prerequisites to the queue
    queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
    processed_courses = 0

    # 3. Process the queue
    while queue:
        current = queue.popleft()
        processed_courses += 1

        for neighbor in adj_list[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # 4. If we processed all courses, no cycle exists
    return processed_courses == numCourses
