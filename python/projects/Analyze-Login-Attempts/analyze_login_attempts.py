# Jordan Fitzgerald
# 9/17/26
# Analyze_Login_Attempts Function

 

#--------------------------------------------------------
# This function analyzes login attempts and provides feedback based on the user's attemps
#--------------------------------------------------------
def analyze_login_attempts(failed_attempts, max_attempts):

    rate = float(failed_attempts) / max_attempts

    if (failed_attempts >= max_attempts):
    
        return "Account Locked. You have exceeded the maximum number of login attempts."
    elif (rate >= 0.5):
        return "Warning: You have failed " + str(failed_attempts) + " login attempts"
    else:
        return "Safe. You have " + str(max_attempts - failed_attempts) + " attempts remaining."








def main():
    result1 = analyze_login_attempts(3, 5)
    print(result1)  # Output: Warning: You have failed 3 login attempts
    result2 = analyze_login_attempts(8, 5)
    print(result2)  # Output: Account Locked. You have exceeded the maximum number of login attempts.
    result3 = analyze_login_attempts(1, 5)
    print(result3)  # Output: Safe. You have 4 attempts remaining.


if __name__ == "__main__":
    main()
