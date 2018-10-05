import torch
import numpy as np

np_data = np.arange(6).reshape((2, 3))
torch_data = torch.from_numpy(np_data)
tensor2array = torch_data.numpy()
print(
    np_data,
    '\n',
    torch_data,
    '\n',
    tensor2array
)

data = [-1, -2, 1, 2]
tensor = torch.FloatTenser(data)
