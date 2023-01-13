import numpy as np

arr = np.array(
    [1,2,4]

)

print("no coma means matics=>",arr,type(arr))
print("SHape of the array :",arr.shape)
print(arr[0],arr[1],arr[2])



arr2D = np.array([
[1,2],
[4,5],
[6,7]

])

# print(arr2D, arr2D.shape)
print(arr2D)
print(
    arr2D[0,0],arr2D[0,1]
)
print(
    arr2D[1,0],arr2D[1,1]
)
print(
    arr2D[2,0],arr2D[2,1]
)



# arr3D = np.array([
#     [
#         [1,2,3],
#         [5,6,7],
#         [3,4,5]
#     ],
#     [
#         [1,2,3],
#         [5,6,7],
#         [3,4,5]
#     ],
#     [
#         [1,2,3],
#         [5,6,7],
#         [3,4,5]
#     ]
# ])

# print(arr3D)
# print(arr3D[0])
# print(arr3D[0,0])
# print(arr3D[0,0,0])




arr2D = np.array([
[1,2],
[4,5],
[6,7]

])
arr2D[0]=[7,15]
print(arr2D)

zeros = np.zeros((4,5))
print(zeros)
print(type(zeros))
ones = np.ones((3,))
print(ones)


consts = np.full((3,3,),9) 
print(consts)

rand =np.random.random((4,4))
print(rand)



























