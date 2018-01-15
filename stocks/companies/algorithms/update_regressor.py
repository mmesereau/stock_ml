from sklearn.neural_network import MLPRegressor
from sklearn.metrics import mean_squared_error, r2_score
import pickle

def update(company, data):
    filename = 'companies/ml_models/' + company + '.sav'
    model = pickle.load(filename)
    model.train(data)
    pickle.dump(model, (open(filename, 'wb')))
    return True
