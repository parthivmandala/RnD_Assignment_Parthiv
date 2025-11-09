import numpy as np
import pandas as pd

# Load your data
df = pd.read_csv("xy_data.csv")
data = df[['x','y']].to_numpy()

# Parameter ranges
X_RANGE = (0, 100)
TH_RANGE_DEG = (0, 50)
M_RANGE = (-0.05, 0.05)

def fit_M_for_theta_X(theta_deg, X_offset, data_xy):
    theta = np.deg2rad(theta_deg)
    x = data_xy[:,0]; y = data_xy[:,1]
    u = x - X_offset
    v = y - 42.0
    t = u*np.cos(theta) + v*np.sin(theta)
    Aobs = -u*np.sin(theta) + v*np.cos(theta)

    mask = (t > 6) & (t < 60)
    sin_part = np.sin(0.3*t)
    mask &= (np.abs(sin_part) > 1e-6)

    t_sel = t[mask]
    A_sel = Aobs[mask]
    sin_sel = sin_part[mask]

    if len(t_sel) < 10:
        return None

    sign_mask = (A_sel * sin_sel) > 0
    t_sel = t_sel[sign_mask]
    A_sel = A_sel[sign_mask]
    sin_sel = sin_sel[sign_mask]

    if len(t_sel) < 10:
        return None

    ylin = np.log(np.abs(A_sel) / np.abs(sin_sel))
    xlin = np.abs(t_sel)

    M_hat = np.dot(xlin, ylin) / np.dot(xlin, xlin)
    M_hat = np.clip(M_hat, M_RANGE[0], M_RANGE[1])

    A_pred = np.exp(M_hat*np.abs(t_sel)) * np.sin(0.3*t_sel)
    err = np.mean(np.abs(A_sel - A_pred))

    return {"M": M_hat, "err": err, "used": len(t_sel)}

x_min, x_max = df.x.min(), df.x.max()
best = None

for th in np.linspace(0.25, 49.75, 200):
    X_lo = max(0, x_min - 25)
    X_hi = min(100, x_max + 25)

    for Xoff in np.linspace(X_lo, X_hi, 160):
        res = fit_M_for_theta_X(th, Xoff, data)
        if res is None:
            continue

        score = res["err"] - 1e-5*res["used"]
        if (best is None) or (score < best["score"]):
            best = {"theta_deg": th, "X": Xoff, "M": res["M"], "score": score}

best_local = best.copy()

for th in np.linspace(best["theta_deg"]-1, best["theta_deg"]+1, 161):
    for Xoff in np.linspace(best["X"]-5, best["X"]+5, 161):
        res = fit_M_for_theta_X(th, Xoff, data)
        if res is None:
            continue

        score = res["err"] - 1e-5*res["used"]
        if score < best_local["score"]:
            best_local = {"theta_deg": th, "X": Xoff, "M": res["M"], "score": score}

theta_deg = best_local["theta_deg"]
theta_rad = np.deg2rad(theta_deg)
M = best_local["M"]
Xoff = best_local["X"]

print("=== Estimated parameters ===")
print(f"theta  = {theta_deg:.6f} degrees  (radians {theta_rad:.6f})")
print(f"M      = {M:.6f}")
print(f"X      = {Xoff:.6f}")

submission = (
    f"\\left(t*\\cos({theta_rad:.6f})-e^{{{M:.6f}|t|}}\\cdot\\sin(0.3t)\\sin({theta_rad:.6f})"
    f"+{Xoff:.6f},\\ 42+t*\\sin({theta_rad:.6f})+e^{{{M:.6f}|t|}}\\cdot\\sin(0.3t)\\cos({theta_rad:.6f})\\right)"
)

print("\nSubmission:")
print(submission)

# -------- SAVE SCRIPT SAFELY --------
with open("fit_params_xy_model_full.py", "w") as f:
    f.write(open(__file__, "r").read())

