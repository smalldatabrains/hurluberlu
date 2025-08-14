from torch import nn
import torch

class Classifier(nn.Module)
    def __init__(self):
        super(Classifier, self).__init__()
        self.classifier = nn.Sequential(
            nn.Linear(4,1),
            nn.Sigmoid()
    )

def forward(self,x):
    x = self.classifier(x)
    return x

model = Classifier()
linear_layer = model.classifier[0]

print("Weight", linear_layer.weight)
print("Bias", linear_layer.bias)
tensor = torch.rand([2,4])

print(tensor)

print(tensor.dtype)
print(tensor.shape)
print(tensor.device)

output = model.forward(tensor)

print(output.dtype)
print(output.shape)
print(output.device)

print(output)
