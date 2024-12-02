# Define the Student class
class Student:
    def hello(self):
        print("Hey there! I'm so excited to learn stuff.")

    def raise_hand(self):
        print("Pick me!")

# Define the ChattyStudent class that inherits from Student
class ChattyStudent(Student):
    def hello(self):
        # Call the parent class's hello() method
        super().hello()
        # Add the chatty student's additional dialogue
        print("How are you doing today? I'm okay, but I'm kind of tired. Did you watch "
              "The Walking Dead last night? You didn't?! Oh man, it was so crazy! What, "
              "you don't want any spoilers? Okay well let me just tell you who died...")

    def raise_hand(self):
        # Use super() to call the parent class's raise_hand() method 10 times
        for _ in range(10):
            super().raise_hand()

# Testing the functionality
if __name__ == "__main__":
    # Test the Student class
    student = Student()
    print("Student says:")
    student.hello()
    student.raise_hand()

    print("\nChattyStudent says:")
    # Test the ChattyStudent class
    chatty_student = ChattyStudent()
    chatty_student.hello()
    chatty_student.raise_hand()
