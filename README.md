# udnanoDSC01
This repository is created to solve the project for the Udacity Nanodegree in Data Science. The project is a part of the Introduction to data science. 
In this project we solve a really simple data science project by looking at some datasets, coming up with a question and answering it. 
The results are then posted to Medium as a blog post in order to exercise our
ability to communicate complex information

## Medium Post
Wrote a blog post for the project on medium
- https://cudea0.medium.com/failing-forwards-with-game-data-da441a6ca1fa

## Dependencies
The required python libraries are:
- numpy
- pandas
- matplotlib
- sklearn

Additionally some plots use
- plotly
- IPython
- Seaborn
However these cells don't need to be run

## File structure
The files within the project are the following

- jpNotebook.ipynb   : Jupyter notebook containing the results
- data/d1.csv        : File that contains the raw data
- code/              : Contains the back-end computation used in the 
  1. loadData.py Load and clean the raw data
  2. genericPlots.py : Plot functions that rely on matplotlib only
  3. plotPlotyly.py  : Plot functions that rely on plotly as an backend
  4. models.py       : Model building on the dataset


# Dataset
The dataset originates from kaggle, it can be retrieved via:
- https://www.kaggle.com/gregorut/videogamesales
It depectis video game sales of video games with sales greater than 100,000  copies.

It allows us to split video games by platform, year, genre and publisher. Our objective is to expore and validate the dataset. Understand it's deficiencies.

## Research Question
The major research questions will revolve around the validity of the dataset. Once that is done we can ask a few follow up questions.

1. Data validation, how well does this dataset represent our a-priory knowledge
2. What genre is the best selling one
3. Who are the market leaders
4. What is the correlation between producing number of games and overall sales


# About Me
CuDeA  : Custom Design Algorithms is my attempt at setting up a consultancy/company that allows me to follow my passion. I hold a BS in Mechatroics Engineering and MSc in Electrical Engineering from Reykjavik University [Iceland]. There I fell in love with computation and engineering optimization, leading to do my MS thesis on nonlinear optimization. Since then I have been lucky to get jobs in research institutes, first at https://www.iiim.is/, currently at https://www.mining3.com/ where I have been able to hone my programming skills and problem solving for technical issues. 

I am doing this project to refresh my Data Science skills.

For any questions find me at:
- cudea0@gmail.com
