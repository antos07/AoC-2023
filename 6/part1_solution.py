def main():
    times = [int(time) for time in input().removeprefix("Time: ").split()]
    distances = [
        int(distance) for distance in input().removeprefix("Distance: ").split()
    ]

    answer = 1
    for time, distance in zip(times, distances):
        answer *= sum(1 for i in range(time + 1) if i * (time - i) > distance)

    print(answer)


if __name__ == "__main__":
    main()
