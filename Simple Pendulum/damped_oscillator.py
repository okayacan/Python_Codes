
from matplotlib import pyplot as plt
from scipy.integrate import ode

# Model Parameters
y0, t0 = [5.0,0.0], 0
kappa = 2.0
eta = 0.1

def f(t, y, arg1,arg2):
    # Sistem
    # x' = u
    # u' = -n*u -k*x
    #
    return [y[1], -arg1*y[0]-arg2*y[1]]


r = ode(f).set_integrator('vode', with_jacobian=False)
r.set_initial_value(y0, t0).set_f_params(kappa,eta)
t1 = 20
dt = 0.01
ts=list()
xs=list()
vs=list()
f = open("damped-oscillator.dat","w")
while r.successful() and r.t < t1:
    ts.append(r.t)
    xs.append(r.y[0])
    vs.append(r.y[1])
    r.integrate(r.t+dt)
    print(r.t,r.y[0],r.y[1],file=f) # to cast results to file f
f.close()
plt.plot(ts,xs,ts,vs)
plt.title("Damped Oscillator Time Course")
plt.xlabel("Time(a.u.)")
plt.ylabel("Deviation from eq.(a.u)")
plt.legend(["x(t)","v(t)"])
plt.show()