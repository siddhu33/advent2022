def main():
    message = open("day6/day6.txt", "r").read().rstrip("\n")
    print(
        next(
            idx
            for idx in range(14, len(message))
            if len(set(message[idx - 14 : idx])) == 14
        )
    )


if __name__ == "__main__":
    main()
