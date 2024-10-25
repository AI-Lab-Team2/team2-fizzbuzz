def fizzbuzz(num: int) -> str:
    '''
    3 -> fizz
    5 -> buzz
    15 -> fizzbuzz
    else -> number

    input: int
    output: str
    '''
    if num == 3 or num == 5:
        return 'fizz'*(num%3==0) + 'buzz'*(num%5==0)
    else:
        return f"{num}"