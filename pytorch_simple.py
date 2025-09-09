from torch import nn    
import torch
from matplotlib import pyplot as plt    
import numpy as np  

tensor = torch.tensor([1,1][2,2],[-1,1.1],[4,3.8],[10,10.3]).float()
x=tensor[:,0].view(-1,1)
y=tensor[:,1].view(-1,1)
print(tensor)
print(tensor.shape)
print(tensor.dtype)
print(x.shape)
print(y.shape)


result=nn.Softmax(y)
print(result)

plt.scatter(x,y,color='blue', label='Real data')

class LinearModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.regressor = nn.Sequential(nn.Linear(1,1)) #expect [batch_size, features]

    def forward(self,x):
        return self.regressor(x)

model = LinearModel()
criterion = MSELoss()
optimizer = torch.optim.SGD(model.parameters(),lr=0.01)

for epoch in range(50):
    y_pred = model(x)
    print(y_pred)
    loss = criterion(y_pred,y)
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
    print(f"Epoch {epoch}: loss{loss.item():.4f}")
    line_color = np.random.rand(3,)
    plt.scatter(x, y_pred.detach().numpy(), color=line_color, label='Prediction')

plt.show()
