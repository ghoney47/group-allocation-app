# group-allocation-app
181ag Final Project
## Mechanism for Hedonistic Coalition Allocation (Draft)

**Drew Goldman, Gavin Honey**

From the perspective of the authors, it is a common occurrence that, during large group gatherings, small sub-groups are often created to have more realistic connection, and to keep everyone included and occupied at a higher level. With this reality, the next (and more difficult) problem is clearly how to designate those groups. Maybe one would want to assign groups randomly, but what if we wanted to apply some level of provable optimality within pairings? This is the question that we want to answer with this project through the application of the Deferred Acceptance algorithm in 1:1 matching and a mix of matching algorithms to achieve group matches. Our goal with this project is to design a matching algorithm that is built of other algorithms from our class and evaluate its outputs.

### Problem Description

We are trying to propose a solution to a group-allocation problem (formally *hedonistic coalitions*) where we have some $n$ agents input their preferences over all the other agents in the group, then we will output some group matching. We will judge our algorithm on the following criteria over some datasets (likely to use the datasets as in *Mechanism Design for Team Formation* in their experiments section): Pareto Optimality, Stability, and Runtime (can we get an output in time linear to the input $O(n^2)$).

### Background

We plan to read both *Mechanism Design for Team Formation* and *The Stability of Hedonic Coalition Structures*. The former is a design of a mechanism, and though we will not necessarily prove any of the conditions of the algorithm, it gives us some background on some datasets we can use to test as well as some methodology on evaluating algorithms. The latter paper gives us a broader understanding of the hedonistic coalition allocation problem space and some potential criteria to aim for (hedonistic stability, etc.). **See proposed algorithm below!**

### Our Proposed Algorithm

As a note, the budget idea is mimicking the A-CEEI-TP algorithm and its predecessors. We want to explore how a budget could be used on a more simplistic mechanism.

**Algorithm: TTC with Utility Preferences**

**Require:** Quantitative preferences over all agents from each agent with a fixed individual budget $B$

1. Compute number of groups from number of agents $n$ and the desired group size $k$ (note the groups may not all be equal in size)
2. Randomly place $k$ of the $n$ agents: one into each group
3. Compute the ranking of each group (cumulative for all agents within the group for each agent yet to be assigned) based on the submitted weighted ranking from each agent
4. Compute each group's ranking of the other agents using funds in $B$ such that each group's ranking is the sum of all of the agents' own rankings
5. Use the top ranked scores for each group and agent as edges in the TTC mechanism
6. Run single iteration of TTC
7. Recompute scores for groups of remaining agents, and recompute scores for agents for each group
8. Repeat steps 5–7 until there are no unmatched agents.

At a high level we have each player compute a weighted Borda Score within their allotted budget (they could value someone very highly) and submit that. Using that score we calculate each group's optimal choice for who to include.

Our testing will try to evaluate how well our algorithm performs and we will also test to see how different budget amounts (essentially weighted Borda Count) will affect matchings to see if there is some approximately optimal initial budget for some $n$ agents.
