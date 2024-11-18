# Tesla Stock Price Prediction using Recurrent Neural Networks

Overview
This project involves building, training, and evaluating Recurrent Neural Network (RNN) models to predict Tesla's daily closing stock prices using time series data. The primary goal is to preprocess the data, engineer features, experiment with various RNN architectures and hyperparameters, and assess model performance.

Objectives
Analyze Tesla's historical stock prices and create a predictive model using RNNs.
Experiment with different hyperparameters such as:
Number of epochs (10, 50, 100, 200).
Learning rate adjustments (default: 0.01).
Number of RNN layers.
Evaluate the models’ ability to capture both long-term trends and short-term fluctuations in stock prices.

Workflow
Data Preprocessing:
Data sourced from Yahoo Finance.
Features engineered to include lagged values and rolling statistics.
Normalization using Min-Max scaling.
Model Training and Evaluation:
Built multiple RNN models using PyTorch with different configurations.
Assessed performance using training and validation loss metrics.
Results Analysis:
Visualized model predictions compared to actual stock prices.
Identified trade-offs between training duration, learning rate, and model accuracy.

Key Findings
Increasing the number of epochs improves model accuracy but risks overfitting if not properly managed.
The final model (200 epochs, learning rate of 0.01) achieved the best performance, balancing generalization and trend alignment.
Predictions closely followed actual prices, with improved handling of volatile periods.

Technologies Used
Python: Core programming language.
PyTorch: For building and training RNN models.
Yahoo Finance API: For fetching Tesla stock data.
Matplotlib: For visualizing predictions and trends.
