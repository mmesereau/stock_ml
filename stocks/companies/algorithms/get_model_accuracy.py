from sklearn.neural_network import MLPRegressor
from sklearn.metrics import mean_squared_error, r2_score
from .. import constructor
import math
import numpy
import warnings
import pandas
import pickle
warnings.filterwarnings(action="ignore", module="scipy", message="^internal gelsd")


def get_accuracy(company):
    try:
        print("hit function")
        #import data
        input_data = constructor.inputs(company)
        print("got input data")
        output_data = constructor.tomorrow_close(company)
        print("got data")

        #split the input data into training and testing data
        input_half = math.floor(input_data.shape[0] / 2)
        train_data = input_data[2:input_half]
        test_data = input_data[input_half:-2]

        #split the output data into training and testing data
        output_half = math.floor(output_data.shape[0] / 2)
        train_output = output_data[2:output_half]
        test_output = output_data[output_half:-2]
        print("got data")

        filename = 'companies/ml_models/' + company + '.sav'
        model = pickle.load(open(filename, 'rb'))
        print("stuff happens now...")

        return model.score(test_data, test_output)
    except:
        print("wtf?")
