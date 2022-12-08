class puzzle():
    def __init__(self, day):
        with open(f"day{day}.txt") as input:
            self.lines = input.readlines()

    def part1():
        pass

    def part2():
        pass

    def solution(self):
        part1_solution = self.part1()
        print(part1_solution)
        print("\n")
        part2_solution = self.part2()
        print(part2_solution)


class day1(puzzle):
    def __init__(self):
        super().__init__(1)

    def part1(self):
        self.max_calories = [0]
        elf_total_calories = 0
        for cal in self.lines:
            if cal != '\n':
                elf_total_calories += int(cal)
            else:
                self.max_calories.append(elf_total_calories)
                elf_total_calories = 0
        self.max_calories.sort(reverse=True)
        return self.max_calories[0]

    def part2(self):
        return self.max_calories[0] + self.max_calories[1] + self.max_calories[2]


class day2(puzzle):
    def __init__(self):
        super().__init__(2)

    move_map = { "X": "A", "Y": "B", "Z": "C" }
    score_map = { "A": 1, "B": 2, "C": 3 }
    win_map = { "A": "C", "B": "A", "C": "B"}

    def part1(self):
        total_score = 0
        for round in self.lines:
            their_move = round.split()[0]
            my_move = self.move_map[round.split()[1]]
            if their_move == my_move:
                total_score += 3
            if (their_move == self.win_map[my_move]):
                total_score += 6

            total_score += self.score_map[my_move]

        return total_score

    def part2(self):
        # "Anyway, the second column says how the round needs to end: X means you need to lose, 
        # Y means you need to end the round in a draw, and Z means you need to win. Good luck!"
        total_score = 0

        def get_my_move(their_move: str, needed_result: str) -> str:
            if needed_result == "X":
                return self.win_map[their_move]
            if needed_result == "Y":
                return their_move
            if needed_result == "Z":
                return list(self.win_map.keys())[list(self.win_map.values()).index(their_move)]

        for round in self.lines:
            their_move = round.split()[0]
            my_move = get_my_move(their_move, round.split()[1])
            if their_move == my_move:
                total_score += 3
            if (their_move == self.win_map[my_move]):
                total_score += 6

            total_score += self.score_map[my_move]

        return total_score

class day3(puzzle):
    def __init__(self):
        super().__init__(3)

    def item_priority(self, item: chr):
        return ord(item) - 96 if ord(item) >= 97 else ord(item) - 64 + 26

    def part1(self):
        total_pri = 0
        for rucksack in self.lines:
            compartment_size = int(len(rucksack) / 2)
            compartment1 = rucksack[0:compartment_size]
            compartment2 = rucksack[compartment_size:]
            items = dict.fromkeys(compartment1)
            for item in compartment2:
                if item in items:
                    total_pri += self.item_priority(item)
                    break

        return total_pri

    def part2(self):
        total_pri = 0
        sack1 = {}
        sack2 = {}
        for rucksack in self.lines:
            if not sack1:
                sack1 = dict.fromkeys(rucksack)
            elif not sack2:
                sack2 = dict.fromkeys(rucksack)
            else:
                for item in rucksack:
                    if item in sack1 and item in sack2:
                        total_pri += self.item_priority(item)
                        sack1 = {}
                        sack2 = {}
                        break
        return total_pri

class day4(puzzle):
    def __init__(self):
        super().__init__(4)
    def part1(self):
        full_overlaps = 0
        for pair in self.lines:
            first_elf = [int(x) for x in pair.split(",")[0].split("-")]
            second_elf = [int(x) for x in pair.split(",")[1].split("-")]
            if first_elf[0] >= second_elf[0] and first_elf[1] <= second_elf[1]:
                full_overlaps += 1
            elif second_elf[0] >= first_elf[0] and second_elf[1] <= first_elf[1]:
                full_overlaps += 1
        return full_overlaps

    def part2(self):
        full_overlaps = 0
        for pair in self.lines:
            first_elf = [int(x) for x in pair.split(",")[0].split("-")]
            second_elf = [int(x) for x in pair.split(",")[1].split("-")]
            if first_elf[0] >= second_elf[0] and first_elf[0] <= second_elf[1]:
                full_overlaps += 1
            elif second_elf[0] >= first_elf[0] and second_elf[0] <= first_elf[1]:
                full_overlaps += 1
        return full_overlaps

