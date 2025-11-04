def add_all(a1,a2,a3,a4):
    return a1 + a2 + a3 + a4

val = (1,2,3,4)
dic_val = {"a1":1,"a2":2,"a3":5,"a4":7}
print("results\n",add_all(*val))
print(f"second results:{add_all(**dic_val)}") # the same as add_all(a1=dict_val["a1"],a2=dict_val["a2"],a3=dict_val["a3"],a4=dict_val["a4"])

def multiply_all(**kwargs):
    print(kwargs)

multiply_all(a=2,b=23,c=2,d=4,e=24,f=43)