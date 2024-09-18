def guess(l,r):
    mid = (l+r)//2
    ans = ''
    while l<=r and ans =='no':
        print(f'Is your number{mid}?')
        ans = lower(input())

    if ans == 'yes':
        print("Hey we got it! Thanks for playing")
    

print('Hello! Welcome to my Word Guessing Game!')
print('Here you enter an upper bound and a lower bound and we have to try to guess your number!')
print('Okay Lets start!')
lower = input('Lower Bound: ')
upper = input('Upper Bound: ')
while lower > upper:
    print('No silly! Your upper has to be greater than your lower! Here, try again:')
    upper = input('Upper Bound:')
print(f'Soo your guess is somewhere between {lower} and {upper} right? Hmmm...')
guess(lower,upper)