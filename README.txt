Name: Robert McCurdy
Class: CSCI 361
Assignment 2

Brief Overview of the Program :

This program will randomly generate two arrays both of size 5. After randomly generating these arrays, two threads are created. The first thread "t1" will call the function
addVectors and pass the argument "x" which is the first randomized array. The second thread "t2" is the exact same except it calls the function subVectors and passes the argument "y" which
is the second randomized array. We then .start() these threads, they will start their functions, and then we call .join() to join them together to print our results.

Overview of addVectors, subVectors, and the randomized arrays :

Numpy was used for both the addVectors method and the subVectors method. It was also used for the randomized arrays(vectors). The addVectors and subVectors method pass in
two variables as the arguments. In theory, these can be anything but in our case they will be the two vectors we pass in. It then prints the original vectors before the addition function,
we then call the .add() function from numpy. This will do vector addition to add the two vectors (arrays) together into one vector. We then print that vector. The subVectors method is basically
the same exact thing except we call the .subtract() method instead of the .add() method. The randomized vectors(arrays) are created using numpy as well but with the random import. The vector
is created by calling random.randint() which passes in two parameters when we're using numpy's random module. The two arguments are the range and size. The range will define what numbers
can be inserted into each of the vector's indexes. So an individual number in the vector could range anywhere from 0 to the number inputted for the range argument. The size just determines how
many numbers will be in the vector.