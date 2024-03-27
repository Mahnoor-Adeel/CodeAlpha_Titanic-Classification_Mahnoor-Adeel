import pickle as pkl
import numpy as np
with open('Logistic_Regression_model.pkl', 'rb') as file:
    model_file = pkl.load(file)

def pred_output(user_input): 
    model_input = np.array(user_input).reshape(-1, 8)
    output = model_file.predict(model_input)
    return output[0]
def main(): 
    #Input Variables 
    name = input("Enter your name: ")

    id = input("Enter your id: ")

    ticket_num = input("Enter your ticket number")

    fare = input("Enter your ticket fare: ")

    cabin = input("Enter cabin number: ")
    
    p_class = input("Enter passenger class(1/2/3): ")

    gender = input("Enter you gender(M/F): ")
    if gender == "M":
        gender = 0
    elif gender == "F":
        gender = 1

    age = input("Enter your age: ")

    sibs = input("Enter number of siblings: ")

    par = input("Enter your parch: ")

    emb = input("Enter your Port of Embarked: (C=Cherbourg | Q=Queentown | S=Southampton) ")
    c, q = 0, 0
    if emb == "C":
        c=1
    elif emb == "Q":
        q=1

    #Predict result
    user_input = [p_class, gender, age, sibs, par, fare, c, q]
    user_input = list(map(float, user_input))
    prediction = pred_output(user_input)

    #Display prediction
    if prediction == 0: 
        prediction = "Oops! Not Survived."
    elif prediction == 1: 
        prediction = "Yay! Survived."


if __name__ == '__main__': 
    main()