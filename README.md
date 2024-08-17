# Facial Recognition Attendance System

Overview
---------
This project is a facial recognition-based attendance system that uses Python and various libraries to identify individuals and record their attendance. The system leverages facial recognition technology to streamline and automate the attendance process.

Features
---------
- Facial Recognition: Identifies individuals using their facial features.
- Attendance Recording: Automatically records attendance based on recognized faces.
- Data Management: Manages and stores facial data and attendance records in a database.

Prerequisites
--------------
Before running the project, ensure you have the following installed:
- Python 3.6 or higher
- face_recognition library
- dlib library
- Other required dependencies (listed below)

Installation
-------------
1. Clone the Repository
   git clone https://github.com/yourusername/facial-recognition-attendance.git
   cd facial-recognition-attendance

2. Create a Virtual Environment (Optional but recommended)
   python -m venv venv
   source venv/bin/activate  # On Windows use venv\Scripts\activate

3. Install Required Packages
   pip install -r requirements.txt

   The requirements.txt file should include the necessary libraries:
   face_recognition
   dlib
   opencv-python
   numpy
   pandas

   If you encounter issues installing dlib, follow the specific instructions for your operating system in the dlib documentation (http://dlib.net/).

Usage
------
1. Add Data to the Database
   Use the AddDataToDatabase.py script to add new facial data to the database:
   python AddDataToDatabase.py

2. Run the Main Program
   Execute the main.py script to start the attendance system:
   python main.py

   The system will use facial recognition to identify individuals and record their attendance.

Files
------
- AddDataToDatabase.py: Script to add new facial data to the database.
- encoder.py: Contains functions for encoding facial features.
- main.py: Main script to run the attendance system.

Troubleshooting
---------------
- Issue with Installing dlib: Refer to the dlib installation guide (http://dlib.net/compile.html) for solutions.
- Face Recognition Accuracy: Ensure high-quality images and proper lighting conditions.

Contributing
-------------
Contributions are welcome! If you find any bugs or have improvements, please create a pull request or open an issue.

License
-------
This project is licensed under the MIT License - see the LICENSE file for details.

Contact
-------
For any questions or suggestions, feel free to contact me at visheshprajapati1234@gmail.com.
