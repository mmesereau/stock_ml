from sklearn.neural_network import MLPRegressor
from sklearn.metrics import mean_squared_error, r2_score
import constructor
import datetime
import math
import numpy
import warnings
import random
warnings.filterwarnings(action="ignore", module="scipy", message="^internal gelsd")


def perceptron_regressor(company, start="2000-01-03", end=datetime.date.today()):
    #import data
    input_data = constructor.inputs(company)
    output_data = constructor.tomorrow_close(company)

    #split the input data into training and testing data
    input_half = math.floor(input_data.shape[0] / 2)
    train_data = input_data[2:input_half]
    test_data = input_data[input_half:-2]

    #split the output data into training and testing data
    output_half = math.floor(output_data.shape[0] / 2)
    train_output = output_data[2:output_half]
    test_output = output_data[output_half:-2]

    #randomize some parameters to identify effectiveness
    hidden_layer_sizes = math.ceil(random.random() * 10)
    activation = random.choice(["identity", "logistic", "tanh", "relu"])
    solver = random.choice(["lbfgs", "sgd", "adam"])


    #set up the model
    model = MLPRegressor(hidden_layer_sizes=(hidden_layer_sizes,), activation=activation, solver=solver, alpha=0.0001,
                         batch_size="auto", learning_rate="constant", learning_rate_init=0.01,
                         power_t=0.5, max_iter=10000, shuffle=False, random_state=None, tol=0.0001, verbose=False, warm_start=False, momentum=0.9,
                         nesterovs_momentum=True, early_stopping=True, validation_fraction=0.1, beta_1=0.9, beta_2=0.999,
                         epsilon=1e-08)

    model = model.fit(train_data, train_output)
    if model.score(train_data, train_output) > 0.979:
        print("R squared on training data: ", model.score(train_data, train_output))
        print("R squared on test data ", model.score(test_data, test_output))
        print("Statistics: ", hidden_layer_sizes, " hidden layers; Activation function: ", activation, " Solver: ", solver)
        print("Tomorrow's actual: ", input_data.iloc[-1][company])
        print("Tomorrow's prediction: ", model.predict(input_data.iloc[-1:]))
        if abs(model.predict(input_data.iloc[-2:-1])[0] - input_data.iloc[-1][company]) > 1:
            perceptron_regressor(company, start, end)

    else:
        print("Failed attempt: ", model.score(train_data, train_output))
        print("Statistics: ", hidden_layer_sizes, " hidden layers; Activation function: ", activation, " Solver: ", solver)
        perceptron_regressor(company, start, end)
