## Week 5

## Cloud and API deployment

### In this project, I willl apply supervised learning (classification) algorithms on spam dataset to build spam classifier.

After obtaining cleaned dataset, i cleaned the data and make tfidf tvectorization to make the data ready for the modeling.

I used Naive Bayesian classifier as  it shows great performance on text classification tasks.


The performace of any classiifer is evaluated using confusion matrix, confusion matrix has many components as follow:

1) True Positive: Cases when we predicted spam and our prediction is true that means actual value is also spam.

2) True Negatives: Cases when we did not predict spam and our prediction is true that means actual value is not spam.

3) False Positives: Cases when we predicted spam and our prediction is false that means actual value is not spam.

4) False Negatives: Cases when we did not predict spam and our prediction is false that means actual value is spam.


In the case of spam classifier i want to build a classifier that detect all of the spam messages and it is okay to flag some ham messages as spam, so in this case i care the most about True positive(Tp) and False Positive(FP)

According to the definition of Recall and precision:
1) Precision : How many times are we correct when the predicted value is positive for a class. TP/(TP + FP)

2) Recall: How many times are we correct when the actual value is positive for a class. TP/(TP+FN)

So, we care the most about precision. We want classifier with the highest precision.