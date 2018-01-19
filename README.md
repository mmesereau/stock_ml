Backlog:

It turns out that the daily update takes quite some time.  I will want to run the process as an overnight process, so I will have to have a perpetually running server.  I don't want this to be cloud hosted, so I will need to acquire a local server.  I may at some point need to find an alternative data source, as Alpha Vantage varies from near-instantaneous response times to tens of seconds response times.  With 500 API requests made every day, the response time makes a large difference.

I will have the overnight process first update the csv file for every company to show today's information.  I will compare today's actual close to today's prediction so that I can track the accuracy of my model.  I will use today's information to make a prediction for tomorrow's close.  I will use today's information as additional training data on all of my models.

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

1/11 Update:
I wrote an API endpoint that runs through 100 randomized models for each company and stores the model parameters, training R^2 and testing R^2.  An average model takes about 10 seconds to train, but I'm doing 100 test models for 500 companies, which comes out to 500,000 seconds or 5.8 days.  This is highly impractical.  My new approach will be to identify successful models using randomized parameters and R^2 measurements, then persist one model per company using the pickle tool.

1/11 Update (II):
I wrote the endpoint described above and edited the existing MLP regressor to then pickle the best model that the function makes.  I also wrote the update_csv endpoint, which will find any dates within the last 100 trading days and add them to the csv files.  The update_csv endpoint will be part of my overnight process.  Tomorrow, I will create models for every company, as right now I only have a model for one.

1/14 Update:
I have generated the models.  Most of them (at least 9 out of 10) were generated with an R^2 of over .99 on testing data.  Some were generated with a much lower testing R^2 (more like 0.6, which is basically useless), and some encountered errors altogether (breaking when attempting to calculate R^2 for either testing or training data).  The models that survived have been saved using the pickle plugin.  
I have written an endpoint to use a model to make a prediction for the future.  I have also written an endpoint to return the actual close for a company on a date.  The framework is in place for an endpoint to retrain the model with today's data, but that has not been completed yet.

1/17 Update:
I have written the whole overnight process and run it twice.  The results of the predictions are underwhelming.  I will continue to refine my models, one particular possibility is to have the output as the percent change rather than the trading value, since that is what I'm ultimately after anyways, and this approach will limit the values to closer to realistic results.

1/19 Update:
Predictions continue to be underwhelming.  I have created a model where the output as percent change, and R^2 measurements have thus far been unsuccessful.  I will need to give the model more information.
