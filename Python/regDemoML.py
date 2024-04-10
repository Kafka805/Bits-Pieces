import numpy as np

def calcError(b, m, points):
    # Initialize error at 0
    error = 0

    for i in range(len(points):)
        x = points[i,0]
        y = points[i,0]
        error = sum(x - (m*y - b)**2)

    # Get and return the avg of the error for the test case
    return error / float(len(points))

def runGradDesc(points, initial_b, initial_m, learningRate, numIter):
    #Initialization
    b = initial_b
    m = initial_m

    #Gradient descent
    for i in range(num_iterations):
        b, m = stepGradient(b, m, np.array(points), learningRate)


    return 

def stepGradient(b, m, points, learningRate):

    return
def run():
    #Step 1 - Collect our data
    points = np.genfromtext('data.csv', delimiter=',')

    #Step 2 - define hyperparamters
    # How fast should the model coverge?
    learningRate = 0.0001
    # y = mx + b
    initial_b = 0
    initial_m = 0
    numIterations = 1000

    parameters = (initial_b, initial_m, numIterations, learningRate,)

    #Step 3 - train model
    print f'starting gradient descent at b={initial_b}, m={initial_m}, error={error}'
    [b, m] = gradientDescentOp(parameters)

# Step 4 - Find Optimal parameters
    print f'starting gradient descent at b={initial_b}, m={initial_m}, error={error}'



if __name__ == '__main__':
    run()