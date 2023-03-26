# attempt for task 6, squareroot.py
# https://hackernoon.com/calculating-the-square-root-of-a-number-using-the-newton-raphson-method-a-how-to-guide-yr4e32zo
# https://en.wikipedia.org/wiki/Newton%27s_method#:~:text=Newton's%20method%20is%20a%20powerful,some%20difficulties%20with%20the%20method.
# s

#1
num = input ("enter a positive flaoting point number:")

def newtonSqrt (x):
    if x <= 0:
        raise ValueError("x must be a positve number")

    guess = x/2
    while True:
        guess_new = 0.5 * (approx_root + x /approx_root)
        if abs(guess_new - guess) < 1e-9:
            return new_guess

print(f


#2
#  Function to ensure the input is a positive integer

#def readNum():
    number = float(input("Please enter a postive number: "))
    while number < 1:
        print("This is not a positive number")
        number = float(input("Try again! Any postive number: "))

#num = readNum()

# Function to return the sqaureroot of a number
# Using Newtons Method
def sqrt(num):

    x = num                        # set inital guess for sqaure root

    while True:

        root = 0.5 * (x + (num / x))

        if abs(root - x) < 1e-9:
            return root

        #x = root

print(f"The sqaure root of {num} is approx {sqrt(num)}") 