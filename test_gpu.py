import torch
import torch_directml

device = torch_directml.device()

print(f"DirectML Device: {device}")
print(f"Is DirectML available: {torch_directml.is_available()}")

x = torch.tensor([1.0, 2.0]).to(device)
print(f"Tensor is successfully on: {x.device}")