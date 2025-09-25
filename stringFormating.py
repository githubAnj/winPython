name = "Anjana"
count = 100

print("my favote animals are {},{},{}".format("cat","dog","sheep"))
#output: my favote animals are cat,dog,sheep

print("my favote animals are {1},{0},{2}".format("cat","dog","sheep"))
#output: my favote animals are dog,cat,sheep

print("my favote animals are {c},{d},{s}".format(c="cat",d="dog",s="sheep"))
#output: my favote animals are cat,dog,sheep

print('Hello {}! its a good day'.format(name))
#output: Hello Anjana! its a good day

print(f"Hello {name}") 
#output: Hello Anjana

print(f"Hey! {name} we are on {count} days codeing challenge")
#output: Hey! Anjana we are on 100 days codeing challenge
