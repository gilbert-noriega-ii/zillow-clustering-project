<a id='section_6'></a>
<img src= 
"
https://www.investopedia.com/thmb/zYw_VrQD4QAfkV3b_SaFzb9NOpo=/960x416/filters:no_upscale():max_bytes(150000):strip_icc()/Zillow2-d26f9db6cd8842d1a999cb70e5dadd3a.jpg" 
         alt="GeeksforGeeks logo" 
         align="right"> 

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
> My goal for this project is to create a model that will find what is driving the errors in the Zestimates of single unit properties in 2017 by including clustering methodologies. I will deliver the following in a github repository: 
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
| structure_dollar_per_sqft | the amount per sqft for the home |
| bedroomcnt  | the amount of bedrooms inside the home |
| calculatedfinishedsquarefeet| the total square feet of the home |
| orange  | orange county |
| no heating | no heating system |
| longitude  | the longitude coordinate|
| los_angeles | los_angeles county|
| latitude  | the latitude coordinate |
| taxrate | tax amount divided by tax valuedollarcnt |
| central_heating | central heating system |
| poolcnt  | the number of pools |
| roomcnt| the total number of rooms |
| age  | years since it has been built |
| land_dollar_per_sqft | price of the home per sqft |
| acres  | the amount of the land |
| floor_wall_heating | type of heating system|
| fireplacecnt  | the total amount of fireplaces |
| bed_bath_ratio | the ratio of bedrooms to bathrooms |
| regionidcity | region id city number |
| regionidzip  | region id zip number|
| ventura | ventura county  |

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
>   - H<sub>0</sub>: The mean logerror is the **same** across all counties
>   - H<sub>a</sub>: The mean logerror is **not the same** across all counties
>
> - Hypothesis 2:
>   - H<sub>0</sub>: Log errors for low cost per sqft houses **are the same** as the log errors for the rest of the houses
>   - H<sub>a</sub>: Log errors for low cost per sqft houses **are different** than the log errors for the rest of the houses
>
> - Hypothesis 3:
>   - H<sub>0</sub>: The mean logerror is the **same** across all bedrooms
>   - H<sub>a</sub>: The mean logerror is **not the same** across all bedrooms
>
> - Hypothesis 4:
>   - H<sub>0</sub>: The mean logerror is the **same** across all heating systems
>   - H<sub>a</sub>: The mean logerror is the **same** across all heating systems
>
> - Hypothesis 5:
>   - H<sub>0</sub>: The mean logerror is the **same** across all size clusters
>   - H<sub>a</sub>: The mean logerror is **not the same** across all size clusters
>
> - Hypothesis 6:
>   - H<sub>0</sub>: The mean logerror is the **same** across all feature clusters
>   - H<sub>a</sub>: The mean logerror is the **same** across all feature clusters
>
> - Hypothesis 7:
>   - H<sub>0</sub>: The mean logerror is the **same** across all value clusters
>   - H<sub>a</sub>: The mean logerror is the **same** across all value clusters

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
>    - which features are most influential: use rfe
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
>2. Install acquire.py, prepare.py and model.py into your working directory.
>3. Run a jupyter notebook importing the necessary libraries and functions.
>4. Follow along in final_report.ipynb or forge your own exploratory path. 

[back to the top](#section_6)