
#mijn versie
import secrets

secretsGenerator = secrets.SystemRandom()

random_number = secretsGenerator.randint(100000, 999999)
print(random_number)

#site versie
# import secrets
#
# #Getting systemRandom class instance out of secrets module
# secretsGenerator = secrets.SystemRandom()
#
# print("Generating 6 digit random OTP")
# otp = secretsGenerator.randrange(100000, 999999)
#
# print("Secure random OTP is ", otp)