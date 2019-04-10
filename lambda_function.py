import json, facebook

def lambda_handler(event, context):
    import re
    print("Lambda Function running...")
    
    token = ""
    
    try:
        f = open("tokens.tk","r")
        token = f.readline()
        f.close()
    except IOError:
        print("No token found. Aborting.")
        return

    graph = facebook.GraphAPI(access_token=token)
    valid_posts = []

    print("Updating protected posts list...")
    posts = graph.get_connections("me","feed")["data"]

    for p in posts:
        if len(valid_posts)>= 2:
            break
        post_id = p["id"]
        if ("message" in p):
            msg = p["message"]
            if (re.findall("F\(.*\) = .*",msg)[0] == msg):
                valid_posts.append(p)

    msg = ""

    if( len(valid_posts) == 0 ):
        msg = "F(0) = 1"
    elif( len(valid_posts) == 1 ):
        msg = "F(1) = 1"
    else:
        p0 = valid_posts[0]["message"]
        p1 = valid_posts[1]["message"]
        n0 = int(p0.split(' ')[-1])
        n1 = int(p1.split(' ')[-1])
        n_novo = n0 + n1
        contagem = int(re.findall("F\((.*)\)",p0)[0])+1
        msg = "F({}) = {}".format(contagem,n_novo)

    try:
        post = graph.put_object("me", "feed", message=msg)
        print("Message posted: \""+msg+"\"")
        print(json.dumps(post))
    except facebook.GraphAPIError:
        print("An error occurred while trying to post message.")
    
    return
