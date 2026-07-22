# Divide_and_Conquer.py

def get_min_distance(points):

    def dist2(p1, p2):
        return (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2

    def dq(px, py):

        n = len(px)

        if n <= 3:
            min_dist = float("inf")

            for i in range(n):
                for j in range(i + 1, n):
                    min_dist = min(min_dist, dist2(px[i], px[j]))

            return min_dist
    
        mid = n // 2
        mid_x = px[mid][0]

        left_x = px[:mid]
        right_x = px[mid:]

        left_y = []
        right_y = []

        left_set = set(left_x)

        for p in py:
            if p in left_set:
                left_y.append(p)
            else:
                right_y.append(p)

        left_min = dq(left_x, left_y)
        right_min = dq(right_x, right_y)

        min_dist = min(left_min, right_min)

        
        if min_dist == 0:
            print(left_min, right_min)

        candidates = []
        for p in py:
            dx = p[0] - mid_x

            if dx * dx < min_dist:
                candidates.append(p)

        m = len(candidates)
        
        for i in range(m):
            for j in range(i + 1, m):
                dy = candidates[i][1] - candidates[j][1]

                if dy * dy >= min_dist:
                    break

                min_dist = min(min_dist, dist2(candidates[i], candidates[j]))

        return min_dist
    
    if len(set(points)) < len(points):
        return 0

    points_x = sorted(points)
    points_y = sorted(points, key = lambda p:p[1])

    return dq(points_x, points_y) 

points = [
    (0, 0),
    (1, 5),
    (2, 2),
    (4, 1),
    (5, 4),
    (7, 3)
]

print(get_min_distance(points))