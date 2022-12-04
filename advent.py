

class day1:
    def __init__(self):
        with open("day1.txt") as input:
            self.lines = input.readlines()

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

    def solution(self):
        part1_solution = self.part1()
        print(part1_solution)
        part2_solution = self.part2()
        print(part2_solution)

class day2:
    def __init__(self):
        with open("day2.txt") as input:
            self.lines = input.readlines()

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

class day3:
    def __init__(self):
        with open("day3.txt") as input:
            self.lines = input.readlines()

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

    def solution(self):
        part1_solution = self.part1()
        print(part1_solution)
        part2_solution = self.part2()
        print(part2_solution)

today = day3()
today.solution()

