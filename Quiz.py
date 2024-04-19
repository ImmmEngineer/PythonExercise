class Question:
    def __init__(self,text,choices,answer) -> None:
        self.text = text
        self.choices = choices
        self.answer = answer
    def checkAnswer(self,answer):
        return self.answer == answer

class Quiz:
    def __init__(self, questions) -> None:
        self.questions = questions
        self.score = 0
        self.questionIndex = 0
    
    def getQuestion(self):
        return self.questions[self.questionIndex]
    
    def displayQuestion(self):
        question = self.getQuestion()
        print(f'Soru {self.questionIndex} : {question.text}')

        for q in question.choices:
            print('-' + q)
        
        answer = input('cevap : ')
        self.guess(answer)
        self.loadQuestion()

    def guess(self,answer):
        question = self.getQuestion()

        if question.checkAnswer(answer):
            self.score += 1
        self.questionIndex += 1 
        

    def loadQuestion(self):
        if len(self.questions) == self.questionIndex:
            self.showScore() 
        else:
            self.displayProgress()
            self.displayQuestion()

    def showScore(self):
        print('score : ', self.score)

    def displayProgress(self):
        totalQuestion = len(self.questions)
        questionNumber = self.questionIndex + 1

        if questionNumber > totalQuestion:
            print('quiz bitti')
        else:
            print(f'Question{questionNumber} of {totalQuestion}'.center(100,'*'))
        


q1 = Question('Aşağidakilerden hangisi orta seviyeli dillerden değildir?',['c','c++','java','c#','python'],'python')
q2 = Question('Python hangi tür bir programlama dilidir?',['derlenmiş','yorumlanmis','karma','isaretci tabanli'],'karma')
q3 = Question('Aşağidakilerden hangisi orta seviyeli dillerdendir?',['c','javascript','ruby','swift','python'],'c')
q4 = Question('Aşağidakilerden hangisi yüksek seviyeli dildir?',['c','c++','java','c#','python'],'python')

questions = [q1,q2,q3,q4]

quiz = Quiz(questions)
quiz.loadQuestion()

