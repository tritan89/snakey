# Battlesnake Python Starter Project



![Battlesnake Logo](https://media.battlesnake.com/social/StarterSnakeGitHubRepos_Python.png)

This project was done during a hackathon by myself and Carson Jennings on March 11, 2023. 

During this competition we successfully implemented an snake that could navigate to collect food and avoid going head to head with snakes of equal or greater length.

We began with the python starter code to implment our snake in, we quickly figured out how to build the basic snake so it would

1. not run into walls 
2. not run into itself
3. not run into other snakes 

Our first challenge was to figure out how to make our snake navigate towards food. Our stratagey was to find the nearest food then head in a straight line towards it. To do this we searched through the list of foods then calcuted the distance from our head to the nearest one by 

