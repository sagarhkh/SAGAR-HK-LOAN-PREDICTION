# Define a list of 5 psychometric questions

questions_list = [
    "How comfortable are you with your current financial situation?",
    "Do you tend to overspend on non-essential items?",
    "How well do you stick to a budget?",
    "Are you actively saving for the future?",
    "Do you have an emergency fund in place?",
]

# Initialize an empty list to store user responses
responses = []

# Display each question and collect user responses
for i, question in enumerate(questions_list, start=1):
    response = input(f"{i}. {question} (Enter a number between 1 and 5): ")

    # Validate and convert the response to an integer
    try:
        response = int(response)
        if 1 <= response <= 5:
            responses.append(response)
        else:
            print("Invalid response. Please enter a number between 1 and 5.")
            exit()
    except ValueError:
        print("Invalid response. Please enter a number between 1 and 5.")
        exit()

# Calculate the average score
average_score = sum(responses) / len(questions_list)

# Determine the risk category based on the average score
risk_category = "Risky Customer" if average_score > 3 else "Safe Customer"

# Display the result
print("\nCustomer Assessment Result:")
print(f"Average Score: {average_score}")
print(f"Risk Category: {risk_category}")