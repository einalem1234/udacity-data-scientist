# Question 2
List three of the supervised learning models above that are appropriate for this problem that you will test on the census data. For each model chosen

- Describe one real-world application in industry where the model can be applied. 
- What are the strengths of the model; when does it perform well?
- What are the weaknesses of the model; when does it perform poorly?
- What makes this model a good candidate for the problem, given what you know about the data?

# Research for Question 2
## Model 1 - Gradient Boosting Classifier
Boosting classifiers use weak learners which performe slightly better than a random choice. these weak learners are then combined to get better.

One real-world example for a gradient boosting classifier is the search engine of Yahoo. The search engine uses it to distinguish between relevant and irrelevant URLs [Reference](http://www.kdd.org/kdd2016/papers/files/adf0361-yinA.pdf). Another example are anomaly detection in unbalanced data sets as DNA sequences [Reference](https://medium.com/@aravanshad/gradient-boosting-versus-random-forest-cfa3fa8f0d80).


The idea of boosting came out of the idea of whether a weak learner can be modified to become better.
A weak hypothesis or weak learner is defined as one whose performance is at least slightly better than random chance. [refernce](https://machinelearningmastery.com/gentle-introduction-gradient-boosting-algorithm-machine-learning/)
Decision trees are used as the weak learner in gradient boosting. [refernce](https://machinelearningmastery.com/gentle-introduction-gradient-boosting-algorithm-machine-learning/)
Real-world application:

A gradient boosting classifier is used in the search engine of Yahoo. It helps to reduce the number of bad URLS/websites in the search results. It is implemented as a binary classification to distinguish between relevant and irrelevant URLs for a given search request.
[Reference](http://www.kdd.org/kdd2016/papers/files/adf0361-yinA.pdf)
A great application of GBM is anomaly detection in supervised learning settings where data is often highly unbalanced such as DNA sequences, credit card transactions or cyber security.[Reference](https://medium.com/@aravanshad/gradient-boosting-versus-random-forest-cfa3fa8f0d80)

Strength of the model:
TODO
The logic behind gradient boosting is simple, (can be understood intuitively, without using mathematical notation). [Reference](https://medium.com/mlreview/gradient-boosting-from-scratch-1e317ae4587d)
In summary, 
• We first model data with simple models and analyze data for errors. 
• These errors signify data points that are difficult to fit by a simple model. 
• Then for later models, we particularly focus on those hard to fit data to get them right. 
• In the end, we combine all the predictors by giving some weights to each predictor.[Reference](https://medium.com/mlreview/gradient-boosting-from-scratch-1e317ae4587d)

GBTs build trees one at a time, where each new tree helps to correct errors made by previously trained tree. With each tree added, the model becomes even more expressive. There are typically three parameters - number of trees, depth of trees and learning rate, and the each tree built is generally shallow.

GBDT training generally takes longer because of the fact that trees are built sequentially. However benchmark results have shown GBDT are better learners than Random Forests. [Reference](https://www.quora.com/What-are-the-advantages-disadvantages-of-using-Gradient-Boosting-over-Random-Forests)

Weaknesses of the model:
Gradient boosting is a greedy algorithm and can overfit a training dataset quickly. [refernce](https://machinelearningmastery.com/gentle-introduction-gradient-boosting-algorithm-machine-learning/)
prone to overfitting, slow learning [Reference](https://www.quora.com/What-are-the-advantages-disadvantages-of-using-Gradient-Boosting-over-Random-Forests)
Gradient Boosted Methods generally have 3 parameters to train shrinkage parameter, depth of tree, number of trees. Now each of these parameters should be tuned to get a good fit. And you cannot just take maximum value of ntree in this case as GBM can overfit fit higher number of trees. [Reference](https://www.quora.com/What-are-the-advantages-disadvantages-of-using-Gradient-Boosting-over-Random-Forests)
    GBMs are more sensitive to overfitting if the data is noisy.
    Training generally takes longer because of the fact that trees are built sequentially.
    GBMs are harder to tune than RF. There are typically three parameters: number of trees, depth of trees and learning rate, and the each tree built is generally shallow. [Reference](https://medium.com/@aravanshad/gradient-boosting-versus-random-forest-cfa3fa8f0d80)
TODO

Good kandidate for the problem:
TODO
#### Model 2 - Decision Trees
mentioned in the paper (where the data was provided)
Random Forests train each tree independently, using a random sample of the data. This randomness helps to make the model more robust than a single decision tree, and less likely to overfit on the training data. There are typically two parameters in RF - number of trees and no. of features to be selected at each node. [Reference](https://www.quora.com/What-are-the-advantages-disadvantages-of-using-Gradient-Boosting-over-Random-Forests)
Real-world application:
TODO
By using the answer wizard, people can find out how ATS Trust can help with an oil tank problem, see possible outcomes for repair and get the answers they need to proceed with their project. Educators seeking to teach the value of decision trees may benefit from applying a similar format used in ATS Trust’s Answer Wizard. [Reference](https://www.funderstanding.com/blog/real-life-application-decision-trees/)
More recently, decision tree methodology has become popular in medical research. An example of the medical use of decision trees is in the diagnosis of a medical condition from the pattern of symptoms, in which the classes defined by the decision tree could either be different clinical subtypes or a condition, or patients with a condition who should receive different therapies. [Reference](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4466856/)

Strength of the model:
TODO
Advantage 2: Decision trees require relatively little effort from users for data preparation. can handle missing values, nogt sensitive to outliers, no variable transformations are required [Reference](http://www.simafore.com/blog/bid/62333/4-key-advantages-of-using-decision-trees-for-predictive-analytics)
Nonlinear relationships between parameters do not affect tree performance. However, decision trees do not require any assumptions of linearity in the data. Thus, we can use them in scenarios where we know the parameters are nonlinearly related. [Reference](http://www.simafore.com/blog/bid/62333/4-key-advantages-of-using-decision-trees-for-predictive-analytics)
The best feature of using trees for analytics - easy to interpret and explain to executives! [Reference](http://www.simafore.com/blog/bid/62333/4-key-advantages-of-using-decision-trees-for-predictive-analytics)
Decision trees are "white boxes" in the sense that the acquired knowledge can be expressed in a readable form [Reference](https://www.researchgate.net/post/What_are_pros_and_cons_of_decision_tree_versus_other_classifier_as_KNN_SVM_NN)

Weaknesses of the model:
TODO
Some of these are related to the problem of multicollinearity: when two variables both explain the same thing, a decision tree will greedily choose the best one, whereas many other methods will use them both. One disadvantage is that all terms are assumed to interact. That is, you can't have two explanatory variables that behave independently. Every variable in the tree is forced to interact with every variable further up the tree. This is extremely inefficient if there are variables that have no or weak interactions. [Reference](https://stats.stackexchange.com/questions/1292/what-is-the-weak-side-of-decision-trees)
These advantages need to be tempered with one key disadvantage of decision trees: without proper pruning or limiting tree growth, they tend to overfit the training data, making them somewhat poor predictors. [Reference](http://www.simafore.com/blog/bid/62333/4-key-advantages-of-using-decision-trees-for-predictive-analytics)

Good kandidate for the problem:
TODO

#### Model 3 - Logistic Regression
Real-world application:
TODO
Marketing: A marketing consultant wants to predict if the subsidiary of his company will make profit, loss or just break even depending on the characteristic of the subsidiary operations.
Human Resources: The HR manager of a company wants to predict the absenteeism pattern of his employees based on their individual characteristic.
Finance: A bank wants to predict if his customers would default based on the previous transactions and history.[Reference](https://www.analyticsinsight.net/introduction-to-logistic-regression/)

Strength of the model:
TODO

Weaknesses of the model:
TODO

Good kandidate for the problem:
TODO
