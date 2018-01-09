1/7/18 Update:

Created my first linear model.  This model ultimately has an R^2 of -0.87 for the MSFT data from Jan 3 2000 to Dec 8 2017.  This model has three parameters used to predict tomorrow's close: Today's close, Bollinger Differential and RSI.  This model was largely a failure because of the abysmal R^2.  

1/8/18 Update:
Created a Multi-Layer Perceptron Regression model.  The same three parameters from yesterday's model are being used.  I have found wild success with this model, partially because I have chosen to randomize some parameters for the model (number of hidden layers, activation function and solving method) and then automated running it until I find an acceptable R^2 on the training data.  R^2 seems to max out around 0.979 on the training data, and it often finds an R^2 of 0.999 on the testing data.  This is tremendous!  When I do end up with an R^2 on the testing data, I am able to predict the next day's close within 1.5%, usually undercutting the actual close.  

My next steps will be as follows:
1.  In it's current form, the automation of the network can break when it doesn't converge within the maximum number of iterations.  I will want to change the network so that it will adapt to this glitch and simply ignores it, and continues on the automation.   *UPDATE:* This turned out to be super easy.

2.  I will want to get up-to-date information on EVERY company on the S&P 500 and run this network on all of them.  I will then keep track of my accuracy regarding top gainers and top losers.

3.  I will, of course, want to add more parameters.  There are plenty of technical indicators out there, and I'm currently using two.  I can do better.
