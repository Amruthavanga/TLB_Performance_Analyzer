from collections import OrderedDict

PAGE_SIZE = 256
TLB_TIME = 10
MEMORY_TIME = 100

PAGE_TABLE = {
    0: 5, 1: 2, 2: 8, 3: 1,
    4: 6, 5: 3, 6: 9, 7: 4,
    8: 7, 9: 0, 10: 10, 11: 11,
    12: 12, 13: 13, 14: 14, 15: 15
}


class TLBSimulator:
    def __init__(self, capacity, policy):
        self.capacity = capacity
        self.policy = policy
        self.tlb = OrderedDict()
        self.hits = 0
        self.misses = 0

    def translate(self, address):
        if address < 0 or address >= 4096:
            print("Invalid address! Use 0 to 4095.")
            return

        page = address // PAGE_SIZE
        offset = address % PAGE_SIZE

        if page in self.tlb:
            self.hits += 1
            frame = self.tlb[page]
            if self.policy == "LRU":
                self.tlb.move_to_end(page)
            status = "TLB HIT"
        else:
            self.misses += 1
            frame = PAGE_TABLE[page]
            status = "TLB MISS"

            if len(self.tlb) >= self.capacity:
                self.tlb.popitem(
                    last=False
                )

            self.tlb[page] = frame

        physical = frame * PAGE_SIZE + offset

        print("\nVirtual Address :", address)
        print("Page Number     :", page)
        print("Offset          :", offset)
        print("Status          :", status)
        print("Frame Number    :", frame)
        print("Physical Address:", physical)

    def report(self):
        total = self.hits + self.misses

        if total == 0:
            print("No addresses processed yet.")
            return

        hit_ratio = self.hits / total
        miss_ratio = self.misses / total

        emat = (
            TLB_TIME
            + hit_ratio * MEMORY_TIME
            + miss_ratio * 2 * MEMORY_TIME
        )

        print("\n--- PERFORMANCE REPORT ---")
        print("Total accesses :", total)
        print("TLB Hits       :", self.hits)
        print("TLB Misses     :", self.misses)
        print(f"Hit Ratio      : {hit_ratio:.2%}")
        print(f"Miss Ratio     : {miss_ratio:.2%}")
        print(f"Average Time   : {emat:.2f} ns")
        print("TLB Entries    :", dict(self.tlb))


def main():
    print("TLB PERFORMANCE ANALYSIS SIMULATOR")

    try:
        capacity = int(input("TLB capacity (1-16): "))
        if not 1 <= capacity <= 16:
            print("Capacity must be between 1 and 16.")
            return

        policy = input("Policy (FIFO/LRU): ").strip().upper()
        if policy not in ("FIFO", "LRU"):
            print("Choose FIFO or LRU.")
            return

    except ValueError:
        print("Enter valid input.")
        return

    sim = TLBSimulator(capacity, policy)

    while True:
        print("\n1. Translate address")
        print("2. Performance report")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            try:
                address = int(input("Virtual address (0-4095): "))
                sim.translate(address)
            except ValueError:
                print("Enter a valid integer.")

        elif choice == "2":
            sim.report()

        elif choice == "3":
            print("Simulation completed!")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()