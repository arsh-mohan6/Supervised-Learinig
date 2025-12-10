#  Ordinary Least Squares (OLS) Linear Regression — From Scratch

This project demonstrates how to implement **Ordinary Least Squares (OLS)** linear regression **without using any external libraries** like NumPy or pandas.  
It’s a simple and educational example of how linear regression works under the hood.

---

##  Features
- Calculates **slope (m)** and **intercept (b)** manually  
- Uses basic Python operations only  
- Predicts `y` values for given `x` inputs  
- Clean and minimal code — great for learning regression fundamentals  

---

##  Formula

The best-fit line is given by:

\[
y = m x + b
\]

\[
x_mean = sum(x)/len(x)
\]


\[
y_mean = sum(y)/len(y)
\]


Where:

\[
m = \frac{\sum (x_i - x_mean)(y_i - y_mean)}{\sum (x_i - x_mean)^2}
\]


\[
b = y_mean - m*x_mean
\]

---

# Multiple Linear Regression

This project demonstrates **Multiple Linear Regression implemented manually in Python**, without using any external libraries like NumPy or scikit-learn.  
It helps understand the mathematical logic behind regression and how the coefficients are derived step by step.

---

## Formula Used

The regression model is:

\[
Y = B_0 + B_1X_1 + B_2X_2
\]

Where the coefficients are calculated using the following formulas:

\[
B_1 = \frac{ΣX_2^2ΣX_1Y - ΣX_1X_2ΣX_2Y}{ΣX_1^2ΣX_2^2 - (ΣX_1X_2)^2}
\]

\[
B_2 = \frac{ΣX_1^2ΣX_2Y - ΣX_1X_2ΣX_1Y}{ΣX_1^2ΣX_2^2 - (ΣX_1X_2)^2}
\]

\[
B_0 = \bar{Y} - B_1\bar{X_1} - B_2\bar{X_2}
\]

---

##  Concept Summary

- **Goal:** Predict the value of `Y` based on two independent variables, `X1` and `X2`.  
- **Method:** Uses the least squares approach to minimize the error between predicted and actual values.  
- **Output:** Regression coefficients `B0`, `B1`, `B2`, and the final regression equation.

---

##  Example

**Input:**
Enter the no of terms : 4
Enter X11: 2
Enter X21: 3
Enter Y1: 4
Enter X12: 4
Enter X22: 2
Enter Y2: 5
Enter X13: 3
Enter X23: 4
Enter Y3: 6
Enter X14: 5
Enter X24: 3
Enter Y4: 7
Enter the x1 : 3
Enter the x2 : 2

makefile
Copy code

##  Output:
Gradient B1 : 0.8
Gradient B2 : 0.2
Bias B0 : 2.0
Final Regression Equation : y = 2.0 + 0.8x1 + 0.2x2
Predicted Value of y at 3.0 and 2.0 is : 4.8000
---

## Key Takeaways

- Understand how multiple regression coefficients are calculated manually.  
- Learn the relationship between dependent and independent variables.  
- Practice applying statistical formulas programmatically.  

