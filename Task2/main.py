def evacuation_boats():

    N, Q, limit = map(int, input().split())
    weights = list(map(int, input().split()))
    priority = list(map(int, input().split()))

    queries = [input().split() for _ in range(Q)]

    people = list(zip(weights, priority))
    people.sort(key=lambda x: x[0])  

    left = 0
    right = N - 1
    boats = 0

    while left <= right:
        if left == right:
            boats += 1
            break

        w1, p1 = people[left]
        w2, p2 = people[right]

        if (w1 + w2 <= limit) and not (p1 == 1 and p2 == 1):
            left += 1
            right -= 1
        else:
            right -= 1

        boats += 1

    print(f"Minimum boats = {boats}")

    for q in queries:
        if q[0] == "CANPAIR":
            x = int(q[1])
            y = int(q[2])

            if weights[x] + weights[y] <= limit and not (
                priority[x] == 1 and priority[y] == 1
            ):
                print("Yes")
            else:
                print("No")

        elif q[0] == "REMAINING":
            B = int(q[1])
            
            left = 0
            right = N - 1
            boats_used = 0
            evacuated = 0

            while left <= right and boats_used < B:
                if left == right:
                    evacuated += 1
                    boats_used += 1
                    break

                w1, p1 = people[left]
                w2, p2 = people[right]

                if (w1 + w2 <= limit) and not (p1 == 1 and p2 == 1):
                    evacuated += 2
                    left += 1
                    right -= 1
                else:
                    evacuated += 1
                    right -= 1

                boats_used += 1

            print(N - evacuated)
evacuation_boats()