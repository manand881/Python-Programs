# learning how to use textwrap and decide width of print statement
import textwrap
i=10
while(i<200):
    print(textwrap.fill("Earlier today, I announced that I’m considering taking Tesla private at a price of $420/share. I wanted to let you know my rationale for this, and why I think this is the best path forward. First, a final decision has not yet been made, but the reason for doing this is all about creating the environment for Tesla to operate best. As a public company, we are subject to wild swings in our stock price that can be a major distraction for everyone working at Tesla, all of whom are shareholders. Being public also subjects us to the quarterly earnings cycle that puts enormous pressure on Tesla to make decisions that may be right for a given quarter, but not necessarily right for the long-term. Finally, as the most shorted stock in the history of the stock market, being public means that there are large numbers of people who have the incentive to attack the company.",width=i))
    i+=10