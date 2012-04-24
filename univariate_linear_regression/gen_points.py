import random

def randvar(n):
   neg = -1 if random.randrange(2) else 1
   return n * random.random() * neg

def points_with_variance(num_points, slope, x0, variance):
    func = lambda x: slope*x+x0
    points = []
    for i in range(num_points):
        points.append((i, func(i) + randvar(variance)))
    return points

if __name__ == "__main__":
    points = points_with_variance(15, -10, 100, 15)
    points_output = ["%f\t%f\n" % (p[0],p[1]) for p in points]

    output_file_name = "points.dat"
    outfile = open(output_file_name, 'w')
    outfile.writelines(points_output)
    outfile.close()

