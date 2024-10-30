'''
Topic: Django Signals

Question 1:
By default are django signals executed synchronously or asynchronously?

Answer:
Django signals are executed synchronously. Signals are used to perform any action on modification of a model instance.
When a signal is triggered, Django processes the signal’s connected receivers one by one in the same thread.
There will be a delay in the execution of other tasks which is waiting for the first task to be completed.

Code with example:
'''

# here we have a sample model
class Student(models.Model):
    name = models.CharField(max_length=255)

@receiver(post_save, sender=Student)
def student_model_receiver(sender, instance, **kwargs):
    print("Signal received. Suppose starting a time-consuming task")
    time.sleep(5)  # Simulate a delay
    print("Task completed.")


def test_student_signal():
    start_time = datetime.datetime.now()
    print(f"Start Time: {start_time}")

    # creating a new student to trigger the signal
    Student.objects.create(name="Munawar")

    end_time = datetime.datetime.now()
    print(f"End Time: {end_time}")

    # Calculate the time difference
    print(f"Time Taken: {end_time - start_time}")


# Running the test of Student signal
test_student_signal()

'''
Output:
Start Time: 2024-10-28 10:00:00 - (sample datetime)
Signal received. Starting time-consuming task...
Task completed.
End Time: 2024-10-28 10:00:05 - (sample datetime)
Time Taken: 0:00:05.000000

The delay of 5 seconds indicates that the signal handler (student_model_receiver) executed synchronously, holding up the entire process until it completed.

'''