
single = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

plural = ['one', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

n = int(input())

i = 1
out = []

for j in str(n)[::-1]:
    k = int(j)
    if i in [1, 9]:
        out.insert(0, single[k - 1])
    elif i in [2, 5, 7]:
        out.insert(0,plural[k - 1])
    else:
        x = ""
        if i == 3:
            x = "hundred and"
        elif i == 4:
            x = "thousand"
        elif i == 6:
            x = 'lakh'
        else:
            x = 'crore'
        out.insert(0, x)
        out.insert(0, single[k - 1])
    i += 1

print(' '.join(out))