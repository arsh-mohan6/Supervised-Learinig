X1 = [3,4,5,6,2]
X2 = [8,5,7,3,1]
Y =[-3.7,3.5,2.5,11.5,5.7]
X1_ = sum(X1)/len(X1)
X2_ = sum(X2)/len(X2)
Y_ = sum(Y)/len(Y)
X1_sum = 0
X2_sum = 0
X1_X2 = 0

X1_Y =0
X2_Y =0
for i in range(len(X1)):
    X1_sum = X1_sum+X1[i]**2
    X2_sum = X2_sum+X2[i]**2
    X1_X2 = X1_X2 + X1[i]*X2[i]
    X1_Y = X1_Y + X1[i]*Y[i]
    X2_Y = X2_Y + X2[i]*Y[i]
    

print(X1_, X2_, Y_, X1_sum ,X2_sum ,X1_X2 ,X1_Y ,X2_Y)

B1 = (X2_sum*X1_Y - X1_X2*X2_Y)/(X1_sum*X2_sum - (X1_X2)**2)

B2 = (X1_sum*X2_Y - X1_X2*X1_Y)/(X1_sum*X2_sum - (X1_X2)**2)

B0 = Y_ - B1*X1_- B2*X2_

print(B0,B1,B2)

y = B0 + B1*3+B2*2

print(f"Predicted Value of y at 3 and 2 is : {y:.4f}")
