from torch import nn
import torch

from torch.utils.data import DataLoader, Dataset

class CustomDataset(Dataset):
    def __init__(self, input, label, transform=None, target_transform=None):
        self.input=input
        self.label=label

    def __len__(self):
        return len(self.label)

    def __getitem__(self, index):
        item = 'hello'
        return item


class Classifier(nn.Module)
    def __init__(self):
        super(Classifier, self).__init__()
        self.classifier = nn.Sequential(
            nn.Linear(10,5),
            nn.Sigmoid(),
            nn.Linear(5,1),
            nn.Sigmoid()
    )

def forward(self,x):
    x = self.classifier(x)
    return x

model = Classifier()
linear_layer = model.classifier[0]

print("Weight", linear_layer.weight)
print("Bias", linear_layer.bias)
input = torch.rand([1000,10]) #1000 examples (N), 4 features (F)
label = torch.rand([1000,1])

print("There are",len(label),"examples in the dataset")

print(input)

print(input.dtype)
print(input.shape)
print(input.device)

output = model.(input)

print(output.dtype)
print(output.shape)
print(output.device)

print(output)
