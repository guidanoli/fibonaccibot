import sys, json, facebook

print("Removing all posts...")
    
token = ""

try:
    f = open("tokens.tk","r")
    token = f.readline()
    f.close()
except IOError:
    print("No token found. Aborting.")
    sys.exit()

graph = facebook.GraphAPI(access_token=token)
posts = graph.get_connections("me","feed")["data"]
valid_posts = []

print("Updating protected posts list...")

for p in posts:
    post_id = p["id"]
    if ("message" in p):
        import re
        msg = p["message"]
        if (re.findall("F\(.*\) = .*",msg)[0] == msg):
            try:
                graph.delete_object(post_id)
                print("Post #"+post_id+" has been deleted")
            except facebook.GraphAPIError:
                print(json.dumps(p))
                print("Post #"+post_id+" could not be deleted")
