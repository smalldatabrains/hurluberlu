import torch
from torch import nn as nn
from torch.utils.data import DataLoader, Dataset
import torch.optim as optim
import torchvision.transforms as transforms
import torchvision
from torch.utils.tensorboard import SummaryWriter
from tqdm import tqdm

# CIFAR dataset import

transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Resize([224,224]), # size from paper
    transforms.Normalize((0.5,0.5,0.5),(0.5,0.5,0.5))
    
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
        # skip connection
        if stride != 1 or in_channels != out_channels:
            self.skip_connection = nn.Conv2d(in_channels=in_channels, out_channels=out_channels, kernel_size=1, stride=stride)
        else:
            self.skip_connection = None
        self.conv1 = nn.Conv2d(in_channels=in_channels, out_channels=out_channels, kernel_size=3, stride=stride, padding=1) # padding to keep image dimension
        self.conv2 = nn.Conv2d(in_channels=out_channels, out_channels=out_channels, kernel_size=3, stride=1, padding=1)
        self.relu = nn.ReLU()
        self.batch_norm1 = nn.BatchNorm2d(out_channels)
        self.batch_norm2 = nn.BatchNorm2d(out_channels)

    def forward(self, x):
        identity = x
        if self.skip_connection is not None:
            identity = self.skip_connection(identity) # in first block [64, 64, 112, 112]
        # print("Identity shape", identity.shape)
        x = self.conv1(x)
        x = self.batch_norm1(x)
        # print("X shape", x.shape)
        x = self.relu(x)
        # print("X shape", x.shape)
        x = self.conv2(x)
        x = self.batch_norm2(x)
        # print("X shape", x.shape)
        x = x + identity
        x = self.relu(x)

        return x
    
class ResNet(nn.Module):
    def __init__(self):
        super().__init__()
        self.name = 'Resnet'
        self.first_conv = nn.Conv2d(in_channels=3, out_channels=64, kernel_size=7, stride=2, padding=3) # padding to keep image dimension
        self.avgpool = nn.AdaptiveAvgPool2d((1,1))
        self.fc = nn.Linear(512, 100) # 100 classes for CIFAR100
        self.first_block = nn.Sequential (
            SolidBlock(in_channels=64, out_channels=64, stride=1),
            SolidBlock(in_channels=64, out_channels=64, stride=1),
            SolidBlock(in_channels=64, out_channels=64, stride=1)
        )
        
        self.second_block = nn.Sequential (
            SolidBlock(in_channels=64, out_channels=128, stride=2),
            SolidBlock(in_channels=128, out_channels=128, stride=1),
            SolidBlock(in_channels=128, out_channels=128, stride=1),
            SolidBlock(in_channels=128, out_channels=128, stride=1),
        )

        self.third_block = nn.Sequential (
            SolidBlock(in_channels=128, out_channels=256, stride=2),
            SolidBlock(in_channels=256, out_channels=256, stride=1),
            SolidBlock(in_channels=256, out_channels=256, stride=1),
            SolidBlock(in_channels=256, out_channels=256, stride=1),
            SolidBlock(in_channels=256, out_channels=256, stride=1),
            SolidBlock(in_channels=256, out_channels=256, stride=1),
        )

        self.forth_block = nn.Sequential (
            SolidBlock(in_channels=256, out_channels=512, stride=2),
            SolidBlock(in_channels=512, out_channels=512, stride=1),
            SolidBlock(in_channels=512, out_channels=512, stride=1)
        )

    def forward(self,x):
        x = self.first_conv(x)
        x = nn.MaxPool2d(kernel_size=(2,2))(x)
        x = self.first_block(x)
        x = self.second_block(x)
        x = self.third_block(x)
        x = self.forth_block(x)

        x = self.avgpool(x)
        x = torch.flatten(x, 1) #flatten 512 long vector

        x = self.fc(x)

        return x

if __name__=='__main__':
    # tensorboard writer
    writer = SummaryWriter()
    # device
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(device)
    # model
    model = ResNet().to(device)
    model.train()
    # Loss criterion
    criterion = nn.CrossEntropyLoss()
    # Optimizer
    optimizer = optim.Adam(model.parameters(),lr=0.001)
    # Epochs
    epochs = 20
    # Use dataloader
    for epoch in range(epochs):
        train_loss = 0
        for batch_idx, (images, labels) in enumerate(dataloader):
            images, labels = images.to(device), labels.to(device)
            prediction = model(images)
            loss = criterion(prediction, labels)
            optimizer.zero_grad() #reinitialize the gradient for next batch
            loss.backward()
            optimizer.step()
            train_loss += loss.item()
            print(f"Batch {batch_idx}/{len(dataloader)}")
            print(f"Batch loss {loss}")
            print(f"Trained {(batch_idx)*len(labels)} images in Epoch {epoch} with total loss {train_loss}")
            writer.add_scalar('Loss/train', loss.item(), batch_idx)
        writer.add_scalar('Loss/epoch', train_loss/len(dataloader), epoch)
        print(f"Epoch {epoch} has average loss of {train_loss/len(dataloader)}")
        PATH = f"./saved_model/CIFAR_MODEL_epoch_{epoch}.pth"
        torch.save(model.state_dict(), PATH)

# why bias = false is recommanded
# decaying learning rate to be implemented
