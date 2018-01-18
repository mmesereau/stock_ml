from sklearn.neural_network import MLPRegressor
from sklearn.metrics import mean_squared_error, r2_score
import pickle

def use(company, data):
    filename = 'companies/ml_models/' + company + '.sav'
    model = pickle.load(open(filename, 'rb'))
    return model.predict(data)
