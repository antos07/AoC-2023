import math


def main():
    time = int(input().removeprefix("Time: ").replace(" ", ""))
    distance = int(input().removeprefix("Distance: ").replace(" ", ""))

    d_sqrt = math.sqrt(time ** 2 - 4 * distance)

    print(int(d_sqrt))


if __name__ == "__main__":
    main()
