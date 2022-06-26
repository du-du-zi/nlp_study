import torch
torch.device('cuda' if torch.cuda.is_available() else 'cpu')