import winsound


def collatz(i):
    if i[0] == 1:
        return [1] + i
    elif i[0] % 2 == 1:
        return collatz([3*i[0] + 1] + i)
    return collatz([int(i[0]/2)] + i)


def get_input():
    num=0
    while num < 1 or num > 32000:
       num = int(input("Enter a number between 1 and 32000: "))
    return num


class TestApp:
    def __init__(self):
        print("Test class initialized!")
        v = get_input()
        print("Getting result: "+str(v))
        result = collatz([v])
        print("Collatz beep with " + str(len(result)) + " steps: \n " + str(result))
        max_result = max(result)

        # The average human can hear between about 20hz and 20k hz. This is our range.
        # We are making sure that people can hear our beautiful collatz music
        step = (20000 - 20) / max_result
        for i in result:
            tone = 20 + int(step * i)

            # Validation
            tone = max([tone, 37])
            tone = min([tone, 32767])

            winsound.Beep(tone, 500)


app = TestApp()

