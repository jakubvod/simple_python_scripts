import pathlib

current_dir = pathlib.Path(__file__).parent
suffix_dict: dict[str, int] = {}

for curr_file in current_dir.iterdir():
    if curr_file.is_dir():
        print("DIRECTORY: " + curr_file.name)
        suffix_dict["DIRECTORY"] = suffix_dict.get("DIRECTORY", 0) + 1
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

filter_suffix: str | None = None
while filter_suffix is None:
    filter_suffix = input("Would you like to filter files by certain suffix? (yes/no): ").strip().upper()
    if filter_suffix != "YES" and filter_suffix != "NO":
        filter_suffix = None

if filter_suffix == "YES":
    print("\n--------------------------------")
    print("AVAILABLE SUFFIXES")
    print("--------------------------------")
    for suffix in suffix_dict.keys():
        print(suffix)
    print("--------------------------------")
    chosen_suffix: str = input("CHOOSE ONE (with a dot): ").strip()
    if chosen_suffix not in suffix_dict:
        print("Invalid suffix!")
    else:
        print("--------------------------------")
        for curr_file in current_dir.iterdir():
            if curr_file.suffix == chosen_suffix:
                print(curr_file.name)

print("--------------------------------")
input("\nStiskni COKOLIV pro ukončení...\n")

