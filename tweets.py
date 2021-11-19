def tweet_count():
    number=int(input())
    tweets={}
    for j in range(0,number):
        a=input()
        a.split()
        # print(a)
        user,tweet=a[0],a[1]
        if user in tweets:
            tweets[user].append(tweet)
        else:   
            tweets.update({user:[tweet]})
    
    for x in tweets:
        print(x,len(tweets[x]))

if __name__=='__main__':
    init=int(input())

    for i in range(0,init):
        tweet_count()