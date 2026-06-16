# Monte Carlo Estimation of π

This project uses a **Monte Carlo simulation** to estimate the value of **π** through random sampling.

## Overview

A unit square of side length **1** contains a quarter circle of radius **1**. Random points are generated uniformly inside the square. By calculating the proportion of points that fall inside the quarter circle, the value of π can be approximated.

## Mathematical Idea

For a quarter circle of radius 1:

* Area of quarter circle:

  [
  \frac{\pi r^2}{4} = \frac{\pi}{4}
  ]

* Area of square:

  [
  1 \times 1 = 1
  ]

Therefore,

[
\frac{\text{Area of Quarter Circle}}{\text{Area of Square}} = \frac{\pi}{4}
]

Since randomly generated points are uniformly distributed within the square,

[
\frac{\text{Points Inside Quarter Circle}}{\text{Total Points}} \approx \frac{\pi}{4}
]

which gives:

[
\pi \approx 4 \times \frac{\text{Points Inside Quarter Circle}}{\text{Total Points}}
]

## Algorithm

1. Generate random points ((x, y)) where:

   [
   0 \le x \le 1,\quad 0 \le y \le 1
   ]

2. Check whether the point lies inside the quarter circle:

   [
   x^2 + y^2 \le 1
   ]

3. Count the number of points inside the quarter circle.

4. Estimate π using:

   [
   \pi \approx 4 \times \frac{\text{Inside Points}}{\text{Total Points}}
   ]

## Sample Output

```text
Enter the number of trials: 1000000

Estimated value of π: 3.141872
```

## Results

As the number of trials increases, the estimate becomes increasingly accurate. This behavior demonstrates the **Law of Large Numbers**, where experimental results converge toward theoretical values with larger sample sizes.

## Concepts Explored

* Monte Carlo Simulation
* Random Sampling
* Geometric Probability
* Estimation of Mathematical Constants
* Law of Large Numbers

## Technologies Used

* Python
* Matplotlib
* `random` module

## Key Takeaway

> Monte Carlo methods show that randomness can be used to estimate deterministic quantities such as π with remarkable accuracy.

