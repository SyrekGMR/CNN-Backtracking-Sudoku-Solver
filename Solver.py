import Image
import Backtracking
import torch
import argparse

from torchvision import transforms
from torch import nn
import torch.nn.functional as F

#Parse arguments





# CNN Model for digit recognition

class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = nn.Conv2d(1, 32, 5, 1)
        self.conv2 = nn.Conv2d(32, 64, 5, 1)
        self.dropout1 = nn.Dropout2d(0.25)
        self.dropout2 = nn.Dropout2d(0.5)
        self.fc1 = nn.Linear(6400, 128)
        self.fc2 = nn.Linear(128, 10)

    def forward(self, x):
        x = self.conv1(x)
        x = F.relu(x)
        x = self.conv2(x)
        x = F.relu(x)
        x = F.max_pool2d(x, 2)
        x = self.dropout1(x)
        x = torch.flatten(x, 1)
        x = self.fc1(x)
        x = F.relu(x)
        x = self.dropout2(x)
        x = self.fc2(x)
        output = F.log_softmax(x, dim=1)
        return output

# Used below for removing grid lines from each digit cell in the Sudoku grid
def find_edges(pic, V=0):
    x_s, x_e, y_s, y_e = 0, 49, 0, 49
    #x_s
    v = pic[25, x_s]
    while v > V:
        x_s += 1
        v = pic[25, x_s]
    #x_e
    v = pic[25, x_e]
    while v > V:
        x_e -= 1
        v = pic[25, x_e]
        
    #y_s
    v = pic[y_s, 25]
    while v > V:
        y_s += 1
        v = pic[y_s, 25]
    
    #y_e
    v = pic[y_e, 25]
    while v > V:
        y_e -= 1
        v = pic[y_e, 25]
        

    return pic[y_s:y_e, x_s:x_e]

def subgrid(img, thresh=125):
    # Iterate over each of the subgrid within the 9x9 sudoky grid
    arr = []
    for y in range(9):
        in_arr = []
        for x in range(9):
            input_img = img[y*50:(y+1)*50, x*50:(x+1)*50]
            input_img = find_edges(input_img, V=0)
            if sum(input_img.flatten()) < 1000:
                pred = 0
            else:
                _, input_img = cv2.threshold(input_img, thresh, 255,cv2.THRESH_BINARY)
                input_img = trans(Image.fromarray(input_img)).reshape(1, 1, 28, 28)
                out = model.forward(input_img.to(device))
                pred = out.topk(1)[-1].item()
                
                # Uncomment to display each digit which is classified
                
                #plt.imshow(input_img.reshape(28, 28))
                #plt.show()
                
            in_arr.append(pred)
        arr.append(in_arr)

    return np.array(arr)

# Run
if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument('--cuda', type=bool, default=False, help="Use cuda")
    parser.add_argument('--image_path', type=str, help="Path to image")

    args = parser.parse_args()

    device = torch.device('cuda') if args.cuda else torch.device('cpu')

    #Load, Modify and Extract contours from image
    img = Image.load_image(args.image_path)
    img = Image.img_mod(img)
    img = Image.locate(img)

    model = Net().to(device)
    model.load_state_dict(torch.load("./cnn_weights.pth"))

    # Resize image for 81 equally size blocks
    img_n = cv2.resize(img_n, (450, 450))
    inner_box = int(img_n.shape[0]/9)

    #Freeze dropout layers
    model.eval()
    arr = []

    unsolved_grid = subgrid(img)

    #Backtracking
    Backtracking.backtracking(arr)