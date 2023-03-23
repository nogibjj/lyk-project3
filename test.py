import json

import random
cpp_questions_and_answers = {
    "What is the difference between a reference and a pointer in C++?": "A reference is an alias to an already existing variable, while a pointer is a variable that stores the memory address of another variable.",
    "What is a virtual function in C++?": "A virtual function is a member function in a base class that can be overridden in a derived class.",
    "What is the difference between an abstract class and an interface in C++?": "An abstract class can have member variables and member functions with implementations, while an interface can only have pure virtual functions.",
    "What is operator overloading in C++?": "Operator overloading is the ability to redefine how operators such as +, -, *, /, etc. work for user-defined types.",
    "What is a constructor in C++?": "A constructor is a member function of a class that is called automatically when an object of the class is created. It is used to initialize the object's member variables.",
    "What is a destructor in C++?": "A destructor is a member function of a class that is called automatically when an object of the class is destroyed. It is used to free up any resources that the object was using.",
    "What is the difference between new and malloc in C++?": "new is an operator in C++ that calls a constructor and returns a pointer to the object it creates, while malloc is a function in C that allocates a block of memory and returns a pointer to the beginning of that block.",
    "What is a smart pointer in C++?": "A smart pointer is a class that acts like a regular pointer, but automatically deletes the object it points to when it is no longer needed.",
    "What is a template in C++?": "A template is a generic programming construct that allows you to define a function or class without specifying the type of data it will work with. The type is specified when the function or class is instantiated.",
    "What is inheritance in C++?": "Inheritance is a mechanism in C++ that allows you to define a new class based on an existing class. The new class (derived class) inherits the properties and behaviors of the existing class (base class)."
}

java_questions_and_answers = {
    "What is the difference between a constructor and a method in Java?": "A constructor is a special method that is called when an object is created, while a method is a regular function that performs a specific task.",
    "What is the difference between an interface and an abstract class in Java?": "An interface is a collection of abstract methods and constants, while an abstract class is a class that may contain both abstract and non-abstract methods.",
    "What is a static method in Java?": "A static method is a method that belongs to the class rather than an instance of the class. It can be called without creating an object of the class.",
    "What is the difference between final, finally, and finalize in Java?": "final is a keyword used to make a variable or method constant, finally is a block of code that is executed regardless of whether an exception is thrown or not, and finalize is a method that is called when an object is garbage collected.",
    "What is polymorphism in Java?": "Polymorphism is the ability of an object to take on many forms. In Java, this is achieved through method overloading and method overriding.",
    "What is the difference between an ArrayList and a LinkedList in Java?": "An ArrayList is backed by an array, while a LinkedList is backed by a doubly-linked list. Accessing an element in an ArrayList is O(1) while accessing an element in a LinkedList is O(n).",
    "What is a synchronized method in Java?": "A synchronized method is a method that can only be accessed by one thread at a time. This is used to prevent race conditions and ensure thread safety.",
    "What is a lambda expression in Java?": "A lambda expression is a concise way to represent an anonymous function. It is often used to write functional interfaces with single abstract methods.",
    "What is the difference between checked and unchecked exceptions in Java?": "Checked exceptions are exceptions that are checked at compile time, while unchecked exceptions are exceptions that are not checked at compile time.",
    "What is the difference between a private, protected, and public access modifier in Java?": "private members can only be accessed within the same class, protected members can be accessed within the same package or subclass, and public members can be accessed from anywhere."
}



def lambda_handler(event, context):
    if 'queryStringParameters' not in event or event['queryStringParameters'] is None:
        return {
            'statusCode': 200,
            'body': 'Welcome to My Software Engineering Quizlet'
        }

        
    else:
        type = event['queryStringParameters']['type']
        question = ''
        if type == 'cPlusPlus':
            question = get_random_c_question()
        elif type == 'java':
            question = get_random_java_question()
        return {
            'statusCode': 200,
            'body': json.dumps(question)
        }
        
        
    
def get_random_cpp_question_and_answer():
    question = random.choice(list(cpp_questions_and_answers.keys()))
    answer = cpp_questions_and_answers[question]
    return question, answer

def get_random_c_question():
    question = random.choice(list(cpp_questions_and_answers.keys()))
    return question

def get_random_java_question():
    question = random.choice(list(java_questions_and_answers.keys()))
    return question
