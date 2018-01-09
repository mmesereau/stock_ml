from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score
import constructor
import datetime
import math
import numpy
import warnings
warnings.filterwarnings(action="ignore", module="scipy", message="^internal gelsd")

def initial_regression_network(company, start="2000-01-03", end=datetime.date.today()):
    #import data
    input_data = constructor.inputs(company, start, end)
    output_data = constructor.tomorrow_close(company, start, end)

    #split the input data into training and testing data
    input_half = math.floor(input_data.shape[0] / 2)
    train_data = input_data[1:input_half]
    test_data = input_data[input_half:-1]

    #split the output data into training and testing data
    output_half = math.floor(output_data.shape[0] / 2)
    # print("Length problem!", input_half, output_half)
    # print(input_data.iloc[0])
    # print(input_data.iloc[-1])
    # print(output_data.iloc[0])
    # print(output_data.iloc[-1])
    train_output = output_data[1:output_half]
    test_output = output_data[output_half:-1]

    #initialize regression object
    model = linear_model.LinearRegression()

    #train the model using training sets
    model.fit(train_data, train_output)

    #make predictions using the testing set
    prediction = model.predict(test_data)
    print(model.predict(input_data.iloc[-2])[0], output_data.iloc[-1])

     #The coefficients
    print('Coefficients: \n', model.coef_)
    # The mean squared error
    print("Mean squared error: %.2f"
          % mean_squared_error(test_output, train_output))
    # Explained variance score: 1 is perfect prediction
    print('Variance score: %.2f' % r2_score(test_output, train_output))
