from users import *

sowon = users('sowon', 'kim', 'F', '1234567')
sowon.describe_user()
sowon.greet_user()

print('\n')

pyo = users('pyo', 'pyo', 'O', '23456')
pyo.describe_user()
pyo.greet_user()
for value in range(0,3):
    print(f"\n{pyo.staff_no} login failed:")
    pyo.increment_login_attempts()
print("Finally login successed:")
pyo.reset_login_attempts()

print('\n')
daniel = users('daniel', 'kang', 'M', '2134123')
daniel.describe_user()
daniel.greet_user()

yerin = admin('yerin', 'jung', 'F', '23141234')
yerin.describe_user()
yerin.greet_user()
yerin.show_privileges()
