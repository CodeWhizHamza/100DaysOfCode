line = "| "
for i in range(1, 864):
    line += f"[{i}](.) | "

    if i % 22 == 0:
        line += "\n| "

with open("dummy.txt", "w") as f:
    f.write(line[:-2] + "|")
