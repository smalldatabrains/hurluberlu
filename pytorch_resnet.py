import torch
from torch import nn as nn
from torch.utils.data import DataLoader, Dataset
import torch.optim as optim
import torchvision.transforms as transforms
import torchvision

# CIFAR dataset import

transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Resize([264,264])
])

dataset = torchvision.datasets.CIFAR100 (
    root ='./data',
    train = True,
    download = True,
    transform = transform
)

dataloader = DataLoader(dataset, batch_size = 64, shuffle = True)

class SolidBloc(nn.Module):
    def __init__(self, in_channels, out_channels, stride):
        super().__init__()
        self.conv1 = nn.Conv2d(in_channels=in_channels, out_channels=out_channels, kernel_size=7, stride=stride)
        self.conv2 = nn.Conv2d(in_channels=in_channels, out_channels=out_channels, kernel_size=3, stride=2)
        self.relu = nn.ReLU()
        self.skip_connection = nn.Sequential()
        if stride!=1:
            self.skip_connection = nn.Sequential(
                nn.Conv2d(in_channels=in_channels, out_channels=out_channels, kernel_size=3, stride=2)
            )

    def forward(self, x):
        x = self.conv1(x)
        x = self.relu(x)
        x = self.conv1(x)
        x = x + self.skip_connection(x)

        return x
    
class ResNet(nn.Module):
    def __init__(self):
        super().__init__()
        self.name = 'Resnet'
        self.sequence_list = [64, 128, 256, 512]
        self.model = nn.ModuleList

    def forward(x):
        pass

if __name__=='__main__':
    # model

    # Loss criterion
    criterion = nn.CrossEntropyLoss()
    # Optimizer
    optimizer = optim.Adam()
    # Epochs
    epochs = 10
    # Use dataloader
    for epoch in range(epochs):
        pass