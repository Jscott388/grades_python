def grade():
    for count in range(0,11):
        data = raw_input("What is your score?")
        score = int(data)
        if 60 <= score <= 69:
            print "Scores:", score , ": Your grade is D"
        elif 70 <= score <= 79:
            print "Scores:", score , ": Your grade is C"
        elif 80 <= score <= 89: # Sweet
            print "Scores:", score , ": Your grade is B"
        elif 90 <= score <= 100:
            print "Scores:", score , ": Your grade is A"
        elif score > 100:
            print "You scored over 100! Great job"
        else:
            print "You have failed"

    print "End of program, Bye!"

grade()
# looks pretty good Joshua.  It's nice that python allows you to do combined expressions like in your elif statements.
