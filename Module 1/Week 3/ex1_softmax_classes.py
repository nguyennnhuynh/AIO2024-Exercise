import torch
import torch.nn as nn

class MySoftmax(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        x_exp = torch.exp(x)
        partition = x_exp.sum(0, keepdim=True)
        return x_exp / partition

class SoftmaxStable(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        x_max = torch.max(x, dim=0, keepdim=True).values
        x_exp = torch.exp(x - x_max)
        partition = x_exp.sum(0, keepdim=True)
        return x_exp / partition

# Ví dụ sử dụng
if __name__ == "__main__":
    data = torch.Tensor([1, 2, 3])

    # Sử dụng lớp MySoftmax
    my_softmax = MySoftmax()
    output = my_softmax(data)
    print("Output using MySoftmax:", output)  # tensor([0.0900, 0.2447, 0.6652])

    # Sử dụng lớp SoftmaxStable
    softmax_stable = SoftmaxStable()
    output_stable = softmax_stable(data)
    print("Output using SoftmaxStable:", output_stable)  # tensor([0.0900, 0.2447, 0.6652])
