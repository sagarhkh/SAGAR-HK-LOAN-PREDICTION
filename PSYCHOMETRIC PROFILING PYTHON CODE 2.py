class CustomerRiskAssessment:
    def __init__(self, questions):
        self.questions = questions
        self.answers = []

    def get_responses(self):
        print("Please provide responses on a scale of 1 to 5 (1: Strongly Disagree, 5: Strongly Agree):")
        for i, question in enumerate(self.questions, start=1):
            response = input(f"{i}. {question}: ")
            try:
                response = int(response)
                if 1 <= response <= 5:
                    self.answers.append(response)
                else:
                    print("Invalid response. Please enter a number between 1 and 5.")
                    return self.get_responses()
            except ValueError:
                print("Invalid response. Please enter a number between 1 and 5.")
                return self.get_responses()

    def assess_risk(self):
        if len(self.answers) == len(self.questions):
            total_score = sum(self.answers)
            average_score = total_score / len(self.questions)

            if average_score <= 2.5:
                return "Low Risk"
            elif 2.5 < average_score <= 3.5:
                return "Medium Risk"
            else:
                return "High Risk"
        else:
            return "Incomplete Assessment. Please answer all questions."

# Example usage
questions_list = [
    "I am comfortable taking risks.",
    "I tend to worry about the future.",
    # Add more questions as needed
]

customer_assessment = CustomerRiskAssessment(questions_list)
customer_assessment.get_responses()
risk_category = customer_assessment.assess_risk()

print(f"\nRisk Assessment Result: {risk_category}")
