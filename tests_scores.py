"""
display user message
while True
    get score
    if score is from 0 to 100
        add score to score total
        add 1 to the number of scores
    else if score is 999
        end Loop
    else 
        print KeyError
calculate average score
display the results
"""

#/usr/bin/env python3
#Display a welcome
def main():
    print("The Test Scores Program")
    print()
    print("Enter 999 to end input")
    print("===========================")

    #initialize
    counter = 0
    score_total = 0
    test_score = 0

    while True:
        test_score = float(input("Enter test score: "))
        if test_score >= 0 and test_score <= 100:
            score_total += test_score
            counter += 1
        elif test_score == 999:
            break
        else:
            print("Test score must be from 0 to 100" + "Score discarded.")
    average_score = round(score_total/counter, 2)

    #format and display
    print("========================================")
    print(f"Total Score: " + str(score_total) + "\nAverage Score: " + str(average_score))

if __name__ == "__main__":
    main()
