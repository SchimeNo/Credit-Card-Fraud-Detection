import scipy, matplotlib, sklearn, numpy
import pandas as pd
import pandas_profiling


#Load dataset
data = pd.read_csv('./datasets/creditcard.csv')


#### Descriptive statistics #####

data.columns #column names
#report = pandas_profiling.ProfileReport(data) #panda's report, may take a while to load
# report.to_file("report.html") #this will generate a file with a summary of the data


# b) Data visualizations

# 3. Prepare Data
# a) Data Cleaning
# b) Feature Selection
# c) Data Transforms

# 4. Evaluate Algorithms
# a) Split-out validation dataset
# b) Test options and evaluation metric
# c) Spot Check Algorithms
# d) Compare Algorithms

# 5. Improve Accuracy
# a) Algorithm Tuning
# b) Ensembles

# 6. Finalize Model
# a) Predictions on validation dataset
# b) Create standalone model on entire training dataset
# c) Save model for later use