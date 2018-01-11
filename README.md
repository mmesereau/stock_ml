Backlog:

I will be using the pickle tool (http://scikit-learn.org/stable/modules/model_persistence.html) to persist my models.  I expect around 550 Multi-Layer Perceptron models by the end, so I'll want to be able to persist at scale.

I will make a new classification algorithm to identify the most effective algorithms to use to produce good predictions.  Essentially, I'm going to nest a neural network inside another neural network.  The outside network will do the work of picking ideal parameters for me.

Using additional input parameters (which in this case are technical indicators), I will tweak the model to be more accurate.  This will also give me an idea of which technical indicators are more effective and which ones are not.

I will create industry-specific models that will predict industry-wide behavior.

I will make a master model that can apply to all companies.  Currently, every model I make only applies to a single company.  By generalizing, I will be able to avoid overfitting.

I will implement additional models such as a SVM or a HMM.  The more models, the more accurate.  I can then wrap the outputs of each of these models in a brand new model to identify the weights of each.

1/7/18 Update:

Created my first linear model.  This model ultimately has an R^2 of -0.87 for the MSFT data from Jan 3 2000 to Dec 8 2017.  This model has three parameters used to predict tomorrow's close: Today's close, Bollinger Differential and RSI.  This model was largely a failure because of the abysmal R^2.  

1/8/18 Update:
Created a Multi-Layer Perceptron Regression model.  The same three parameters from yesterday's model are being used.  I have found wild success with this model, partially because I have chosen to randomize some parameters for the model (number of hidden layers, activation function and solving method) and then automated running it until I find an acceptable R^2 on the training data.  R^2 seems to max out around 0.979 on the training data, and it often finds an R^2 of 0.999 on the testing data.  This is tremendous!  When I do end up with an R^2 on the testing data, I am able to predict the next day's close within 1.5%, usually undercutting the actual close.  

1/9/2018 Update:
I added get_companies.py to track which companies are on the S&P 500.  I can then run writeFiles.py on each company and write them to the companies folder.  


1/10 Update:
I have wrapped the application in the initial Django framework.  I will be using this to process incoming HTTP requests and communicate with the SQL database that has been set up.  I have collected the CSV data for all S&P 500 companies (and added them to the .gitignore file to limit the size of the git commits) and also added the companies to the database, with fields "name", "ticker" and "industry".  I also now have the framework to turn this into a web-based application if I desire to do so down the line.
