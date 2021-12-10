import matplotlib.pyplot as plt

def bezier (start, end, via2, via1) :
    """
    implements cubic Bézier curves between 'start' and 'end' and smoothly
    approaches via1 and via2 in between.

    see https://youtu.be/aVwxzDHniEw for a beautiful explanation on how they
    work

    start : tuple of two floats, start point of the curve
    end   : tuple of two floats, end   point of the curve
    via1  : tuple of two floats, first deviation point
    via2  : tuple of two floats, second deviation point
    returns : a function f(t) that computes the curve between t in [0...1]

    """

    if not (len(start) == len(end) == len(via1) == len(via2) == 2) :
        raise ValueError("Not a 2D point")

    def inner (t) :
        x = (1-t)**3 * start[0] + 3 *(1-t)**2 * t * via1[0] + 3 * (1-t) * t**2 * via2[0] + t**3 * end[0]
        y = (1-t)**3 * start[1] + 3 *(1-t)**2 * t * via1[1] + 3 * (1-t) * t**2 * via2[1] + t**3 * end[1]
        return (x, y)

    return inner

# ............................................................................ #

def get_smooth_curve (pts_through, pts_via) :
    """
    constructs a smooth curve through all poitns pts_through that goes near the
    points pts_via

    pts_through: list of tuples of two floats
    pts_via    : list of tuples of two floats
    returns: a function f(t) that computes the curve between t in [0...1]

    """

    if len(pts_through) != len(pts_via) :
        raise ValueError("Length of point lists must be equal")

    for through, via in zip(pts_through, pts_via) :
        if not (len(through) == len(via) == 2) :
            raise ValueError("Not a list of 2D points")

    def inner (t) :
        N = len(pts_through) - 1        # number of sections on the curve
        section_id = int(t * N)
        section_t = t * N - int(t * N)


        A = pts_through[section_id    ]
        B = pts_through[section_id + 1]

        if section_id :
            S = pts_via[section_id - 1]
            x = 2 * A[0] - S[0]
            y = 2 * A[1] - S[1]

        else :
            # use the subsequent via point
            x, y = pts_via[section_id + 1]

        C = pts_via    [section_id    ]
        D = (x, y)

        func = bezier(A, B, C, D)

        return func(section_t)



    return inner

# ............................................................................ #
# test code

#plt.figure()

#T = [t / 100 for t in range(100)]

#through = [(0.0, 0.0), (1.0, 1.0), (2.0, 0.0), (3.0, 0.5)]
#via     = [(0.3, 1.0), (0.6, 0.5), (1.5, 0.5), (3.0, 1.0)]

#func = bezier(through[0], through[1], via[0], via[1])

#X, Y = list(zip(*[func(t) for t in T]))
#plt.plot(X, Y)

#func = get_smooth_curve(through, via)

#X, Y = list(zip(*[func(t) for t in T]))

#plt.plot(X, Y)
#for A, C in zip(through, via) :
    #plt.plot(*A, "ro")
    #plt.plot(*C, "go")

#plt.show()

# ............................................................................ #
# the problem

N_points = 500
T = [t / N_points for t in range(N_points)]

dotted_through = [(3000,  1), (5000,  0)]
dotted_via     = [(5000, -1), (3000, -1)]

solid_through = [(5000,  0.0), (3000, 2.5), (7500, 2.0), (3000, 4.0), (25000, 4.0), (20000, -2)]
solid_via     = [*solid_through]

dotted_func = get_smooth_curve(dotted_through, dotted_via)
solid_func  = get_smooth_curve( solid_through,  solid_via)

dotted_X, dotted_Y = list(zip(*[dotted_func(t) for t in T]))
solid_X,   solid_Y = list(zip(*[ solid_func(t) for t in T]))
