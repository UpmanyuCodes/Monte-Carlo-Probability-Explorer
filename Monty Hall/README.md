# Monty Hall Problem Simulation

This project uses a Monte Carlo simulation to explore the famous **Monty Hall Problem** and demonstrate why **switching doors gives a 2/3 probability of winning**, even though many people initially believe the odds become 50-50.

## The Problem

Imagine you are a contestant on a game show with **three doors**:

* Behind **one door** is a car  (the prize).
* Behind the **other two doors** are goats .

The game proceeds as follows:

1. You choose one of the three doors.
2. The host, who **knows where the car is**, opens one of the remaining doors that definitely contains a goat.
3. You are then given a choice:

   * **Stay** with your original door.
   * **Switch** to the other unopened door.

The question is:

> **Should you switch, stay, or does it not matter?**

---

## A Common Misconception

After the host opens a door, many people reason that:

> "There are only two doors left, so the probability must be 50-50."

However, this intuition is incorrect.

### The Correct Probabilities

* Probability that your **initial choice was correct**:

```text
1/3
```

* Probability that your **initial choice was incorrect**:

```text
2/3
```

Since the host always reveals a goat and never opens the door with the car, the entire **2/3 probability transfers to the remaining unopened door**.

Therefore:

```text
Stay   → 1/3 chance of winning
Switch → 2/3 chance of winning
```

---

## Why This Simulation?

The Monty Hall result is often counterintuitive, and many people remain unconvinced even after seeing the mathematical explanation.

To investigate this phenomenon, I implemented a **Monte Carlo simulation** that repeatedly plays the Monty Hall game thousands of times and records the outcomes for both strategies:

* Always **staying** with the initial choice.
* Always **switching** after the host reveals a goat.

As the number of trials increases, the experimental probabilities converge toward their theoretical values.

---

## Sample Results

```text
Stay   : 0.3331
Switch : 0.6669
```

These values may vary slightly between runs due to randomness, but with a sufficiently large number of trials, they consistently approach:

```text
Stay   → 1/3
Switch → 2/3
```

---

## Key Takeaway

> The Monty Hall Problem demonstrates that intuition can sometimes be misleading in probability.

Despite appearing to be a 50-50 situation after one door is opened, switching doors doubles the probability of winning.

This simulation provides an empirical demonstration of that result using repeated random experiments.
