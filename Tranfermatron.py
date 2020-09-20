import praw
import pandas as pd
import time

print('****************************************************************************************')
project_name='REDDIT ACCOUNT TRANSFORMATOR X50'
made_by="Adit Ahmedabadi"
Date="10th August 2020"
print(project_name.center(85))
print(made_by.center(85))
print(Date.center(85))
print('****************************************************************************************')

#Getting Details Of Original Account
username_i=input("Enter Username of your Original Account:")
client_id_i=input("\nEnter Client ID of your Original Account:")
client_secret_i=input("\nEnter Client Secret ID of your Original Account:")
password_i=input('\nEnter Password for Original Account:')
user_agent_i=input('\nEnter user agent (Press Enter if you dont have one:')
if len(user_agent_i)<1:
    user_agent_i="randomgibberish_import"

#authenticating the account using Python Reddit API Wrapper (PRAW)
reddit = praw.Reddit(client_id=client_id_i,
client_secret=client_secret_i,
username=username_i,
password=password_i,
user_agent=user_agent_i)
print("Export User Authenticated!")

#extrcting user subscribed subreddits
sub_reddit=reddit.user.subreddits()
print(type(sub_reddit))
subreddit_lst=list()
subscriber_lst=list()  #show number of suscribers
for i in sub_reddit:
    subreddit_lst.append(i.display_name)
    subscriber_lst.append(i.subscribers)

subreddit_dict=dict()
subreddit_dict['Name']=subreddit_lst
subreddit_dict['Subsribers']=subscriber_lst

#changing the panda module configuration to display each and every subreddit
pd.set_option("display.max_rows", None, "display.max_columns", None)

print("Printing All The Subreddits u Joined.........")
print('=======================================================')
#printing out subreddits in an organized form
brics = pd.DataFrame(subreddit_dict)
print(brics)
print('=======================================================')

export_lst=subreddit_lst
print("\n\n==================SUBREDDIT TRANSFER=====================")


#Getting Details Of New Account Account
username_e=input("Enter Username of your New Account:")
client_id_e=input("\nEnter Client ID of your New Account:")
client_secret_e=input("\nEnter Client Secret ID of your New Account:")
password_e=input('\nEnter Password for New Account:')
user_agent_e=input('\nEnter user agent (Press Enter if you dont have one:')
if len(user_agent_e)<1:
    user_agent_e="randomgibberish_export"


reddit = praw.Reddit(client_id=client_id_e,
client_secret=client_secret_e,
username=username_e,
password=password_e,
user_agent=user_agent_e)
print("\nImport User Authenticated!")

print("\nJoining The Provided Subreddits..... (Press Ctrl+C to Skip in Between)")
for i in export_lst:
    if KeyboardInterrupt:
        print("Process Interrupted By User...skipping to next step.....")
    sub_reddit=i
    subreddit = reddit.subreddit(sub_reddit)
    start = time.time()
    print('Joining',i,'.......')
    subreddit.subscribe()
    print('Joined',i,'!')
    print('--------------------------------')
    end = time.time()
print(f"Time for joining subreddits is {end - start}")

print("Subscribed to all originally subscribed subreddits!")


choice=input("\n\nWould You Like to add new ones? (Y/N)")
if choice == 'Y' or 'y':
    how_many=input('How Many?')
    for i in range(0,int(how_many)):
        extra_sub= input("\nEnter the Name of The Subreddit you would like to subscribe to:")
        if extra_sub.startswith('r/'):
            extra_sub=extra_sub[2:]
        ex_subreddit = reddit.subreddit(extra_sub)
        print('Joining',extra_sub,'.......')
        ex_subreddit.subscribe()
        print('Joined',extra_sub,'!')

print("Thank You!")