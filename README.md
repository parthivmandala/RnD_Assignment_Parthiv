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
