# Monte Carlo Estimation of π

This project uses a **Monte Carlo simulation** to estimate the value of **π** through random sampling.

## Overview

Imagine a **unit square** (side length = 1) containing a **quarter circle** of radius 1.

Random points are generated inside the square. By observing how many of these points fall inside the quarter circle, we can estimate the value of π.

---

## Mathematical Idea

### Step 1: Calculate the areas

For a circle of radius **1**:

* Area of the full circle = `π × 1² = π`
* Area of the quarter circle = `π / 4`

For the unit square:

* Area of the square = `1 × 1 = 1`

Therefore,

```text
Area of Quarter Circle / Area of Square = π / 4
```

---

### Step 2: Relate areas to random points

If random points are distributed uniformly inside the square, then:

```text
Points Inside Quarter Circle / Total Points ≈ π / 4
```

Rearranging,

```text
π ≈ 4 × (Points Inside Quarter Circle / Total Points)
```

---

## Algorithm

1. Generate random points `(x, y)` such that:

   ```text
   0 ≤ x ≤ 1
   0 ≤ y ≤ 1
   ```

2. Check whether the point lies inside the quarter circle:

   ```text
   x² + y² ≤ 1
   ```

3. Count the number of points inside the quarter circle.

4. Estimate π using:

   ```text
   π ≈ 4 × (Inside Points / Total Points)
   ```

---

## Sample Output

```text
Enter the number of trials: 1000000

Estimated value of π: 3.141872
```

---

## Results

As the number of trials increases, the estimate becomes more accurate.

This behavior illustrates the **Law of Large Numbers**, where experimental results converge toward their theoretical values as the sample size grows.

---

## Concepts Explored

* Monte Carlo Simulation
* Random Sampling
* Geometric Probability
* Estimation of Mathematical Constants
* Law of Large Numbers

---

## Technologies Used

* Python
* Matplotlib
* `random` module

---

## Key Takeaway

> Randomness can be used to estimate deterministic mathematical constants.

Through repeated random experiments, Monte Carlo methods provide an elegant computational approach to approximating values such as **π**, while also demonstrating fundamental principles of probability and statistics.
