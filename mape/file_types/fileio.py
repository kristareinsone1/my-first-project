with open("items.txt", "w", encoding="utf-8") as fails:
    for i in range(1, 101):
        fails.write(f"item{i}\n")
