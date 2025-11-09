# Assignment Submission – Research & Development / AI

## Problem Statement

We are given a parametric curve:

$$
x(t) = X + t\cos(\theta) - e^{M|t|}\sin(0.3t)\sin(\theta)
$$

$$
y(t) = 42 + t\sin(\theta) + e^{M|t|}\sin(0.3t)\cos(\theta)
$$

The unknown parameters are:

$$
\theta,\ M,\ X
$$

with the constraints:

$$
0^\circ < \theta < 50^\circ,\quad -0.05 < M < 0.05,\quad 0 < X < 100,\quad 6 < t < 60
$$

We are given `xy_data.csv` containing sampled points from this curve.  
Our objective is to estimate the values of **θ, M, X** such that the model best fits the data by minimizing **L1 error**.

---

## Approach and Methodology

### 1. Curve Decomposition

The curve can be interpreted as:

| Component | Meaning |
|----------|---------|
| $(t\cos\theta,\ t\sin\theta)$ | Linear direction movement |
| $A(t)=e^{M|t|}\sin(0.3t)$ | Oscillatory displacement term |
| $(X,42)$ | Translation offset |

So internally, each point can be viewed as:

$$
(t,\ A(t))
$$

### 2. Inverse Mapping (Recovering Internal Coordinates)

For any guess of \( \theta \) and \( X \):

$$
u = x - X,\quad v = y - 42
$$

Reverse rotation:

$$
t = u\cos(\theta) + v\sin(\theta)
$$
$$
A_{obs} = -u\sin(\theta) + v\cos(\theta)
$$

### 3. Solving for M

From:

$$
A(t) = e^{M|t|}\sin(0.3t)
$$

Taking log:

$$
\ln\left(\frac{|A_{obs}|}{|\sin(0.3t)|}\right) \approx M|t|
$$

This forms a **linear regression** problem to estimate \( M \).

### 4. Parameter Search Strategy

- Grid search over \(\theta\) and \(X\)
- For each pair, compute \(M\) from regression
- Evaluate mean L1 error
- Select parameters with minimum error

---

## Final Estimated Parameters

| Parameter | Value |
|----------|--------|
| θ | **30.000503°** (≈ 0.523608 radians) |
| M | **0.030108** |
| X | **54.981792** |

---

## Final Curve
$$
\left(t*\cos(0.523608)-e^{0.030108|t|}\cdot\sin(0.3t)\sin(0.523608)+54.981792,\ 42+t*\sin(0.523608)+e^{0.030108|t|}\cdot\sin(0.3t)\cos(0.523608)\right)
$$

---

## L1 Error Evaluation

To evaluate how closely the predicted curve matches the observed data, we use the **L1 distance** between corresponding points.

For each point, the L1 distance is computed as:

$$
d_i = \left| x_{\text{obs},i} - x_{\text{pred},i} \right| + \left| y_{\text{obs},i} - y_{\text{pred},i} \right|
$$

The overall fitting score is the mean of all such distances:

$$
\text{L1 Score} = \frac{1}{N}\sum_{i=1}^{N} d_i
$$

Using the estimated parameters:

$$
\theta = 30.000503^\circ,\quad M = 0.030108,\quad X = 54.981792
$$

The calculated L1 score is:

$$
\boxed{\text{L1 Score} = 0.01966}
$$

This value is **very low**, indicating that the predicted curve fits the observed dataset **very accurately**.

This value is very small, indicating that the predicted parametric curve matches the observed data with high accuracy.

