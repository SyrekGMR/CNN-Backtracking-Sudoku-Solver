# CNN-Backtracking-Sudoku-Solver
<p align="center">
  <img src="Images/sudoku.png" />
</p>
<br>

<p align="center">
<h2>
  CNN-based digit detector followed by a backtracking algorithm.
</h2>
</p>
<br>
Taking a screenshot of a sudoku board, the CV2 provides us with various methods for extracting the sudoku grid from the image.
<br>
<p align="center">
  <img src="Sudoku_Grids/Grid1.PNG" />
</p>
Image modification such as convering the RGB image to Grayscale are applied to make contours and digits more distinct allowing for easier detection and classification.
<br>
<p align="center">
  <img src="Sudoku_Grids/Contour_Cut.png" />
</p>
<br>

A small CNN with ~800k parameters is trained on the MNIST digit classification dataset for use in identifying the digits in each subgrid seen above.
The sudoku grid is split into 81 such subgrids which are then iterated over, resized to 28x28, to match the network configuration, and propagated through the network to identify the digit within each subgrid. At each step the sum of all pixel values within each cropped image is taken to identify empty subgrid which are labelled as 0 to be filled in by the backtracking algorithm next.

<br>
<p align="center">
  <img src="Images/1.png" />
  <img src="Images/2.png" />
  <img src="Images/3.png" />
  <img src="Images/4.png" />
  <img src="Images/5.png" />
  <img src="Images/6.png" />
  <img src="Images/7.png" />
  <img src="Images/8.png" />
  <img src="Images/9.png" />
</p>
<br>

Finally, with the scanned sudoku grid this is then fed into the backtracking algorithm, widely used in constraint satisfaction problems such as this one where there exist numerous conditions on the validity of a number within each subgrid. The algorithm proceeds to iterate over each possible candidate where in the case of exhausting all possible candidates it moves backwards and modifies the previous candidates.
<p align="center">
[[2 8 4 1 7 5 9 6 3]
  <br>
 [3 6 9 8 4 2 5 7 1]
  <br>
 [1 5 7 9 6 3 8 2 4]
  <br>
 [5 3 1 7 2 4 6 8 9]
  <br>
 [9 2 6 3 8 1 7 4 5]
  <br>
 [4 7 8 6 5 9 3 1 2]
  <br>
 [7 9 5 4 1 8 2 3 6]
  <br>
 [6 1 3 2 9 7 4 5 8]
  <br>
 [8 4 2 5 3 6 1 9 7]]
 </p>
