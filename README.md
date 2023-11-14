# [Loan Default Prediction: Harnessing Behavioural Insights](#loan-default-prediction-harnessing-behavioural-insights)
## Using SQL and Machine Learning
## Table of Contents
- [Project Overview](#project-overview)
- [Tools](#tools)
- 
### Project Overview
---
Behavioral traits, influenced by spending patterns, psychometric assessments, and personal attributes, contribute significantly to a borrower's financial decision-making process

identify high-risk behaviors, thereby revolutionizing loan default prediction methodologies and fostering more informed lending practices.

the challenge lies in accurately predicting and preventing loan defaults, 
fall short in capturing the nuanced behavioral aspects of borrowers that influence their repayment behaviors. 

The problem at hand is to develop a robust loan default prediction model that harnesses behavioral insights, delving into the psychological and decision-making aspects of borrowers. 

how personal attributes, spending behaviors, healthcare insights, legal history, and psychometric assessments collectively contribute to credit risk. 

Traditional credit scoring models, while valuable, often lack the ability to capture the intricate behavioral nuances of borrowers that significantly impact their repayment behaviors. 

model that incorporates a deeper understanding of borrower behavior. 

This approach aims to empower financial institutions with a more sophisticated, data-driven tool that can make lending decisions based on a deeper understanding of borrower behavior. 
### Tools 🧰
- MS Excel
- SQL
- POWER BI

### Data Sources 💻
|Narration                                   |Amount |    
|--------------------------------------------|-------|
|ECS INDIANENERGYEXCHANGE                    |350/-  |    
|UPI/DR/213837071375/UPSTOX/ICIC/            |2000/- |    
|UPI/DR/214810301915/APOLLOHOSPITALWHIT/     |6700/- |
|EPPF TRANSACTION PPF01801000719 NGPLINKCELL |10000/-|
|UPI/CR/212385128555/ZOMATO LTD/PYTM/**ORDER |356/-  |
|GROSS INTCR : 141001144301/2               |1718/- |
|SALARY CREDIT FOR MAY-2023                  |56783/-| 


### Data Analysis ↗️
```sql
SELECT * FROM GITHUB EXCEL CSV WHERE Narration IN (ECS,UPSTOX,EPPF,GROSS INTCR);RETURN
'Green Flag'
SELECT * FROM GITHUB EXCEL CSV WHERE Narration IN (APOLLOHOSPITAL,ZOMATO);RETURN
'Red Flag'
SELECT * FROM GITHUB EXCEL CSV WHERE Narration=APOLLOHOSPITAL AND Amount>=30000; RETURN
'Major Health Issue'

```
`column1`

**bold**
*italic*

### Results/Findings


### Recommendations


### Limitations

### Reference

[Canara Dacoe Idea](https://canara-dacoethon.hackerearth.com/challenges/hackathon/canara-dacoe-thon/dashboard/8cdb5f3/idea/published/loan-default-prediction-harnessing-non-financial-insights/)
