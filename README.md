<a id='section_6'></a>
<h1><center>Zillow Clustering Project</center></h1>
<center> Author: Gilbert Noriega </center>

[About the Project](#section_1) [Data Dictionary](#section_2) [Initial Hypotheses/Thoughts](#section_3) [Project Plan](#section_4) [How to Reproduce](#section_5)



<a id='section_1'></a>
## About the Project
___

### Background
> I am a junior data scientists on the Zillow data science team and while trying to find the stength to finish my project at 4pm on Friday, I get a tap on my shoulder from someone behind me. When I turn around, I am surprised to find that it is Mr. Zillow himself. He says to me, "Hey, I here you are good with numbers. Can you tell me what is driving the errors in the Zestimates for single unit/single family homes in 2017?" ;-) 
>I manage to muster out the words, "Yes, I can definitely do that!" thinking to myself that I did'nt know he even knew my name. 
>He responds with "Great, I knew I could count on you!" but as he is walkling out the door, he leaves me with one final remark...
>"By the way, I have a very important meeting on Wednesday with the data science team and would like you to share what you find. Thanks, have a great weekend."
>>
> Looks like we got a lot of work to do. Might as well get started!

___
>*Acknowledgement:The dataset was provided by Codeup from the MySequel Database* 

___

### Goals
> My goal for this project is to create a model that will find what is driving the errors in the Zestimates of single unit properties in 2017 by including clustering methodologies. We will deliver the following in a github repository: 
>
> - A clearly named final notebook. This notebook will be what I present and will contain plenty of markdown documentation and cleaned up code.
> - A README that explains what the project is, how to reproduce you work, and your notes from project planning
> - A Python module or modules that automate the data acquisistion and preparation process. These modules should be imported and used in your final notebook.
  
[back to the top](#section_6)

___

<a id='section_2'></a>
## Data Dictionary

| Features | Definition |
| :------- | :-------|
| bathroom | the amount of bathrooms inside the home |
| bedroom  | the amount of bedrooms inside the home |
| sqft| the total square feet of the home |
| fips  | numeric codes which uniquely identify geographic areas |
| fullbathcnt | the amount of full bathrooms(shower included) inside the home |
| lotsqft  | the total square feet of the entire property |
| poolcnt | amount of pools at the home|
| roomcnt  | the total amount of rooms inside the home |
| yearbuilt | the year the home was built |

|  Target  | Definition |
|:-------- |:---------- |
|  logerror  | the log of the difference between what the zestimate is and the actual selling price |

[back to the top](#section_6)
___
<a id='section_3'></a>
## Initial Hypothesis & Thoughts

>### Thoughts
>
> - We could add a new feature?
> - Should I turn the continuous variables into booleans?

>### Hypothesis
> - Hypothesis 1:
>   - H<sub>0</sub>: ____ and ____ are **independent**
>   - H<sub>a</sub>: ____ and ____ are **dependent**
>
> - Hypothesis 2:
>   - H<sub>0</sub>: There is **no difference** ____
>   - H<sub>a</sub>: There is **a difference** ____


[back to the top](#section_6)
___
<a id='section_4'></a>
## Project Plan: Breaking it Down

>- acquire
>    - acquire data from MySQL
>       - join tables to include transaction date
>    - save as a csv and turn into a pandas dataframe
>    - summarize the data
>    - plot distribution
>
>- prepare
>    - address missing data
>    - create features
>    - split into train, validate, test
>
>- explore
>    - test each hypothesis
>    - plot the continuous variables
>    - plot correlation matrix of all variables
>    - create clusters and document its usefulness/helpfulness
>
>- model and evaluation
>    - which features are most influential: use SelectKBest and rfe
>    - try different algorithms: LinearRegression, LassoLars, Polynomial Regression
>    - evaluate on train
>    - evaluate on validate
>    - select best model
>    - create a model.py that pulls all the parts together.
>    - run model on test to verify.
>
>- conclusion
>    - summarize findings
>    - make recommendations
>    - next steps


[back to the top](#section_6)

___

<a id='section_5'></a>
## How to Reproduce

>1. Download data from zillow database in MySQL with Codeup credentials.
>2. Install acquire.py and prepare.py into your working directory.
>3. Run a jupyter notebook importing the necessary libraries and functions.
>4. Follow along in final_report.ipynb or forge your own exploratory path. 

[back to the top](#section_6)