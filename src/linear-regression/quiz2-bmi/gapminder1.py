# TODO: Add import statements
from pandas import read_csv
from sklearn.linear_model import LinearRegression

# Assign the dataframe to this variable.
# TODO: Load the data
bmi_life_data = read_csv("bmi_and_life_expectancy.csv", header=0)
#print(bmi_life_data.loc['Country'])
#print(list(bmi_life_data.columns.values['Country']))
x_values = bmi_life_data[['BMI']]
y_values = bmi_life_data[['Life expectancy']]
print(y_values)

# Make and fit the linear regression model
#TODO: Fit the model and Assign it to bmi_life_model
bmi_life_model = LinearRegression()
bmi_life_model.fit(x_values, y_values)


# Make a prediction using the model
# TODO: Predict life expectancy for a BMI value of 21.07931

laos_life_exp = bmi_life_model.predict(21.07931)
