# CSCI-435-SkillTest
A skill test at the beginning of CSCI 435: Software Engineering.

## Project Description
This tool recieves a set of corresponding XML and PNG files. The XML files describe the GUI components of an Android application. The PNG files are a screenshot of what that application looks like. The tool processes the files by drawing yellow dotted rectangles around each GUI element for the purpose of highlighting these elements and making them easy to see and distinguish from eachother. The resulting images are output into the output folder.

## Design Decisions
I started by reading in the input files and creating a folder for the output files if it does not exist. Then I wrote a function for parsing the XML files. I use Python's standard library for handling XML files. I created a depth first search recursive solution to traverse the tree like structure of the XML file. I start at the root, looking for "node" elements. Whenever I find one, I add its bounds to a collective list of all the coordinates which will be used to draw the rectangles. At each node in the tree, I search its children for other nodes, continuing down until I hit a dead end.

The rectangles are then drawn using the draw.py file. I chose to use OpenCV with Python as I had previously heard of it and it was the first thing that popped into my head when I read the project description and realized I would need a way to modify the images. I had limited knowledge of it so I started by reading the documentation and wrote a solution to draw rectangles at all of the previously gathered coordinates onto copies of the image files. I ran into a problem where the rectangles were made up of solid lines, these lines were harder to differentiate from the images themselves compared to the dotted lines shown in the example we were provided. After doing some research I found out that drawing dotted lines is not a feature of OpenCV and not knowing where to start with it, I used ChatGPT to generate some modifications to my drawing code to make the lines dotted.

## Compile and Run the tool
1. Clone the repository:
```
git clone https://github.com/kobifeldman/CSCI-435-SkillTest.git
```
2. Create a virtual environment:
```
python -m venv venv
```

3. Activate the virtual environment:  
Windows:
```
venv\Scripts\activate.bat
```

Unix/Mac:
```
source venv/bin/activate
```

4. Install the necessary libraries:
```
pip install -r requirements.txt
```

5. Run the program:
```
python main.py
```