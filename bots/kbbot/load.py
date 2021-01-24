from .kb import KB, Boolean, Integer

# Initialise all variables that you need for you strategies and game knowledge.
# Add those variables here.. The following list is complete for the Play Jack strategy.
J4 = Boolean('j4')
J9 = Boolean('j9')
J14 = Boolean('j14')
J19 = Boolean('j19')

Q3 = Boolean('q3')
Q8 = Boolean('q8')
Q13 = Boolean('q13')
Q18 = Boolean('q18')

K2 = Boolean('k2')
K7 = Boolean('k7')
K12 = Boolean('k12')
K17 = Boolean('k17')

T1 = Boolean('t1')
T6 = Boolean('t6')
T11 = Boolean('t11')
T16 = Boolean('t16')

A0 = Boolean('a0')
A5 = Boolean('a5')
A10 = Boolean('a10')
A15 = Boolean('a15')

P0 = Boolean('p0')
P1 = Boolean('p1')
P2 = Boolean('p2')
P3 = Boolean('p3')
P4 = Boolean('p4')
P5 = Boolean('p5')
P6 = Boolean('p6')
P7 = Boolean('p7')
P8 = Boolean('p8')
P9 = Boolean('p9')
P10 = Boolean('p10')
P11 = Boolean('p11')
P12 = Boolean('p12')
P13 = Boolean('p13')
P14 = Boolean('p14')
P15 = Boolean('p15')
P16 = Boolean('p16')
P17 = Boolean('p17')
P18 = Boolean('p18')
P19 = Boolean('p19')

def jack_information(kb):
    kb.add_clause(J4)
    kb.add_clause(J9)
    kb.add_clause(J14)
    kb.add_clause(J19)

def jack_knowledge(kb):
    kb.add_clause(~J4, P4)
    kb.add_clause(~J9, P9)
    kb.add_clause(~J14, P14)
    kb.add_clause(~J19, P19)

    kb.add_clause(~P4, J4)
    kb.add_clause(~P9, J9)
    kb.add_clause(~P14, J14)
    kb.add_clause(~P19, J19)

def queen_information(kb):
    kb.add_clause(Q3)
    kb.add_clause(Q8)
    kb.add_clause(Q13)
    kb.add_clause(Q18)

def queen_knowledge(kb):
    kb.add_clause(~Q3, P3)
    kb.add_clause(~Q8, P8)
    kb.add_clause(~Q13, P13)
    kb.add_clause(~Q18, P18)

    kb.add_clause(~P3, Q3)
    kb.add_clause(~P8, Q8)
    kb.add_clause(~P13, Q13)
    kb.add_clause(~P18, Q18)

def king_information(kb):
    kb.add_clause(K2)
    kb.add_clause(K7)
    kb.add_clause(K12)
    kb.add_clause(K17)

def king_knowledge(kb):
    kb.add_clause(~K2, P2)
    kb.add_clause(~K7, P7)
    kb.add_clause(~K12, P12)
    kb.add_clause(~K17, P17)

    kb.add_clause(~P2, K2)
    kb.add_clause(~P9, K7)
    kb.add_clause(~P12, K12)
    kb.add_clause(~P17, K17)

def ten_information(kb):
    kb.add_clause(T1)
    kb.add_clause(T6)
    kb.add_clause(T11)
    kb.add_clause(T16)

def ten_knowledge(kb):
    kb.add_clause(~T1, P1)
    kb.add_clause(~T6, P6)
    kb.add_clause(~T11, P11)
    kb.add_clause(~T16, P16)

    kb.add_clause(~P1, T1)
    kb.add_clause(~P6, T6)
    kb.add_clause(~P11, T11)
    kb.add_clause(~P16, T16)

def ace_information(kb):
    kb.add_clause(A0)
    kb.add_clause(A5)
    kb.add_clause(A10)
    kb.add_clause(A15)

def ace_knowledge(kb):
    kb.add_clause(~A0, P0)
    kb.add_clause(~A5, P5)
    kb.add_clause(~A10, P10)
    kb.add_clause(~A15, P15)

    kb.add_clause(~P0, A0)
    kb.add_clause(~P5, A5)
    kb.add_clause(~P10, A10)
    kb.add_clause(~P15, A15)

def cheap_information(kb):
    kb.add_clause(J4)
    kb.add_clause(J9)
    kb.add_clause(J14)
    kb.add_clause(J19)

    kb.add_clause(Q3)
    kb.add_clause(Q8)
    kb.add_clause(Q13)
    kb.add_clause(Q18)

    kb.add_clause(K2)
    kb.add_clause(K7)
    kb.add_clause(K12)
    kb.add_clause(K17)

def cheap_knowledge(kb):
    kb.add_clause(~J4, P4)
    kb.add_clause(~J9, P9)
    kb.add_clause(~J14, P14)
    kb.add_clause(~J19, P19)

    kb.add_clause(~P4, J4)
    kb.add_clause(~P9, J9)
    kb.add_clause(~P14, J14)
    kb.add_clause(~P19, J19)

    kb.add_clause(~Q3, P3)
    kb.add_clause(~Q8, P8)
    kb.add_clause(~Q13, P13)
    kb.add_clause(~Q18, P18)

    kb.add_clause(~P3, Q3)
    kb.add_clause(~P8, Q8)
    kb.add_clause(~P13, Q13)
    kb.add_clause(~P18, Q18)

    kb.add_clause(~K2, P2)
    kb.add_clause(~K7, P7)
    kb.add_clause(~K12, P12)
    kb.add_clause(~K17, P17)

    kb.add_clause(~P2, K2)
    kb.add_clause(~P9, K7)
    kb.add_clause(~P12, K12)
    kb.add_clause(~P17, K17)
