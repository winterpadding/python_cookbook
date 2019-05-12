print('ACME', 50, 91.5)
print('ACME', 50, 91.5, sep=',')
print('ACME', 50, 91.5, sep=',', end='!!\n')

# Will print one item per line
for i in range(5):
    print(i)

# Will print all items on one line, separated by space
for i in range(5):
    print(i, end=' ')

print('')  # Put in a  new line

# If people don't know about the sep and end arguments they will use str.join
print(','.join(('ACME', '50', '91.5')))

share_data = ('ACME', 50, 91.5)
# print(','.join(share_data))  # This will fail

# Works around the above failure
print(','.join(str(x) for x in share_data))

# But this can be simplified by using the print with sep argument
print(*share_data, sep=',')
