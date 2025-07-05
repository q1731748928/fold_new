import torch
import numpy as np

# list_1 = [[[1, 2, 3, 4, 5, 6],
#          [1, 2, 3, 4, 5, 6],
#          [1, 2, 3, 4, 5, 6]]
#           ]
# print(list_1)
# print(np.array(list_1))
# print(torch.tensor(list_1))

# list_2 = [
#         [127, 128, 3, 4, 5, 6],
#          [1, 2, 3, 4, 5, 6],
#          [1, 2, 3, 4, 5, 6]
# ]
# t2 = torch.tensor(list_2, dtype=torch.int8) # [-128-127]
# print(t2)

# list_2 = [
#         [127, 128, 3, 4, 5, 6],
#          [1, 2, 3, 4, 5, 6],
#          [1, 2, 3, 4, 5, 6]
# ]
# t2 = torch.tensor(list_2, requires_grad=True) # [-128-127]
# print(t2.double().dtype)

# list_3 = [
#         [127, 128, 3, 4, 5, 6],
#          [1, 2, 3, 4, 5, 6],
#          [1, 2, 3, 4, 5, 6]
# ]
# t3 = torch.tensor(list_3) # [-128-127]
# print(t3.shape)
# print(t3.size())list_3 = [
#         [127, 128, 3, 4, 5, 6],
#          [1, 2, 3, 4, 5, 6],
#          [1, 2, 3, 4, 5, 6]
# ]
# t3 = torch.tensor(list_3) # [-128-127]
# print(t3.shape)
# print(t3.size())

# t4 = torch.empty(2, 2, 3)
# t4 = torch.ones(2, 2, 3)
# t4 = torch.randint(low=100, high=1000, size=(2, 3, 4))
# t4 = torch.FloatTensor(2, 3, 4)
# print(t4)

# t5 = torch.randint(low=100, high=1000, size=(2, 3, 4))
# print(t5.numpy())
# t6 = torch.tensor([[[[[100]]]]])
# print(t6.item())

# list_7 = [[119, 139, 223, 612],
#          [712, 640, 798, 271],
#          [854, 268, 821, 589]]
# t7 = torch.tensor(list_7)
# print(t7.max(dim=0))

# list_8 = [[[119, 139, 223, 612],
#          [712, 640, 798, 271],
#          [854, 268, 821, 589]],
#         [[553, 531, 464, 231],
#          [315, 653, 741, 772],
#          [397, 396, 365, 762]]
#           ]
# t8 = torch.tensor(list_8)
# print(t8.max(dim=2).values)

# list_8 = [[[119, 139, 223, 612],
#          [712, 640, 798, 271],
#          [854, 268, 821, 589]],
#
#         [[553, 531, 464, 231],
#          [315, 653, 741, 772],
#          [397, 396, 365, 762]]
#           ]
# t8 = torch.tensor(list_8)
# print(t8.view(4, 5))

# view
# list_9 = [[119, 139, 223, 612],
#          [712, 640, 798, 271]]
# t9 = torch.tensor(list_9)
# print(t9.size())

# print(t9.permute(1, 0)) # 轴交换

# t10 = torch.randint(low=100, high=1000, size=(2, 3, 4))
# print(t10.permute(1, 0, 2).size())

# list_10 = [[[119, 139, 223, 612],
#          [712, 640, 798, 271],
#          [854, 268, 821, 589]],
#
#         [[553, 531, 464, 231],
#          [315, 653, 741, 772],
#          [397, 396, 365, 762]]
#           ]
# t10 = torch.tensor(list_10)
# print(t10.view(4, 6))

list_10 = [[[119, 139, 223, 612],
         [712, 640, 798, 271],
         [854, 268, 821, 589]],

        [[553, 531, 464, 231],
         [315, 653, 741, 772],
         [397, 396, 365, 762]]
          ]
t10 = torch.tensor(list_10)
# print(t10[1:, 2:, 3].item())

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')


