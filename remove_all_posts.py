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

protected_ids = []
f = open("protected.ids","r")
for l in f:
    protected_ids.append(l.strip("\n"))
f.close()

id_list = []

for p in posts:
    post_id = p["id"]
    id_list.append(post_id)
    if post_id in protected_ids:
        print("Post #"+post_id+" bypassed (protected)")
        continue
    try:
        graph.delete_object(post_id)
        print("Post #"+post_id+" has been deleted")
    except facebook.GraphAPIError:
        print(json.dumps(p))
        answer=input("Would you like to protect this post (y/n)? ")
        if(answer.lower()[0]=='y'):
            try:
                f = open("protected.ids","a")
                f.write(post_id)
                f.close()
            except IOError:
                print("Unable to edit protected.ids")
                sys.exit()

new_prot_ids = []

for prot in protected_ids:
    if prot in id_list:
        new_prot_ids.append(prot)
    else:
        print("Id protegido {} não encontrado no feed e removido".format(prot))

if len(new_prot_ids) != len(protected_ids):
    try:
        f = open("protected.ids","w")
        f.write("")
        f.close()
        f = open("protected.ids","a")
        for i in new_prot_ids:
            f.write(i)
        f.close()
    except IOError:
        print("Unable to edit protected.ids")
        sys.exit()
