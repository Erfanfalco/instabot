import pandas as pd

follower = pd.read_csv('followers_1 (1).csv').dropna()
following = pd.read_csv('following.csv').dropna()


def search(followings):
    follow = []
    for i in range(0, 349):
        try:
            if len(followings['ani'][i]) < 20:
                follow.append(followings['ani'][i])
        except:
            pass
    return follow


flwing = search(following)
flwrs = search(follower)

distinct_items = flwing
for item in flwing:
    if item not in flwrs:
        print(item)
        distinct_items.remove(item)

# print(distinct_items)