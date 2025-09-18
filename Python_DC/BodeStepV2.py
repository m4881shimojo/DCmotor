import numpy as np
import matplotlib.pyplot as plt
import control

# 伝達関数 G(s) 
#DC-motor単体の伝達関数
##num = [302000.]
#den = [0.01170222,42.45808241,9120.699]
##DC-motor＋負荷の伝達関数Simpy
num = [0.0302*5,0.0302*0.05,0.0302*1e5]
den = [5.85111e-9,2.12290585111e-5,0.01291843449,30.324708012,91.503]
#手計算伝達関数
#num = [1.51e-1, 1.51e-3,3.02e3] #S^2,s^1,s^0 の順
#den = [1.279e-2,29.9,90.902] #S^3,s^2,s^1,s^0 の順
sys = control.TransferFunction(num, den)

# 2. 時間範囲の作成 (linspaceを使用)
# 0から2秒までを1000分割
# linspace(開始, 終了, 分割数)
t= np.linspace(0, 2, 1000)

# =========================
# 1. ステップ応答 (axで描画)
# =========================
t, y = control.step_response(sys,t)

fig, ax1 = plt.subplots(figsize=(7,5))
ax1.plot(t, y, 'b')
ax1.set_xlabel("Time [s]")
ax1.set_ylabel("Response")
ax1.set_title("Step Response")
ax1.grid(True)

plt.tight_layout()

# =========================
# 2. Bode 線図（ゲイン＋位相）
# =========================
f_min = 1   # Hz
f_max = 10000   # Hz
f = np.logspace(np.log10(f_min), np.log10(f_max), 1000)  # 対数スケール
w = 2 * np.pi * f  # rad/s に変換

# Bode 特性を数値計算
#mag, phase, omega = control.freqresp(sys, w)
mag, phase, omega = control.frequency_response(sys, w)

fig, ax1 = plt.subplots(figsize=(8,5))

# ゲイン (dB)
ax1.semilogx(f, 20*np.log10(np.abs(mag)), 'b-', label="Magnitude [dB]")
ax1.set_xlabel("Frequency [Hz]")
ax1.set_ylabel("Magnitude [dB]", color='b')
ax1.grid(True, which="both")
ax1.tick_params(axis='y', labelcolor='b')

# 位相 (deg) を右軸に
ax2 = ax1.twinx()
ax2.semilogx(f, np.degrees(phase), 'r--', label="Phase [deg]")
ax2.set_ylabel("Phase [deg]", color='r')
ax2.tick_params(axis='y', labelcolor='r')
#ax2.set_ylim(-200, 20)
#ax2.set_yticks(np.arange(-200, 21, 20))    # 20刻みで補助線

plt.title("Bode Diagram")
plt.tight_layout()


plt.show()