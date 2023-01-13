# import numpy as np 
# import matplotlib.pyplot as plt

# x=np.arange(0,3*np.pi,0.1)
# y=np.sin(x)

# print(x)
# print(y)

# plt.plot(x,y)
# plt.show()

# print("I am here")






# import numpy as np 
# import matplotlib.pyplot as plt

# x=np.arange(0,3*np.pi,0.1)
# y_sin=np.sin(x)
# y_cos=np.cos(x)





# plt.plot(x,y_sin)
# plt.plot(x,y_cos)

# plt.xlabel('x  axis lable')
# plt.ylabel('y  axis lable')
# plt.title('Sine and cosine')
# plt.legend(['Sine','cpsine'])
# plt.show()

# print("I am here")





# import numpy as np 
# import matplotlib.pyplot as plt

# x=np.arange(0,3*np.pi,0.1)
# y_sin=np.sin(x)
# y_cos=np.cos(x)





# plt.plot(x,y_sin)
# plt.plot(x,y_cos)

# #create the first subplot
# plt.subplot(2,1,1)  #2 is height 1 breath and 1 is active (position define karta hai)
# plt.plot(x,y_sin)

# #create the second subplot
# plt.subplot(2,1,2)
# plt.plot(x,y_cos)


# plt.xlabel('x  axis lable')
# plt.ylabel('y  axis lable')
# plt.title('Sine and cosine')
# #plt.legend(['Sine','cpsine'])
# plt.show()

# print("I am here")






import numpy as np 
import matplotlib.pyplot as plt

# x=np.arange(0,3*np.pi,0.1)
# y_sin=np.sin(x)
# y_cos=np.cos(x)
x=np.linspace(-20,20,1000)
def func(x):
    y=[]
    for elem in x:
        # # result =elem**2
        # result = -5*(elem**2) + 4*elem**2
        result = 1 - (elem**2)/2
        y.append(result)
    return y

y =   func(x)  
plt.plot(x,y)      



plt.xlabel('x  axis lable')
plt.ylabel('y  axis lable')
plt.title('Sine and cosine')
plt.show()

print("I am here")









