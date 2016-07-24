# # """
# # Part 1: Discussion

# # 1. What are the three main design advantages that object orientation
# #    can provide? Explain each concept.

# """The three main design advantages are abstraction, encapsulation, and 
#     polymorphism. 

#     Abstraction in object orientation allows the programmer to 
#     hide details, such as the code a method uses internally. In other words and
#     for exmaple, a programmer can call a super or subclass method without having 
#     to read and fully understand how the method was created.

#     Encapsulation allows data to live close to its functionality. In other words,
#     classes sohuld only contain the most relevant and essential attributes and 
#     methods that are unique and specific to that class. For exmaple, if you were
#     to create a subclass Cat (of the superclass Animal), you should make sure
#     that all attributes and methods are specific and unique to a cat, the things
#     that make a cat a cat (i.e. meowing, hissing, etc.)

#     Polymorphism allows interchangeability of components. Polymorphism is the 
#     art of using the same method in different places in different ways. In other
#     words, polymorphism means creating a structure that can take or use many
#     forms of objects. For example, you may start with a superclass
#     (AbstractAnimal) that facilitates the creation of many forms of that 
#     superclass, such as Dog, Cat, Mouse, etc.""" 

# # 2. What is a class?

#     """For me, a class is a construct that allows a programmer to structure
#     their code in a logical, efficient manner by beginning with an abstract,
#     universal form which lends to all particulars. Classes are bundles
#     of code that let us create predictable objects with which we can work. If we
#     wanted to create a class for each animal, it's helpful to begin with the 
#     attributes that all animals share (AbstractAnimal) and pass those 
#     characteristics on to the all particular animals (i.e. Cat) and begin 
#     building the essential features of Cat on top of the general attributes of
#     all animals."""


# # 3. What is an instance attribute?

#     """An instance attribute is a characteristic of a singular example of a 
#     class. For example, if we had the subclass Cat, I could categorize my black
#     cat (her name is Ringo), as an instance of Cat. Ringo has unique
#     features, characteristics, and habits that make her unique from other cats.
#     Those features would be an example of instance attributes because her 
#     unique, odd behaviors (such as playing fetch with me) are not shared by all
#     animals or all cats."""

# # 4. What is a method?

#     """A method is like a function but specifically for a class. Many times we
#     want our classes to have conditional actions or give us back something that's
#     been calculated, for example. We can write functions specifically for our
#     classes."""

# # 5. What is an instance in object orientation?
    
#     """Instances are specific, particular examples of classes. Whiskey, my other
#     cat (she's tabby with white), is a particular example of a Cat (subclass), 
#     which is a type of Animal (superclass). You can think of instances as being 
#     copies of a class, but we can change each instance independently """

# # 6. How is a class attribute different than an instance attribute?
# #    Give an example of when you might use each.

#     """A class attribute is a broader, more general attribute that will have a 
#     wider scope of influence than an instance attribute. A class attribute 
#     assigned to Cat (a subclass) will be true and inherited for every instance
#     of every cat ever. An instance attribute, on the other hand, is specific to 
#     each example of the class. For example, you might assign the class attribute
#     of meowing to all Cats, but an instance attribute would make more sense for 
#     Alex, the cat who likes to take a bath. Most cats don't like water; therefore,
#     it wouldn't make sense to assign "likes taking a bath" to all Cats; rather,
#     we can make exceptions for unique instances with instance attributes. """


# # Parts 2 and 3:


class Student(object):
    def __init__ (self, first_name, last_name, address):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address


class Question(object):
    def __init__ (self, questions, answer):
        self.questions = questions
        self.answer = answer    

    def ask_and_evaluate(self):
        print self.questions 
        answer_given = raw_input(">>>")
        if answer_given == self.answer:
            return True
        else:
            return False


class Exam(object):
    def __init__ (self, name, questions):
        self.name = name
        self.questions = questions

    def add_question(self, question, answer):
        ask_and_answer = Question(question, answer)
        self.questions.append(ask_and_answer)

    def administer(self):
        score = 0

        for question in self.questions:
            if question.ask_and_evaluate() == True:
                score += 1

        return float(score) / len(self.questions)
# Part 4 

def take_test(student, exam):
    score = exam.administer()
    student.score = score
    print "You scored %d percent on the exam." % (100 * student.score)

def example():
    exam = Exam("Test 1", [])

    exam.add_question(
        'According to your reading, the main focus or unit of analysis for ' 
        'sociologists is:',
        "a group of people")

    exam.add_question(
        '"Social class background is a good predictor of achievement in school." ' 
        'In this statement, achievement in school is the:',
        "dependent variable")

    exam.add_question(
        'true or false: Sociologists who want to understand society from the ' 
        'macro-level should use a qualitative research design.',
        'false')

    exam.add_question(
        "true or false: Ethnocentrism is the belief that one's own culture is "
        'superior to that of others.',
        'true')

    student = Student(
        "Jessica",
        "Petersen",
        "555 Hackbright Way")

    take_test(student, exam)


# Part 5

class Quiz(Exam):
    def administer(self):
        return super(Quiz, self).administer()


def example2():
    quiz = Quiz("Quiz 1", [])

    quiz.add_question(
        'According to your reading, the main focus or unit of analysis for ' 
        'sociologists is:',
        "a group of people")

    quiz.add_question(
        '"Social class background is a good predictor of achievement in school." ' 
        'In this statement, achievement in school is the:',
        "dependent variable")

    quiz.add_question(
        'true or false: Sociologists who want to understand society from the ' 
        'macro-level should use a qualitative research design.',
        'false')

    quiz.add_question(
        "true or false: Ethnocentrism is the belief that one's own culture is "
        'superior to that of others.',
        'true')

    score = quiz.administer()
    if score >= 0.50:
        print "Good job! You passed the quiz!"
    else:
        print "You did not pass the quiz. It's time to hit the books!"



























