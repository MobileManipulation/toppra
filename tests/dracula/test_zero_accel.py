from scipy.interpolate import CubicSpline

from toppra.dracula.zero_acceleration_start_end import impose_natural_bc

if __name__ == "__main__":
    t = [0, 3, 8, 12]
    knots = [(0, 0, 3, -2), (1, 2, 0, -3), (2, 0, 4, 2), (3, -1, 2, 0)]
    cspl = CubicSpline(t, knots, bc_type="clamped")
    impose_natural_bc(cspl)
