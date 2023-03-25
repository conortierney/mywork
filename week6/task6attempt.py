# attempt for task 6, squareroot.py
# https://hackernoon.com/calculating-the-square-root-of-a-number-using-the-newton-raphson-method-a-how-to-guide-yr4e32zo
# https://en.wikipedia.org/wiki/Newton%27s_method#:~:text=Newton's%20method%20is%20a%20powerful,some%20difficulties%20with%20the%20method.


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