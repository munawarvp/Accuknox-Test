'''
Topic: Django Signals

Question 3:
By default do django signals run in the same database transaction as the caller?

Answer:
Yes, by default, Django signals run in the same database transaction as the caller if they are triggered within a transaction.
This means that if an error occurs in the signal handler or in the caller after the signal is triggered, the entire transaction,
including changes made by the signal handler, will be rolled back.

Code with example: (for this we have a limitation to demonstrate the code with an example since we dont have any real db transaction)
'''

# here we have a sample model
class Student(models.Model):
    name = models.CharField(max_length=255)

# i have added a log model to store the logs whn Student signal is triggered
class LogEntry(models.Model):
    action = models.CharField(max_length=100)


@receiver(post_save, sender=Student)
def student_signal_receiver(sender, instance, **kwargs):
    print("Signal handler running... Logging an action.")
    LogEntry.objects.create(action="Signal handler executed")


# Function to test transaction behavior with signals
def test_signal_transaction():
    try:
        with transaction.atomic():
            # Creating an instance of Student, which will trigger the post_save signal
            Student.objects.create(name="Test")
            
            # Raising an exception to trigger a rollback
            print("Raising an exception to test rollback...")
            raise Exception("Intentional error to test transaction rollback")
    except Exception as e:
        print(f"Exception caught: {e}")

    # Checking if the log entry from the signal handler was rolled back
    log_entries = LogEntry.objects.filter(action="Signal handler executed")
    print(f"Log entries found after rollback: {log_entries.count()}")

# Run the test
test_signal_transaction()

'''
Output:
Signal handler running... Logging an action.
Exception caught: Intentional error to test transaction rollback
Log entries found after rollback: 0

This will be the output if we test in real db transaction
The log entries count 0 indicates that the log entry from the signal handler was rolled back.
'''