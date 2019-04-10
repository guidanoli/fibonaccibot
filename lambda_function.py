import json, facebook

def lambda_handler(event, context):
    
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
    posts = graph.get_connections("me","feed")["data"]
    valid_posts = []
    protected_ids = []

    try:
        f = open("protected.ids","r")
        for l in f:
            protected_ids.append(l.strip("\n"))
    except IOError:
        print("Couldn't read protected.ids")
        return
    
    for p in posts:
        if not p["id"] in protected_ids:
            valid_posts.append(p)

    if( len(valid_posts) == 0 ):
        graph.put_object("me", "feed", message="F(0) = 1")
        print("F(0) = 1 posted.")
    elif( len(valid_posts) == 1 ):
        graph.put_object("me", "feed", message="F(1) = 1")
        print("F(1) = 1 posted.")
    else:
        import re
        p0 = valid_posts[0]["message"]
        p1 = valid_posts[1]["message"]
        n0 = int(p0.split(' ')[-1])
        n1 = int(p1.split(' ')[-1])
        n_novo = n0 + n1
        contagem = int(re.findall("F\((.*)\)",p0)[0])+1
        msg = "F({}) = {}".format(contagem,n_novo)
        post = graph.put_object("me", "feed", message=msg)
        print(json.dumps(post))
    
    return
