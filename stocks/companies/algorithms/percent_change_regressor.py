from sklearn.neural_network import MLPRegressor
from sklearn.metrics import mean_squared_error, r2_score
from .. import constructor
import datetime
import math
import numpy
import warnings
import random
import pandas
import pickle
warnings.filterwarnings(action="ignore", module="scipy", message="^internal gelsd")

def perceptron_regressor(company, start="2000-01-03", end=datetime.date.today(), tries=0, max_trainr2=0, max_testr2=0, fails=0):
    hidden_layer_sizes = math.ceil(random.random() * 10)
    activation = random.choice(["identity", "logistic", "tanh", "relu"])
    solver = random.choice(["lbfgs", "sgd", "adam"])
    max_iter = 400

    testr2 = 0
    trainr2 = 0

    #import data
    input_data = constructor.inputs(company)
    output_data = constructor.percent_gain(company)

    #split the input data into training and testing data
    input_half = math.floor(input_data.shape[0] / 2)
    train_data = input_data[2:input_half]
    test_data = input_data[input_half:-2]

    #split the output data into training and testing data
    output_half = math.floor(output_data.shape[0] / 2)
    train_output = output_data[2:output_half]
    test_output = output_data[output_half:-2]

    trainr2 = 0
    testr2 = 0


    #set up the model
    model = MLPRegressor(hidden_layer_sizes=hidden_layer_sizes, activation=activation, solver=solver, alpha=0.0001,
                         batch_size="auto", learning_rate="constant", learning_rate_init=0.01,
                         power_t=0.5, max_iter=max_iter, shuffle=False, random_state=None, tol=0.0001, verbose=False, warm_start=False, momentum=0.9,
                         nesterovs_momentum=True, early_stopping=False, validation_fraction=0.1, beta_1=0.9, beta_2=0.999,
                         epsilon=1e-08)
    model = model.fit(train_data, train_output)
    try:
        trainr2 = model.score(train_data, train_output)
        testr2 = model.score(test_data, test_output)
    except:
        print("error computing r squared")
    if trainr2 > .5 or fails > 10:
        return [trainr2, testr2]
    else:
        fails = fails + 1
        print(trainr2, testr2)
        return perceptron_regressor(company)