# Using the Gradient Descent algorithm
import subprocess

def create_hypothesis(slope, x0):
    return lambda x: slope*x + x0

def linear_regression(data_points, learning_rate=0.01, variance=0.001):
    """ Takes a set of data points in the form: [(1,1), (2,2), ...] and outputs (slope, x0). """

    slope_guess = 1.
    x0_guess = 1.

    last_slope = 1000.
    last_x0 = 1000.
    num_points = len(data_points)

    while (abs(slope_guess-last_slope) > variance or abs(x0_guess - last_x0) > variance):
        last_slope = slope_guess
        last_x0 = x0_guess

        hypothesis = create_hypothesis(slope_guess, x0_guess)

        x0_guess = x0_guess - learning_rate * (1./num_points) * sum([hypothesis(point[0]) - point[1] for point in data_points])
        slope_guess = slope_guess - learning_rate * (1./num_points) * sum([ (hypothesis(point[0]) - point[1]) * point[0] for point in data_points])

    return (slope_guess, x0_guess)

def plot_data_and_line(line, data_file):
    # Plot with gnuplot
    plot = subprocess.Popen(['gnuplot'], stdin=subprocess.PIPE)
    line_eq = "%f*x+%f" % line
    plot.communicate("plot %s, '%s' with points;" % (line_eq,data_file))

if __name__ == "__main__":
    data_file = "points.dat"
    points_str = [line.strip().split('\t') for line in open(data_file,'r').readlines()]
    points = [(float(x),float(y)) for (x,y) in points_str]
    line = linear_regression(points)
    print line

    plot_data_and_line(line, data_file)
