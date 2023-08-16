# stockBot

## This program is my attemp at developing an algorithmic trading framework. It is built in python, utilizing YFinance, VectorBT, and Pandas-TA mainly. Some of these frameworks may prove redundant, but the focus on this project now is to determine which frameworks will work best for my implementation.

### Currently, I have developed a small MySQL database implementation to store the results of my testing, as well as a simple class layout for what my implementation should need in the future.

### At this point, I am using Jupyter to test out the above libraries, so as to reduce my API calling and better visualize the data transformations that will occur in the future.

### Minimum env
> Python 3.6
> conda install -c conda-forge discord.py
> conda install -c conda-forge cchardet
> conda install -c conda-forge charset-normalizer
> conda install flask_restful
> pip install yfinance
> pip install pandas-ta
> pip install -U vectorbt