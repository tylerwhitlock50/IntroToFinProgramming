###########################################
###############PART 1######################
###########################################
#1 Load the USD LIBOR data from FRED using the code 'USDONTD156N' and store it in a variable called usd_libor.
usd_libor = wb.DataReader('USDONTD156N', 'fred', start, end)

#2  Drop the NaN values from the usd_libor DataFrame.
usd_libor.dropna(inplace=True)

#3 Create a LinearRegression object called reg.
reg = linear_model.LinearRegression()

#4 Split the data into training and testing sets. Use 20% of the data for testing and set the random_state to 0.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

#5 Fit the model using the training data and make predictions on the testing data.
y_pred = reg.predict(X_test)

#6 Calculate the absolute difference between the 'EUR_LIBOR' and 'USD_LIBOR' columns and store it in a new column called 'COLUMN'.
df['COLUMN'] = abs(df['EUR_LIBOR'] - df['USD_LIBOR'])

#7 Rename the columns of the DataFrame to 'X1', 'X2', and 'Y'.
df.columns = ['X1', 'X2', 'Y']


###########################################
###############PART 2######################
###########################################

#8 Calculate the percent change of the 'column_name' column and store it in the same column.
df['column_name'] = df['column_name'].pct_change()

#9 Fit the model using the training data and make predictions on the testing data.
reg.fit(X_train, y_train)

#10 Calculate the R2 score of the model.
r2_score(y_test, y_pred)

#11 Calculate the percent change of the 'Y' column and store it in a new column called 'X'.
df['X'] = df['Y'].pct_change()

#12 Plot the 'X' column against the 'Y' column.
plt.scatter(df['X'], df['Y'])


#13 Get the intercept of the model.
reg.intercept_

#14 Get the coefficients of the model.
reg.coef_