class day5(puzzle):
    def __init__(self):
        super().__init__(5)

    def part1(self):
        determine_format = True
        stacks = []
        for stackdata in self.lines:
            if "[" in stackdata:
                if determine_format:
                    determine_format = False
                    line_length = len(stackdata)
                    stack_count = int(line_length / 4)
                    stacks = [ [] for _ in range(stack_count) ]
                crates = [ stackdata[i:i+4].strip() for i in range(0, len(stackdata), 4)]
                for cratenum in range(len(crates)):
                    if crates[cratenum]:
                        stacks[cratenum].insert(0, crates[cratenum].strip("[,]"))

            if "move" in stackdata:
                moves = stackdata.split(" ")
                for i in range(int(moves[1])):
                    stacks[int(moves[5])-1].append(stacks[int(moves[3])-1].pop())

        return ''.join([stack.pop() for stack in stacks])

    def part2(self):
        determine_format = True
        stacks = []
        for stackdata in self.lines:
            if "[" in stackdata:
                if determine_format:
                    determine_format = False
                    line_length = len(stackdata)
                    stack_count = int(line_length / 4)
                    stacks = [ [] for _ in range(stack_count) ]
                crates = [ stackdata[i:i+4].strip() for i in range(0, len(stackdata), 4)]
                for cratenum in range(len(crates)):
                    if crates[cratenum]:
                        stacks[cratenum].insert(0, crates[cratenum].strip("[,]"))

            if "move" in stackdata:
                moves = stackdata.split(" ")
                source_stack = stacks[int(moves[3])-1]
                dest_stack = stacks[int(moves[5])-1]
                crate_count = int(moves[1])
                crate_start = len(source_stack)-crate_count
                for i in range(crate_count):
                    print(len(source_stack), crate_count)
                    dest_stack.append(source_stack.pop(crate_start))

        return ''.join([stack.pop() for stack in stacks])


class day6(puzzle):
    def __init__(self):
        super().__init__(6)

    def part1(self):
        marker = ["-" for i in range(4)]
        position = 0
        for letter in self.lines[0]:
            position += 1
            for i in range(4):
                if marker[i] == letter:
                    marker[i] = "-"
            marker.pop(0)
            marker.append(letter)
            if "-" not in marker:
                break

        return position

    def part2(self):
        marker = ["-" for i in range(14)]
        position = 0
        for letter in self.lines[0]:
            position += 1
            for i in range(14):
                if marker[i] == letter:
                    marker[i] = "-"
            marker.pop(0)
            marker.append(letter)
            if "-" not in marker:
                break

        return position

class day7(puzzle):
    def __init__(self):
        super().__init__(7)

    class folder():
        def __init__(self, name, size_limit, parent={}):
            self.name = name
            self.files = {}
            self.sub_folders = {}
            self.parent = parent
            self.size_limit = size_limit

        def add_file(self, filename, filesize):
            self.files[filename] = filesize

        def add_sub_folder(self, folder_name):
            if folder_name not in self.sub_folders:
                self.sub_folders[folder_name] = day7.folder(folder_name, self.size_limit, self)

        def folder_size(self):
            return sum(int(self.files[f]) for f in self.files) + sum(self.sub_folders[s].folder_size() for s in self.sub_folders)

        # def small_folders(self):
        #     current_files_size = sum(int(self.files[f]) for f in self.files)
        #     sub_folders_size = sum(self.sub_folders[s].folder_size() for s in self.sub_folders)
        #     smalls = []

        #     current_folder_size = current_files_size + sub_folders_size
        #     if current_folder_size < self.size_limit:
        #         smalls.append(current_folder_size)

        #     for folder in self.sub_folders:
        #         sub_folder_size = self.sub_folders[folder].folder_size()
        #         if sub_folder_size < self.size_limit:
        #             smalls.append(self.sub_folders[folder].folder_size())
        #     return smalls

        def print(self):
            if self.size_limit == 100000 and self.folder_size() < self.size_limit:
                print(f"{self.folder_size()}")
            elif self.size_limit != 100000 and self.folder_size() >= self.size_limit:
                print(f"{self.folder_size()}")
            for folder in self.sub_folders:
                self.sub_folders[folder].print()

    def get_file_structure(self, size_limit):
        root = day7.folder("/", size_limit)
        cwd = root
        for line in self.lines:
            if "$ cd" in line:
                folder_name = line.split()[2]
                if folder_name == "/":
                    cwd = root
                elif folder_name == "..":
                    cwd = cwd.parent
                else:
                    cwd = cwd.sub_folders[folder_name]
            elif "$" not in line:
                if "dir" in line:
                    folder_name = line.split()[1]
                    cwd.add_sub_folder(folder_name)
                else:
                    filesize = line.split()[0]
                    filename = line.split()[1]
                    cwd.add_file(filename, filesize)

        return root

    def part1(self):
        structure = self.get_file_structure(100000)

        structure.print()

        return "Add up the values above"

    def part2(self):
        structure = self.get_file_structure(6090135)
        needed_space = structure.folder_size() - 40000000
        structure.print()

        return f"Smallest folder size at least {needed_space}"

today = day7()
today.solution()

