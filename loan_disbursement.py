import sys
sys.path.append("../dev1")  # Allows importing from dev1

from loan_app import check_loan_eligibility

def disburse_loan(credit_score, amount):
    approval_status = check_loan_eligibility(credit_score)
    
    if approval_status == "Loan Approved":
        return f"✅ Loan of ${amount} has been disbursed successfully!"
    else:
        return "❌ Loan cannot be disbursed due to low credit score."

if __name__ == "__main__":
    score = int(input("Enter Credit Score: "))
    amount = float(input("Enter Loan Amount: $"))
    
    print(disburse_loan(score, amount))
