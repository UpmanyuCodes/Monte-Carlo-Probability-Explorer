import random
import matplotlib.pyplot as plt

head_count = 0
tail_count = 0

running_probability = []

n = int(input("Enter the number of trials: "))

for toss in range(1, n + 1):

    result = random.choice(["heads", "tails"])

    if result == "heads":
        head_count += 1
    else:
        tail_count += 1

    current_probability = head_count / toss
    running_probability.append(current_probability)


final_head_probability = head_count / n
final_tail_probability = tail_count / n

print("\n----- Simulation Results -----")
print(f"Total Trials           : {n}")
print(f"Heads                  : {head_count}")
print(f"Tails                  : {tail_count}")
print(f"P(Heads) Experimental  : {final_head_probability:.4f}")
print(f"P(Tails) Experimental  : {final_tail_probability:.4f}")
print(f"P(Heads) Theoretical   : {0.5:.4f}")
print(f"P(Tails) Theoretical   : {0.5:.4f}")


plt.figure(figsize=(12, 6))

plt.plot(
    range(1, n + 1),
    running_probability,
    linewidth=2,
    label="Experimental Probability of Heads"
)

plt.axhline(
    y=0.5,
    linestyle="--",
    linewidth=2,
    label="Theoretical Probability (0.5)"
)

plt.xlabel("Number of Trials")
plt.ylabel("Probability")
plt.title("Monte Carlo Simulation: Convergence of Experimental Probability")
plt.xlim(1, n)
plt.ylim(0, 1)

plt.grid(alpha=0.3)
plt.legend()

plt.tight_layout()
plt.savefig('coin_toss_graph.png', dpi=100)
print("\nGraph saved as 'coin_toss_graph.png'")
plt.show()