from itertools import islice
batch_processing = __import__('1-batch_processing').batch_processing

for user in islice(batch_processing(50), 50):
    print(user)
