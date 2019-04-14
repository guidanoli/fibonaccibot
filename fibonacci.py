import json, facebook, re

def IsBotMessage(msg):
    import re
    regexp = re.findall("F\(.*\) = .*",msg)
    return ( len(regexp) > 0 and regexp[0] == msg )

def FibonacciBot(event, context):
    print("Bot running...")
    token = ""
    try:
        f = open("token.tk","r")
        token = f.readline()
        f.close()
    except IOError:
        print("No token found. Aborting.")
        return

    graph = facebook.GraphAPI(access_token=token)
    valid_posts = []
    print("Gathering last two iterations...")
    posts = graph.get_connections("me","feed")["data"]
    for p in posts:
        if len(valid_posts)>= 2:
            break
        if ("message" in p and IsBotMessage(p["message"]) ):
            valid_posts.append(p)
                
    msg = ""
    print("Calculating current iteration...")
    if( len(valid_posts) == 0 ):
        msg = "F(0) = 1"
    elif( len(valid_posts) == 1 ):
        msg = "F(1) = 1"
    else:
        p0 = valid_posts[0]["message"]
        p1 = valid_posts[1]["message"]
        n0 = int(p0.split(' ')[-1])
        n1 = int(p1.split(' ')[-1])
        n2 = n0 + n1
        count = int(re.findall("F\((.*)\)",p0)[0])+1
        msg = "F({}) = {}".format(count,n2)
        
    try:
        post = graph.put_object("me", "feed", message=msg)
        print("Message posted: \""+msg+"\".")
        print(json.dumps(post))
    except facebook.GraphAPIError:
        print("An error occurred while trying to post to feed.")
        return
        
    return
