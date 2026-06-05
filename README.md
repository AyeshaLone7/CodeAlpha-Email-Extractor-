📧 Email Extractor – Task Automation with Python

-Project Overview

Email Extractor is a Python-based automation script designed to extract email addresses from text files automatically. The program scans a user-provided file, identifies valid email addresses using regular expressions, removes duplicates, generates a summary report, and saves the results into a separate file. A backup copy of the generated file is also created for additional safety.

This project demonstrates how Python can be used to automate repetitive real-world tasks efficiently.

---

- Objective

The primary objective of this project is to automate the process of extracting email addresses from text files. Instead of manually searching and collecting email addresses, the script performs the task automatically, saving both time and effort.

---

- Project Files
The project consists of the following files:

1.email-extractor.py → Main Python script responsible for extracting email addresses.
2.data-1.txt → Input file containing raw text data and email addresses.
3.backup_result.txt → Output file where the extracted email addresses and report are stored.

---

- Key Features

- Reads data from a user-specified text file.
- Detects and extracts valid email addresses.
- Removes duplicate email entries.
- Sorts extracted emails for better organization.
- Generates a detailed extraction report.
- Saves results to a new output file.
- Creates an automatic backup of the output file.
- Provides a simple and user-friendly interface.

---

- Technologies and Concepts Used

- Python Programming
- Regular Expressions ("re")
- File Handling
- OS Module ("os")
- File Operations with "shutil"
- Lists and Sets
- Loops and Conditional Statements

---

⚙ Working Procedure

1. File Selection

The user enters the name of the text file containing the required data.

2. File Validation

The program checks whether the specified file exists before processing it.

3. Email Extraction

A regular expression pattern is used to identify and extract all valid email addresses from the file.

4. Duplicate Removal

Duplicate email addresses are removed to ensure that only unique records are stored.

5. Report Generation

The script generates a summary report showing:

- Total emails found
- Unique emails extracted
- Duplicate entries removed

6. Saving Results

All extracted email addresses are saved to a user-defined output file.

7. Backup Creation

A backup copy of the output file is automatically generated for data protection.

---

🌍 Real-World Applications

- Contact information management
- Data cleaning and preprocessing
- Email list organization
- Marketing and outreach campaigns
- Record maintenance and analysis

---

📚 Learning Outcomes

This project helped strengthen understanding of:

- File handling in Python
- Regular expressions for pattern matching
- Task automation techniques
- Data processing and organization
- Practical use of Python modules

---

🚀 Future Improvements

Potential enhancements for future versions include:

- Exporting results to CSV format
- GUI-based interface using Tkinter
- Support for multiple file formats
- Automatic folder scanning
- Advanced email validation techniques

---

📌 Conclusion

The Email Extractor project is a practical example of task automation using Python. By combining file handling, regular expressions, and automation techniques, the program efficiently extracts, organizes, and stores email addresses while minimizing manual work and improving productivity.

---

👩‍💻 Author

Ayesha Abdul Aziz

A passionate technology enthusiast with a growing interest in Artificial Intelligence, Hardware Engineering, and Embedded Systems. Dedicated to developing practical software solutions, exploring automation techniques, and continuously improving programming skills through hands-on projects and real-world applications.

This project was developed as part of the learning journey to strengthen Python programming, automation, and problem-solving skills.
