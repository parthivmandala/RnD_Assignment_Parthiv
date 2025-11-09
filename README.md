Problem Statement

We are given a parametric curve defined as:

𝑥
(
𝑡
)
	
=
𝑋
+
𝑡
cos
⁡
(
𝜃
)
−
𝑒
𝑀
∣
𝑡
∣
sin
⁡
(
0.3
𝑡
)
sin
⁡
(
𝜃
)
,


𝑦
(
𝑡
)
	
=
42
+
𝑡
sin
⁡
(
𝜃
)
+
𝑒
𝑀
∣
𝑡
∣
sin
⁡
(
0.3
𝑡
)
cos
⁡
(
𝜃
)
x(t)
y(t)
	​

=X+tcos(θ)−e
M∣t∣
sin(0.3t)sin(θ),
=42+tsin(θ)+e
M∣t∣
sin(0.3t)cos(θ)
	​


with unknown parameters:

𝜃
,
  
𝑀
,
  
𝑋
.
θ,M,X.

Given constraints:

0
∘
<
𝜃
<
50
∘
,
−
0.05
<
𝑀
<
0.05
,
0
<
𝑋
<
100
,
6
<
𝑡
<
60.
0
∘
<θ<50
∘
,−0.05<M<0.05,0<X<100,6<t<60.

We are provided a dataset xy_data.csv containing samples of this curve for 
6
<
𝑡
<
60
6<t<60.
The task is to estimate the correct values of 
𝜃
,
𝑀
,
𝑋
θ,M,X such that the predicted curve matches the data with minimal L1 error.

Approach and Methodology (Explanation – Scoring Section)
1. Understanding the Curve Structure

The curve consists of:

A linear motion in direction 
𝜃
θ: 
(
𝑡
cos
⁡
𝜃
,
 
𝑡
sin
⁡
𝜃
)
(tcosθ, tsinθ)

A vertical sinusoidal displacement modulated by exponential scaling:

𝐴
(
𝑡
)
=
𝑒
𝑀
∣
𝑡
∣
sin
⁡
(
0.3
𝑡
)
A(t)=e
M∣t∣
sin(0.3t)

A constant translation (offset): 
(
𝑋
,
42
)
(X,42)

This means each data point 
(
𝑥
,
𝑦
)
(x,y) can be converted back to internal coordinates 
(
𝑡
,
𝐴
(
𝑡
)
)
(t,A(t)) using rotation.

2. Undoing the Rotation and Translation

For any guess of 
𝜃
θ and 
𝑋
X:

𝑢
=
𝑥
−
𝑋
,
𝑣
=
𝑦
−
42
u=x−X,v=y−42

Apply rotation by 
−
𝜃
−θ:

𝑡
=
𝑢
cos
⁡
𝜃
+
𝑣
sin
⁡
𝜃
t=ucosθ+vsinθ
𝐴
obs
=
−
𝑢
sin
⁡
𝜃
+
𝑣
cos
⁡
𝜃
A
obs
	​

=−usinθ+vcosθ

If 
𝜃
θ and 
𝑋
X are correct, 
𝑡
t should lie within 
(
6
,
60
)
(6,60) and 
𝐴
obs
A
obs
	​

 should match the model 
𝐴
(
𝑡
)
A(t).

3. Solving for 
𝑀
M

From the equation:

𝐴
(
𝑡
)
=
𝑒
𝑀
∣
𝑡
∣
sin
⁡
(
0.3
𝑡
)
A(t)=e
M∣t∣
sin(0.3t)

Taking log:

ln
⁡
(
∣
𝐴
obs
∣
∣
sin
⁡
(
0.3
𝑡
)
∣
)
≈
𝑀
∣
𝑡
∣
ln(
∣sin(0.3t)∣
∣A
obs
	​

∣
	​

)≈M∣t∣

This becomes a straight line in 
(
∣
𝑡
∣
,
 
log
⁡
(
⋅
)
)
(∣t∣, log(⋅)) → we use least-squares regression to solve for 
𝑀
M.

4. Parameter Search

A coarse-to-fine grid search was performed over 
𝜃
θ and 
𝑋
X.

For each pair, 
𝑀
M was solved using the log-linear method.

The model with minimum L1 error was selected.

5. Final Estimated Parameters
Parameter	Value

𝜃
θ	30.000503° (≈ 0.523608 rad)

𝑀
M	0.030108

𝑋
X	54.981792
Final Curve (Submission Format Required)
(
𝑡
cos
⁡
(
0.523608
)
−
𝑒
0.030108
∣
𝑡
∣
sin
⁡
(
0.3
𝑡
)
sin
⁡
(
0.523608
)
+
54.981792
,
  
42
+
𝑡
sin
⁡
(
0.523608
)
+
𝑒
0.030108
∣
𝑡
∣
sin
⁡
(
0.3
𝑡
)
cos
⁡
(
0.523608
)
)
(tcos(0.523608)−e
0.030108∣t∣
sin(0.3t)sin(0.523608)+54.981792,42+tsin(0.523608)+e
0.030108∣t∣
sin(0.3t)cos(0.523608))
	​

Evaluation (L1 Score)
Metric	Performance
Mean L1 error in internal A-space	≈ 0.01439
Mean L1 error in (x,y) space	≈ 0.01966

This is very low → indicating a very accurate parameter recovery.