import pathlib

current_dir = pathlib.Path(__file__).parent
suffix_dict: dict[str, int] = {}

for curr_file in current_dir.iterdir():
    if curr_file.is_dir():
        print("Directory: " + curr_file.name)
        suffix_dict["Directory"] = suffix_dict.get("Directory", 0) + 1
    elif curr_file.is_file():
        print(curr_file.suffix)
        suffix_dict[str(curr_file.suffix)] = suffix_dict.get(str(curr_file.suffix), 0) + 1
    else:
        print("Wrong Format!")

print("\n--------------------------------")
print("TOTAL")
print("--------------------------------")
for suffix, count in suffix_dict.items():
    print(suffix + " = " + str(count))
print("--------------------------------")

