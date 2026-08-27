# Model Card

## Model Details
This model is a Random Forest classifier developed to predict whether or not an individual's annual income is greater than $50,000 based on demographic and employment-related information from the Census Income dataset. The model was implemented using scikit-learn and trained with a fixed random state of 42 to support reproducible results.

## Intended Use
The model is intended to predict whether or not an individual's annual income is greater than $50,000 based on demographic and employment-related variables contained in the Census Income dataset. The model was developed for the machine learning community to practice model training, evaluation, and deployment. It is not intended to make high-stakes decisions about individuals, such as decisions involving employment, lending, insurance, or eligibility for services.

## Training Data
The model was trained using the provided census.csv dataset, which contains 
32,561 records and 15 columns drawn from the 1994 U.S. Census data. The dataset includes demographics such as age, workclass, education, occupation, marital status, race, sex, hours worked per week, and native country. The target variable is salary, which indicates whether or not an individual's annual income exceeds the $50,000 threshold.
The dataset was split into training and testing sets using an 80/20 split with a random state of 42. Categorical features in the training data were transformed using one-hot encoding, and the salary labels were converted to binary values using a label binarizer.

## Evaluation Data
The model was evaluated using the 20% test portion of the provided census.csv dataset created by the train-test split. The test data was not used to train the model. Categorical features in the evaluation data were transformed using the one-hot encoder fitted on the training data, and the salary labels were transformed using the previously fitted label binarizer. This allowed the model's performance to be evaluated on data that was not used during training.

## Metrics
The model was evaluated using precision, recall, and F1 score. Precision measures the proportion of positive predictions that were correct, while recall measures the proportion of actual positive cases that the model correctly identified. The F1 score provides a balance between precision and recall.
On the 20% of the data that was reserved for testing, the model achieved a precision of 0.7419, a recall of 0.6384, and an F1 score of 0.6863. These results indicate that the model was more precise when predicting individuals earning more than $50,000 than it was at identifying all individuals who actually belonged to that class.
Performance was also evaluated across individual values of the categorical features. These slice metrics are recorded in slice_output.txt and demonstrated that model performance varies across different subgroups in the dataset.

## Ethical Considerations
The dataset contains sensitive demographic attributes, including race and sex, that may be associated with historical, societal, and institutional inequalities. As a result, the model may learn patterns or biases present in the underlying data. On the other hand, the dataset does not include direct identifiers such as names or contact information that would readily identify specific individuals. The slice evaluation also shows that model performance is not consistent across all demographic and employment-related groups.
Predictions from this model should not be used to make high-stakes decisions about individuals, including decisions related to employment, lending, insurance, or access to services. Additional reviews of bias would be necessary before considering the model for a real-world application involving people.

## Caveats and Recommendations
The model was trained on historical Census data (specifically from 1994) and likely does not accurately represent current populations, employment patterns, or income distributions. Model performance also varies across categorical slices, and results for groups with very small sample sizes should be interpreted cautiously because their metrics may not be reliable.
Before using the model in a real-world application, it would be beneficial to train and evaluate it on more recent and representative data, perform additional bias analyses, and investigate methods for improving performance across underrepresented groups. Additional model and hyperparameter comparisons could also be performed to determine whether another approach provides better predictive performance. The model should not be used for high-stakes decisions without substantially more validation and evaluation.
