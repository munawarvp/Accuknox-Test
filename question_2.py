'''
Topic: Django Signals

Question 2:
Do django signals run in the same thread as the caller?

Answer:
Yes, by default, Django signals run in the same thread as the caller.
When a signal is emitted, Django executes the connected signal handlers within the same thread as the caller, meaning that any processing done in the signal 
handler will block the caller until it finishes.

Code with example:
'''

# here we have a sample model
class Student(models.Model):
    name = models.CharField(max_length=255)


# Signal handler function that logs the thread ID
# thread ID can be logged using threading.get_ident() and threading is a module in Python
@receiver(post_save, sender=Student)
def student_signal_receiver(sender, instance, **kwargs):
    print(f"Signal handler thread ID: {threading.get_ident()}")


def test_signal_thread():
    print(f"Caller thread ID: {threading.get_ident()}")

    # Creating an instance of Student, which will trigger the post_save signal
    Student.objects.create(name="Test")

# Run the test
test_signal_thread()

'''
Output:
Caller thread ID: 140109026969344 - (sample thread ID)
Signal handler thread ID: 140109026969344

The same thread IDs confirm that the signal handler is executed in the same thread as the caller.
'''
