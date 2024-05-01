head = 'Create your account';
print(head);

user_name = input('Input username: ');
password = input('Input password: ');

print('User', user_name, 'created successfully');

second_head = 'Login now';
print(second_head);

user_name_1 = input('Input username: ');
password_1 = input('Input password: ');

if user_name == user_name_1 and password == password_1:
    print('User logged in successfully');
else:
    print('Invalid credentials');

