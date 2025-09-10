import torch
from torch import nn as nn
from torch.utils.data import DataLoader, Dataset
import torch.optim as optim
import torchvision.transforms as transforms
import torchvision

# CIFAR dataset import

transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Resize([224,224])
])

dataset = torchvision.datasets.CIFAR100 (
    root ='./data',
    train = True,
    download = True,
    transform = transform
)

dataloader = DataLoader(dataset, batch_size = 64, shuffle = True)

class SolidBlock(nn.Module):
    def __init__(self, in_channels, out_channels, stride):
        super().__init__()
        self.skip_connection = nn.Conv2d(in_channels=in_channels, out_channels=out_channels, kernel_size=1, stride=stride)
        self.conv2 = nn.Conv2d(in_channels=in_channels, out_channels=out_channels, kernel_size=3, stride=stride)
        self.relu = nn.ReLU()

    def forward(self, x):
        identity = self.skip_connection(x)
        print("Identity shape", identity.shape)
        x = self.conv2(x)
        print("X shape", x.shape)
        x = self.relu(x)
        print("X shape", x.shape)
        x = self.conv2(x)
        print("X shape", x.shape)
        x = x + identity
        x = self.relu(x)

        return x
    
class ResNet(nn.Module):
    def __init__(self):
        super().__init__()
        self.name = 'Resnet'
        self.first_conv = nn.Conv2d(in_channels=3, out_channels=64, kernel_size=7, stride=2)
        self.avgpool = nn.AdaptiveAvgPool2d((1,1))
        self.fc = nn.Linear(512, 100) # 100 classes for CIFAR CIFAR100

    def forward(x):
        x=SolidBlock()
        return x

if __name__=='__main__':
    # model
    model = ResNet()
    model.train()
    # Loss criterion
    criterion = nn.CrossEntropyLoss()
    # Optimizer
    optimizer = optim.Adam(model.parameters(),lr=0.001)
    # Epochs
    epochs = 1
    # Use dataloader
    for epoch in range(epochs):
        for image, label in dataloader:
            print(image)
            print(label)
