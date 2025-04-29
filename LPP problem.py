from pulp import LpProblem, LpVariable, LpMaximize
problem=LpProblem("Blending_Optimization",LpMaximize)
x1=LpVariable("X1",lowBound=0) # amount of ingredient A the Blend
x2=LpVariable("X2",lowBound=0)# amount of ingredient B the Blend
x3=LpVariable("X3",lowBound=0)# amount of ingredient C the Blend

# Define Objective function 
#Profit_per_unit

Profit_per_unit_A=10 #ingredient A
Profit_per_unit_B=15 #ingredient B
Profit_per_unit_C=8 #ingredient 

problem +=Profit_per_unit_A*x1+Profit_per_unit_B*x2+Profit_per_unit_C*x3

#Define Constraints
# Maximum Amount Of Ingredient
ingredient_A_constraint =20
ingredient_B_constraint =30
ingredient_C_constraint =25

salt_constraint =10 # maximum gram of salt allowed in the final product

problem+=x1 <=ingredient_A_constraint,"ingredient_A_constraint"
problem +=x2<=ingredient_B_constraint,"ingredient_B_constraint"
problem +=x3<=ingredient_C_constraint,"ingredient_C_constraint"

#total salt Constraint
salt_per_unit_A=2
salt_per_unit_B=3
salt_per_unit_C=1
problem += salt_per_unit_A*x1+salt_per_unit_B*x2+salt_per_unit_C*x3<=salt_constraint,"salt_constraint"

problem.solve()
# output
print("Optimal Blend :")
print(f"Ingredient A{x1.value()}units")
print(f"Ingredient B{x2.value()}units")
print(f"Ingredient C{x3.value()}units")

print(f" Total Profit:{Profit_per_unit_A*x1.value()+Profit_per_unit_B*x2.value()+Profit_per_unit_C*x3.value()}")
print(f"Total salt:{salt_per_unit_A*x1.value()+salt_per_unit_B*x2.value()+salt_per_unit_C*x3.value()}")