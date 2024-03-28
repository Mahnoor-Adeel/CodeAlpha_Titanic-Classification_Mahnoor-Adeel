Titanic Classification Problem
<h2 align='center'>Titanic Passenger Survival Prediction</h2>
<p align = 'center'> This program determines if a person survives based on multiple characteristics such as age, gender, passenger class, and etc. This was part of Data Science Intership with CodeAlpha.</p> <hr>
<h3>Project Workflow :bookmark_tabs: </h3>

**1. Importing Data:** The dataset used for this problem contained infromation about a large nuber of patients and if they survived or not. The source of this dataset is https://www.kaggle.com/competitions/titanic/data?select=train.csv. 

**2. Data Cleaning:** In this part, missing values were handled in the dataset. The missing values in a particular field were either replaced by the mean value, if the variable was quantitaive, or the mode, if the varaible was categorical. 

**3. Data Analysis:** In this part, all the statistical metrics for instance; mean, medians, and quartiles were studied. Furthermore, rate of survival was calculated for males and females respectively.

**4. Data Visualisation:** In this part, we visualized survival rates in different gender and passenger classes witth the help of Bar Graphs and Pie Charts.

**5. Encoding Categorical Variables:** In this part, caterogical variables like gender and embarked were mapped to quatitaive variables so that they could be used for training a regression model. Binary encoding was used for categorical variables.

**6. Preparing Dataset for Model Training:** Irrelevant varaibles like name and id and more survived were eliminated from the input data as they do not determine the survival of a person.

**7. Splitting Datset for Training and Testing:** Dataset was splitted into two parts for, training and testing, randomly.

**8. Logistic Regression Model Training:** Logistic Regression Model was used, as the output variable was a binary variable. Logitic Regression method from Python's Scikit-Learn library was used in this part.

**9. Checking Accuracy of the Model:** Acuracy of the model was checked using accuracy socre metric from Python's Scikit-Learn library.

**10. Deploying Model:** The model was deployed in a pickle file so that it could be used for predicting survival for a perosn after taking input of his characteristics.

