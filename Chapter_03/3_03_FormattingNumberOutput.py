x = 1234.56789

# 'f' string was added in Python 3.6
print(format(x, '0.2f'))
print(f'{x:0.2f}')

print(format(x, '>10.1f'))  # Right justified in by 10 chars.
print(f'{x:>10.1f}')

print(format(x, '<10.1f'))  # Left aligned
print(f'|{x:<10.1f}|')

print(format(x, '^10.1f'))  # Centered
print(f'|{x:^10.1f}|')

print(format(x, ','))
print(f'{x:,}')


print(format(x, '0,.1f'))
print(f'{x:0,.1f}')
