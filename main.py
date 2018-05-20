from matplotlib.pyplot import figure, show
from numpy import arange, sin, pi, sinh, arctan, abs, tan, power
from fractions import Fraction

t = arange(-1.0, 1.0, 0.01)

fig = figure(1)
fig.tight_layout()

ax1 = fig.add_subplot(331)
ax1.plot(t, (3 + 100)*arctan(sinh(t*0.25)*5) / (pi + 100 * abs(t)))
ax1.grid(True)
ax1.set_ylim((-2, 2))
ax1.set_ylabel('Amplitude (dB)')
ax1.set_xlabel('Time (s)')
ax1.set_title('Gutter Distortion Curve')

ax2 = fig.add_subplot(332)
ax2.plot(t, ( 3 + 100 ) * tan(t) * 37 * (pi / 180) / ( pi + 100 * abs(t) ))
ax2.grid(True)
ax2.set_ylim((-2, 2))
ax2.set_ylabel('Amplitude (dB)')
ax2.set_xlabel('Time (s)')
ax2.set_title('Oddball Distortion Curve')

ax3 = fig.add_subplot(333)
ax3.plot(t, ( 3 + 100 ) * sin(t / 2) * 120 * (pi / 260) / ( pi + (100 * 2.41) * abs(sin(t / 3.45)) ))
ax3.grid(True)
ax3.set_ylim((-2, 2))
ax3.set_ylabel('Amplitude (dB)')
ax3.set_xlabel('Time (s)')
ax3.set_title('Simple Distortion Curve')

ax4 = fig.add_subplot(334)
ax4.plot(t, ( 3 + 100 ) * sin(t / 5) * 120 * (pi / 260) / ( pi + (100 * 2.41) * abs(sin(t / 9)) ))
ax4.grid(True)
ax4.set_ylim((-2, 2))
ax4.set_ylabel('Amplitude (dB)')
ax4.set_xlabel('Time (s)')
ax4.set_title('Smooth Distortion Curve')

ax5 = fig.add_subplot(335)
ax5.plot(t, ( 3 + 100 ) * power(t, 0.6) * 20 * (pi / 270) / ( pi + 100 * abs(power(t, 0.6)) ))
ax5.grid(True)
ax5.set_ylim((-2, 2))
ax5.set_ylabel('Amplitude (dB)')
ax5.set_xlabel('Time (s)')
ax5.set_title('Ultra Metal Distortion Curve')

ax6 = fig.add_subplot(336)
ax6.plot(t, ( 3 + 100 ) * sin(t) * 68 * (pi / 200) / ( pi + (100 * 0.9) * abs(t) ))
ax6.grid(True)
ax6.set_ylim((-2, 2))
ax6.set_ylabel('Amplitude (dB)')
ax6.set_xlabel('Time (s)')
ax6.set_title('Vintage Distortion Curve')

show()

