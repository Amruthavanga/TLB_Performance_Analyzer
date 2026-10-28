import matplotlib.pyplot as plt

# Sample data for demonstration only
capacities = [2, 4, 8]
fifo_hit_ratio = [40, 60, 80]
lru_hit_ratio = [50, 70, 90]

plt.figure(figsize=(8, 5))

plt.plot(capacities, fifo_hit_ratio, marker="o", label="FIFO")
plt.plot(capacities, lru_hit_ratio, marker="s", label="LRU")

plt.title("TLB Performance Analysis")
plt.xlabel("TLB Capacity")
plt.ylabel("Hit Ratio (%)")
plt.xticks(capacities)
plt.ylim(0, 100)
plt.grid(True)
plt.legend()
plt.tight_layout()

plt.savefig("tlb_performance.png")
plt.show()

print("Graph saved as tlb_performance.png")