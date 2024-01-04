expression = input('Expression: ')
x, y, z = expression.split(' ')
match y:
    case '+':
        ans = float(x)+float(z)
    case '-':
        ans = float(x)-float(z)
    case '*':
        ans = float(x)*float(z)
    case '/':
        ans = float(x)/float(z)
print(f'{ans:.1f}')
