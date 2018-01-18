from sklearn.neural_network import MLPRegressor
from sklearn.metrics import mean_squared_error, r2_score
import pickle

def update(company, data, output):
    try:
        filename = 'companies/ml_models/' + company + '.sav'
        model = pickle.load(open(filename, 'rb'))
        model.fit(data, output)
        pickle.dump(model, (open(filename, 'wb')))
    except:
        print("Something wrong with pickle?")
    return True
