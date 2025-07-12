#!/usr/bin/env python3
"""
Script to generate LaTeX content files for Chapters 1-11
based on the actual Python files in each chapter folder.
"""

import os
import glob

def create_chapter_content(chapter_num, chapter_title, concepts, main_files, summary, key_takeaways):
    """Create a chapter content file with the given information."""
    
    content = f"""% Chapter {chapter_num} Content - {chapter_title}
% This file contains the content for Chapter {chapter_num} based on actual Python files

This document contains the essential keywords and definitions from Chapter {chapter_num} of "Python Crash Course" along with their corresponding code examples.

"""
    
    # Add concepts
    for i, (concept, definition, example_file) in enumerate(concepts, 1):
        content += f"\\subsection*{{{i}. {concept}}}\n"
        content += f"\\textbf{{Definition}}: {definition}\n\n"
        
        if example_file:
            content += f"\\lstinputlisting[language=Python, caption={concept.lower()}]{example_file}\n\n"
        else:
            content += f"\\begin{{lstlisting}}\n# Example code for {concept.lower()}\n\\end{{lstlisting}}\n\n"
    
    # Add practical examples section
    content += f"\\section*{{Practical Examples from Chapter {chapter_num}}}\n\n"
    content += f"\\subsection*{{Working with {chapter_title}}}\n"
    content += f"Chapter {chapter_num} introduces {chapter_title.lower()}. Here are the key files:\n\n"
    
    for file_desc, file_path in main_files:
        content += f"\\textbf{{{file_desc}}}:\\n"
        content += f"\\lstinputlisting[language=Python, caption={file_path}]{{{file_path}}}\\n\\n"
    
    content += "\\textbf{To run these programs:}\\n"
    content += "\\begin{verbatim}\\n"
    for _, file_path in main_files:
        content += f"python {file_path}\\n"
    content += "\\end{verbatim}\\n\n"
    
    # Add summary and key takeaways
    content += f"\\section*{{Summary}}\n{summary}\n\n"
    content += "\\section*{Key Takeaways}\\n"
    content += "\\begin{itemize}\\n"
    for takeaway in key_takeaways:
        content += f"    \\item {takeaway}\\n"
    content += "\\end{itemize}\\n"
    
    return content

# Chapter 4 content
chapter4_concepts = [
    ("for Loop - Iterating Through Lists", "A loop that runs once for each item in a list or other collection.", "Chapter04/401_magicians.py"),
    ("Loop Variable - Current Item", "The variable that holds the current item being processed in a loop.", None),
    ("Indentation - Code Blocking", "The use of spaces or tabs to indicate which lines of code belong together in a block.", None),
    ("range() Function - Number Sequences", "A function that generates a sequence of numbers for use in loops.", "Chapter04/402_first_numbers.py"),
    ("List Comprehension - Compact Lists", "A way to create lists using a compact syntax with loops and conditions.", "Chapter04/404_squares.py"),
    ("Slicing - List Portions", "A way to work with a portion of a list by specifying start and end indices.", None),
    ("Copying Lists - Creating Duplicates", "Creating a copy of a list to avoid modifying the original.", None),
]

chapter4_files = [
    ("Basic Loops", "Chapter04/401_magicians.py"),
    ("Number Sequences", "Chapter04/402_first_numbers.py"),
    ("List Comprehensions", "Chapter04/404_squares.py"),
]

chapter4_summary = "Chapter 4 focuses on working with lists using loops. You learn how to iterate through lists, use the range() function, and create list comprehensions for more efficient code."

chapter4_takeaways = [
    "for loops iterate through each item in a list",
    "Use proper indentation to define loop blocks",
    "range() generates sequences of numbers",
    "List comprehensions create lists efficiently",
    "Slicing allows you to work with portions of lists",
    "Copy lists to avoid modifying originals"
]

# Generate Chapter 4 content
chapter4_content = create_chapter_content(4, "Working with Lists", chapter4_concepts, chapter4_files, chapter4_summary, chapter4_takeaways)

with open("chapter4_content.tex", "w") as f:
    f.write(chapter4_content)

print("Generated chapter4_content.tex")

# Continue with other chapters...
# (I'll create a more comprehensive script for all chapters) 