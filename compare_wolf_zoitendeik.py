from zoitendeik_lib.Zoitendeik import *

if __name__ == '__main__':
    phi0 = Target_function(lambda x: (x[0] - 8) ** 2 + (x[1] + 2) ** 2,
                           lambda x: [2 * (x[0] - 8), 2 * (x[1] + 2)])

    phi1 = Constraint('ineq',
                      lambda x: -0.5*x[0] - x[1] + 2,
                      lambda x: [-0.5, -1])

    phi2 = Constraint('ineq',
                      lambda x: -1.5*x[0] - x[1] + 3,
                      lambda x: [-1.5, -1])

    phi3 = Constraint('ineq',
                      lambda x: -x[0],
                      lambda x: [-1, 0])

    phi4 = Constraint('ineq',
                      lambda x: -x[1],
                      lambda x: [0, -1])

    z = Zoitendeik_step(phi0, [phi1, phi2, phi3, phi4], [0.0, 0.0], 0.25, 0.5)

    # K, R изменены в Zoitendeik.py

    z.minimize(eps=0.01)
