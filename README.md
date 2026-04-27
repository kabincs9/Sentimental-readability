# 📖 Readability - Grade Level Analyzer

![Python](https://img.shields.io/badge/Language-Python-blue.svg)
![CS50x](https://img.shields.io/badge/CS50x-Week%206-orange.svg)
![Text Analysis](https://img.shields.io/badge/Text%20Analysis-Readability-brightgreen.svg)

A clean Python program that analyzes any English text and tells you the **U.S. school grade level** needed to understand it.

# ✨ Overview

This program uses the **Coleman-Liau Index** to calculate the readability of a text. It counts letters, words, and sentences, then outputs the approximate grade level required to comfortably read the text.

Great for writers, teachers, and anyone who wants to check how complex their writing is.

## 🎯 Features

- ✅ Accurately counts **letters**, **words**, and **sentences**
- ✅ Implements the Coleman-Liau readability formula:
index = 0.0588 * L - 0.296 * S - 15.8
text- ✅ Handles punctuation, spaces, and multiple sentences properly
- ✅ Clear and professional output:
- "Before Grade 1"
- "Grade X" (for grades 1–16)
- "Grade 16+" (college level or higher)
- ✅ Simple and user-friendly interface

## 🚀 Quick Start

```bash
# Clone the repository
git clone https://github.com/kabincs9/readability.git
cd readability

# Run the program
python readability.py
Then paste any English text when prompted.
📊 Example
Input:
textWhen he was nearly thirteen, my brother Jem got his arm badly broken at the elbow.
Output:
textGrade 7
Another Example:
textIt is a truth universally acknowledged, that a single man in possession of a good fortune, must be in want of a wife.
Output:
textGrade 12
🧠 What I Learned

Text processing and character analysis in Python
Counting letters, words, and sentences accurately
Implementing mathematical formulas
Floating-point calculations and rounding
Conditional logic for different grade outputs

🛠️ Built With

Python 3
Standard libraries only (string module optional)
