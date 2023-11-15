# [Loan Default Prediction: Harnessing Behavioural Insights](#loan-default-prediction-harnessing-behavioural-insights)
 
## Project Overview
---
High value loans will be on our balance sheet on an average of 15-30 years its equally important for a lending institution to monitor the borrower in both financial and non financial aspects through out the tenure of the loan. Since the traditional loan default model cover all the financial aspects our model highlights the non-financial/behavioural aspects of the borrower.
Behavioral traits, personal attributes, spending patterns, healthcare insights, legal history, and psychometric assessments collectively influence  a borrower's financial decision-making process and fostering more informed lending practices.
The problem at hand is to develop a robust loan default prediction model that harnesses behavioral insights, delving into the psychological and decision-making aspects of borrowers.
This approach aims to empower financial institutions with a more sophisticated, data-driven tool that can make lending decisions based on a deeper understanding of borrower behavior.

### Tools 🧰
- MS Excel
- Machine Learning-Prinipal Component Analysis
- SQL
- POWER BI

### Data Sources 💻
Real time transactions of customers are fetched from CBS with relevant details which are then sorted for **$\color{green}{Green Flags}$** and **$\color{red}{Red Flags}$** using SQL.    
- Transaction entries such as EPPF,INT on savings,Dividend credits are marked as  **$\color{green}{Green Flags}$**  
- Transaction entries such as APOLLOHOSPITAL,ZOMATO are marked as **$\color{red}{Red Flags}$** 

|Date      |Time   |Narration                                   |Amount |    
|----------|-------|--------------------------------------------|-------|
|09.04.2023|11:03am|ECS INDIANENERGYEXCHANGE                    |350/-  |    
|12.06.2023|10:07pm|UPI/DR/213837071375/UPSTOX/ICIC/            |2000/- |    
|28.06.2023|08:30pm|UPI/DR/214810301915/APOLLOHOSPITALWHIT/     |6700/- |
|13.07.2023|09:45am|EPPF TRANSACTION PPF01801000719 NGPLINKCELL |10000/-|
|16.07.2023|11:48pm|UPI/CR/212385128555/ZOMATO LTD/PYTM/**ORDER |356/-  |
|01.08.2023|10:09am|GROSS INTCR : 141001144301/2                |1718/- |
|03.08.2023|11:03pm|SALARY CREDIT FOR MAY-2023                  |56783/-| 


### Data Analysis ↗️
```sql
SELECT * FROM GITHUB EXCEL CSV WHERE Narration IN (ECS,UPSTOX,EPPF,GROSS INTCR);RETURN
'Green Flag'
SELECT * FROM GITHUB EXCEL CSV WHERE Narration IN (APOLLOHOSPITAL,ZOMATO);RETURN
'Red Flag'
```

### Machine Learning
**Dimensionality Reduction:**

**Challenge**: Huge datasets with numerous spending-related features can lead to a complex and computationally demanding model.                         
**PCA Solution**: Reduces the dimensionality of the dataset by transforming the original features into a smaller set of  principal components. This not only simplifies the dataset but also helps maintain the most significant information related to spending patterns.

**Identifying Dominant Spending Patterns:**

**Challenge**: Understanding which spending patterns significantly impact the loan prediction model can be intricate in large datasets.                                
**PCA Solution**: Identifies the principal components that capture the most critical spending behaviors influencing loan predictions.

**Reducing Noise and Redundancy:**

**Challenge**: Large datasets may contain noise and redundant information that can affect predictive accuracy.          
**PCA Solution**: Filters out noise and redundant information, emphasizing the most critical spending patterns. 


**Deep Behavioral Insights:**

**Challenge:** Extracting nuanced insights from extensive spending data to understand customer behavior deeply.       
**PCA Solution:** Helps uncover hidden patterns and relationships within the spending data. By capturing the essence of spending patterns in principal components, PCA provides a foundation for deep behavioral insights, aiding in the understanding of complex customer behaviors and preferences.

 This approach ensures that the essential information is retained while addressing the challenges associated with large and complex datasets, ultimately improving the accuracy and effectiveness of the loan prediction process.

### Visualisation:
![SPENDING PATTERN-MONTH WISE DATA JPEG1](https://github.com/sagarhkh/sagarsql/assets/81975233/6b7087e7-5a3c-45bb-97cb-90d39fa8154a)

 ![SPENDING PATTERN-MONTH WISE DATA JPG 2](https://github.com/sagarhkh/sagarsql/assets/81975233/a377b770-ffaf-4700-aa1f-8549d17e5e90)



### Results/Findings


### Recommendations


### Limitations:

### Reference
[Canara Dacoe Idea](https://canara-dacoethon.hackerearth.com/challenges/hackathon/canara-dacoe-thon/dashboard/8cdb5f3/idea/published/loan-default-prediction-harnessing-non-financial-insights/)
