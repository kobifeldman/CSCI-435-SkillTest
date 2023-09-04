# CSCI-435-SkillTest
A skill test at the beginning of CSCI 435: Software Engineering.

## Project Description
This tool recieves a set of corresponding XML and PNG files. The XML files describe the GUI components of an Android application. The PNG files are a screenshot of what that application looks like. The tool processes the files by drawing yellow dotted rectangles around each GUI element for the purpose of highlighting these elements and making them easy to see and distinguish from eachother. The resulting images are output into the output folder.

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

## Credits