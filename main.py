# project in the Automate the Boring Things with Python book.
import random
def getAnswer(*answer_number):
    answer_number = {1: 'it is certain', 2: 'it is decidely so', 3: 'yes', 4: 'Reply hazy try again',
                    5: 'Ask again later', 6: 'Concentrate and ask again', 7: 'My reply is no',
                    8: 'Outlook not so good', 9: 'Very doubtful', 10: 'Hell no, brother!'}

    r = random.randint(1, 10)
    print(answer_number[r])


getAnswer()
