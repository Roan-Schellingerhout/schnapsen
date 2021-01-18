import sys
from kb import KB, Boolean, Integer, Constant

# Define our propositional symbols
# J1 is true if the card with index 1 is a jack, etc
# You need to initialise all variables that you need for you strategies and game knowledge.
# Add those variables here.. The following list is complete for the Play Jack strategy.
J0 = Boolean('j0')
J1 = Boolean('j1')
J2 = Boolean('j2')
J3 = Boolean('j3')
J4 = Boolean('j4')
J5 = Boolean('j5')
J6 = Boolean('j6')
J7 = Boolean('j7')
J8 = Boolean('j8')
J9 = Boolean('j9')
J10 = Boolean('j10')
J11 = Boolean('j11')
J12 = Boolean('j12')
J13 = Boolean('j13')
J14 = Boolean('j14')
J15 = Boolean('j15')
J16 = Boolean('j16')
J17 = Boolean('j17')
J18 = Boolean('j18')
J19 = Boolean('j19')
PJ0 = Boolean('pj0')
PJ1 = Boolean('pj1')
PJ2 = Boolean('pj2')
PJ3 = Boolean('pj3')
PJ4 = Boolean('pj4')
PJ5 = Boolean('pj5')
PJ6 = Boolean('pj6')
PJ7 = Boolean('pj7')
PJ8 = Boolean('pj8')
PJ9 = Boolean('pj9')
PJ10 = Boolean('pj10')
PJ11 = Boolean('pj11')
PJ12 = Boolean('pj12')
PJ13 = Boolean('pj13')
PJ14 = Boolean('pj14')
PJ15 = Boolean('pj15')
PJ16 = Boolean('pj16')
PJ17 = Boolean('pj17')
PJ18 = Boolean('pj18')
PJ19 = Boolean('pj19')

Q0 = Boolean('q0')
Q1 = Boolean('q1')
Q2 = Boolean('q2')
Q3 = Boolean('q3')
Q4 = Boolean('q4')
Q5 = Boolean('q5')
Q6 = Boolean('q6')
Q7 = Boolean('q7')
Q8 = Boolean('q8')
Q9 = Boolean('q9')
Q10 = Boolean('q10')
Q11 = Boolean('q11')
Q12 = Boolean('q12')
Q13 = Boolean('q13')
Q14 = Boolean('q14')
Q15 = Boolean('q15')
Q16 = Boolean('q16')
Q17 = Boolean('q17')
Q18 = Boolean('q18')
Q19 = Boolean('q19')

PQ0 = Boolean('pq0')
PQ1 = Boolean('pq1')
PQ2 = Boolean('pq2')
PQ3 = Boolean('pq3')
PQ4 = Boolean('pq4')
PQ5 = Boolean('pq5')
PQ6 = Boolean('pq6')
PQ7 = Boolean('pq7')
PQ8 = Boolean('pq8')
PQ9 = Boolean('pq9')
PQ10 = Boolean('pq10')
PQ11 = Boolean('pq11')
PQ12 = Boolean('pq12')
PQ13 = Boolean('pq13')
PQ14 = Boolean('pq14')
PQ15 = Boolean('pq15')
PQ16 = Boolean('pq16')
PQ17 = Boolean('pq17')
PQ18 = Boolean('pq18')
PQ19 = Boolean('pq19')


K2 = Boolean('k2')
K7 = Boolean('k7')
K12 = Boolean('k12')
K17 = Boolean('k17')

PK2 = Boolean('pk2')
PK7 = Boolean('pk7')
PK12 = Boolean('pk12')
PK17 = Boolean('pk17')

# Create a new knowledge base
kb = KB()

# GENERAL INFORMATION ABOUT THE CARDS
# This adds information which cards are Jacks
kb.add_clause(J4)
kb.add_clause(J9)
kb.add_clause(J14)
kb.add_clause(J19)
# Add here whatever is needed for your strategy.
kb.add_clause(Q3)
kb.add_clause(Q8)
kb.add_clause(Q13)
kb.add_clause(Q18)

kb.add_clause(K2)
kb.add_clause(K7)
kb.add_clause(K12)
kb.add_clause(K17)


# DEFINITION OF THE STRATEGY
# Add clauses (This list is sufficient for this strategy)
# PJ is the strategy to play jacks first, so all we need to model is all x PJ(x) <-> J(x),
# In other words that the PJ strategy should play a card when it is a jack
kb.add_clause(~J4, PJ4)
kb.add_clause(~J9, PJ9)
kb.add_clause(~J14, PJ14)
kb.add_clause(~J19, PJ19)
kb.add_clause(~PJ4, J4)
kb.add_clause(~PJ9, J9)
kb.add_clause(~PJ14, J14)
kb.add_clause(~PJ19, J19)
# Add here other strategies

# queens
kb.add_clause(~Q3, PQ3)
kb.add_clause(~Q8, PQ8)
kb.add_clause(~Q13, PQ13)
kb.add_clause(~Q18, PQ18)
kb.add_clause(~PQ3, Q3)
kb.add_clause(~PQ8, Q8)
kb.add_clause(~PQ13, Q13)
kb.add_clause(~PQ18, Q18)

# kings
kb.add_clause(~K2, PK2)
kb.add_clause(~K7, PK7)
kb.add_clause(~K12, PK12)
kb.add_clause(~K17, PK17)
kb.add_clause(~PK2, K2)
kb.add_clause(~PK7, K7)
kb.add_clause(~PK12, K12)
kb.add_clause(~PK17, K17)

kb.add_clause(~PQ4)
# print all models of the knowledge base
for model in kb.models():
    print(model)

# print out whether the KB is satisfiable (if there are no models, it is not satisfiable)
print(kb.satisfiable())
