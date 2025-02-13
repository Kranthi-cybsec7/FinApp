def check_loan_eligibility(credit_score):
    if credit_score >= 700:
        return "Loan Approved"
    else:
        return "Loan Denied"

if __name__ == "__main__":
    score = int(input("Enter Credit Score: "))
    print(check_loan_eligibility(score))
