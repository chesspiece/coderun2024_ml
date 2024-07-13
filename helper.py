if __name__ == "__main__":
    res = []
    with open("need_help.txt", "r") as f:
        for line in f:
            res.append([int(x) for x in line.strip().split()])
    with open("help_output.txt", "w") as f:
        f.write("np.array([")
        for line in res:
            f.write("".join(str(line)) + ",")
        f.write("])")
