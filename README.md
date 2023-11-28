# [Loan Default Prediction: Harnessing Behavioural Insights](#loan-default-prediction-harnessing-behavioural-insights)
 
## Project Overview📽️
---
High value loans will be on our balance sheet on an average of 15-30 years its important for a lending Institution to monitor the borrower in both financial and non financial aspects through out the tenure of the loan. Since the traditional loan default model cover all the financial aspects our model highlights the non-financial/behavioural aspects of the borrower.
Behavioral traits, personal attributes, spending patterns, healthcare insights, legal history, and psychometric assessments collectively influence  a borrower's financial decision-making process and fostering more informed lending practices.
The problem at hand is to develop a robust loan default prediction model that harnesses behavioral insights, delving into the psychological and decision-making aspects of borrowers.
This approach aims to empower financial institutions with a more sophisticated, data-driven tool that can make lending decisions based on a deeper understanding of borrower behavior.

## Model Logic🧠
Our model collects historical transaction activities of the potensial high value loan eligible customers and real time transaction activities of existing loan customers in real time.Data is then seggregated into the following:                     
#### **$\color{red}{Red Flags}$**:Using keywords related to hospitalisation,medical insurance claims,high value online shopping,day trading,online betting activities,frequent food orders(zomato,swiggy)/office commute(ola/uber) during late night would be a risk to the health of the customer and to the bank financially in the long run.
*Historical transaction activities of the deceased customers (Death claimed accounts) can be used to correlate the results.
#### **$\color{green}{Green Flags}$**:Keywords related to investing such as Dividend credits,SI to PPF/PF/NPS/SIP/MF/upstox/IND money,GYM memberships would classify the customer to be fit physically and financially. 
#### **$\color{blue}{Psychometric-profiling}$**:Evaluates customer's behavioral and pyschological traits,providing insights into thier Risk Assessment,Financial Discipline,Stress Handling,Long term planning,Decision Making Patterns,Financial Literacy.A set of 20 crafted questions in a questionnaire can be developed to gather the above insights.


### Tools 🧰
- MS Excel
- SQL
- Machine Learning-Prinipal Component Analysis
- POWER BI

### Data Sources 📂
Real time transactions of customers with relevant details are fetched from CBS. 

|Date      |Time   |Narration                                   |Amount |    
|----------|-------|--------------------------------------------|-------|
|09.04.2023|11:03am|ECS INDIANENERGYEXCHANGE                    |350/-  |    
|12.06.2023|10:07pm|UPI/DR/213837071375/UPSTOX/ICIC/            |2000/- |    
|28.06.2023|08:30pm|UPI/DR/214810301915/APOLLOHOSPITALWHIT/     |6700/- |
|13.07.2023|09:45am|EPPF TRANSACTION PPF01801000719 NGPLINKCELL |10000/-|
|16.07.2023|11:48pm|UPI/CR/212385128555/ZOMATO LTD/PYTM/**ORDER |356/-  |
|01.08.2023|10:09am|GROSS INTCR : 141001144301/2                |1718/- |
|03.08.2023|11:03pm|SALARY CREDIT FOR MAY-2023                  |56783/-| 


### Data Analysis using SQL↗️
The data is then sorted for **$\color{green}{Green Flags}$** and **$\color{red}{Red Flags}$** using SQL.    
- Transaction entries such as EPPF,INT on savings,Dividend credits are marked as  **$\color{green}{Green Flags}$**.  
- Transaction activities during **$\color{red}{midnight hours}$** and entries such as APOLLOHOSPITAL,ZOMATO are marked as **$\color{red}{Red Flags}$**. 

```sql
SELECT * FROM GITHUB EXCEL CSV WHERE Narration IN (ECS,UPSTOX,EPPF,GROSS INTCR);RETURN
'Green Flag'
SELECT * FROM GITHUB EXCEL CSV WHERE Narration IN (APOLLOHOSPITAL,ZOMATO);RETURN
'Red Flag'
```

### Machine Learning📚
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

### Visualisation📺
![SPENDING PATTERN-MONTH WISE DATA JPEG1](https://github.com/sagarhkh/sagarsql/assets/81975233/6b7087e7-5a3c-45bb-97cb-90d39fa8154a)

 ![SPENDING PATTERN-MONTH WISE DATA JPG 2](https://github.com/sagarhkh/sagarsql/assets/81975233/a377b770-ffaf-4700-aa1f-8549d17e5e90)



### Scalability
Transaction data gives insights into demographic spending patterns giving banks more deep understanding of spending behaviors based on age groups, metro/ non-metro regions,  
How India spends is a strong indicator of income, the changing demographics and aspirations of users across the country.
With increase in the no of bank accounts opened and no of UPI users skyrocketing every year all over India, this gives us more data to look into customer spending habits not only in urban parts but in rural parts as well.



### Recommendations
-How spending activities can make a person rich or poor use this predictive analysis during lending.  
-Learning from historical spending activities of successful individuals using the same as a benchmark.


### Limitations:
Since the model is dealing with large real time dataset which are not labelled in many cases we can advice Unified Payment Interface (UPI) apps to introduce mnemonic codes in the transaction id as it would be more authentic and  convenient to identify and segregate them into respective  **$\color{green}{Green Flags}$**/**$\color{red}{Red Flags}$** indicators.   

### Reference 📹
[Canara Dacoe Idea](https://canara-dacoethon.hackerearth.com/challenges/hackathon/canara-dacoe-thon/dashboard/8cdb5f3/idea/published/loan-default-prediction-harnessing-non-financial-insights/)

[Youtube video link](https://youtu.be/NczwkNBXV0E?si=jPU5I9YjIVEKWsn9)

