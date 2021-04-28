""" Question 4 .  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . Total: 20 marks
Write a program to score True-False tests. Correct answers get 1 point, wrong
answers -1 point and no answer (i.e., x) gets 0. The program rst reads in the
thirty correct answers to the test questions (each answer being T or F). It then
reads a series of answer sets { each of these is a student number (an integer)
followed by thirty answers, each of which is one of the characters T, F, or x.
x is used to report that no answer was given. The input is terminated by a
record beginning with the student number 999. The program should output
each student number followed by their score on the test.
Use functions as appropriate.
Sample input:
T F T F T F T F T F T F T F T F T F T F T F T F T F T F T F
100 T F T T F F T F T F T F T F T T T F F F x F T x T F T F x F """

answers = input()