# Battlesnake Python Starter Project



![Battlesnake Logo](https://media.battlesnake.com/social/StarterSnakeGitHubRepos_Python.png)

This project was done during a hackathon by myself and Carson Jennings on March 11, 2023. 

During this competition we successfully implemented an snake that could navigate to collect food and avoid going head to head with snakes of equal or greater length.

We began with the python starter code to implement our snake in, we quickly figured out how to build the basic snake so it would

1. not run into walls 
2. not run into itself
3. not run into other snakes 

Our first challenge was to figure out how to make our snake navigate towards food. Our strategy was to find the nearest food then head in a straight line towards it. To do this we searched through the list of foods then calculated the distance from our head to the nearest one by finding the relative distance of our head to each food.
Then we moved towards the food by choosing the best possible move out of our give safe moves. 

After testing this functionality we found that if another snake was implementing the same strategy then we would end up colliding head to head and die quite often. To eliminate this behaviour we checked if there was an enemy head within 2 spaces of the food we were going for and if there was then we checked its length, If it was less than ours we would continue onto the food else we would pick the next closest food. 

# results

In the tournament we competed in our snake was able to make it past the first round and almost into the third round. Overall this experience taught me how to make quick decisions, collaborate quickly and effectively, and code well under pressure. I would like to try another battlesnake tournament next time building the snake a few weeks in advance to improve its performance.  

