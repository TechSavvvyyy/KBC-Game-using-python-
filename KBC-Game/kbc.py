from questions import QUESTIONS
def isAnswerCorrect(question, answer):
    return True if question["answer"]==answer else False      #remove this
def lifeLine(ques):
    return ques['option1'],ques['option'+str(ques['answer'])]
def kbc():
  print("\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t WELCOME\n")
  noq=0
  moneywon=0
  lifeline_use=0
  while (noq<=15):
    noq+=1
    print("\tQuestion ", noq," : " ,QUESTIONS[noq-1]["name"]," ")
    print(f'\t\tOptions:')
    print(f'\t\t\tOption 1: {QUESTIONS[noq-1]["option1"]}')
    print(f'\t\t\tOption 2: {QUESTIONS[noq-1]["option2"]}')
    print(f'\t\t\tOption 3: {QUESTIONS[noq-1]["option3"]}')
    print(f'\t\t\tOption 4: {QUESTIONS[noq-1]["option4"]}')
    ans = input('Your choice ( 1-4 ) : ')
    if ans=="lifeline" and lifeline_use==0:
        op1,op2=lifeLine(QUESTIONS[noq-1])
        print(f'\t\tOptions:')
        print(f'\t\t\tOption 1: {op1}')
        c=QUESTIONS[noq-1]['answer']
        print(f'\t\t\tOption {c} : {op2}')
        ans = input('Your choice ( 1-2 ) : ')
        lifeline_use =1
    if ans == "lifeline" and lifeline_use == 1:
        print("\t\t\t\t\tSorry , you can use lifeline only one time")
        noq-=1
        ans=0
    # check for the input validations
    if ans=="quit":
        break;
    a=isAnswerCorrect(QUESTIONS[noq - 1], int(ans))
    if a and ans!=0:
        moneywon+=QUESTIONS[noq-1]['money']
        # print the total money won.
        print("\t\t\t\t\tTotal money won :",moneywon)
        # See if the user has crossed a level, print that if yes
        if (noq - 5 == 0):
            print("LEVEL INCREASED,", "You are Now on level 1")
        elif (noq - 11 == 0):
            print("\t\t\t\t\tLEVEL INCREASED", "You are Now on level 2")
        print('\t\t\t\t\tCorrect !\n')
    elif not a:
        if noq<=5:
            moneywon=0
        elif noq<=11:
            moneywon=10,000
        else:
            moneywon=320000
        print("\t\t\t\t\tIncorrect ! \n\t\t\t\t\tCorect answer is ",QUESTIONS[noq-1]["answer"])
        break;

  print("\t\t\t\t\tTotal money won :",moneywon)
kbc()
