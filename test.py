from zxcvbn import zxcvbn

password="Dh102299$%!"

result = zxcvbn(password)
print(result['score'])