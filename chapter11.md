# Chapter 11: Testing Your Code

## 1. Test - Code Verification

**Definition**: A piece of code that verifies that another piece of code works correctly.

```python
def test_first_last_name():
    """Do names like 'Janis Joplin' work?"""
    formatted_name = get_formatted_name('janis', 'joplin')
    assert formatted_name == 'Janis Joplin'
```

## 2. Unit Test - Function Testing

**Definition**: A test that verifies that one aspect of a function works correctly.

```python
# Unit testing with unittest
import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """Test for 'name_function.py'."""

    def test_first_last_name(self):
        """Do names like 'Janis Joplin' work?"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

    def test_first_last_middle_name(self):
        """Do names like 'Wolfgang Amadeus Mozart' work?"""
        formatted_name = get_formatted_name('wolfgang', 'mozart', 'amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')

if __name__ == '__main__':
    unittest.main()
```

## 3. Test Case - Test Class

**Definition**: A class that contains a series of unit tests that can be run together.

```python
class NamesTestCase(unittest.TestCase):
    """Tests for 'name_function.py'."""
    
    def test_first_last_name(self):
        """Do names like 'Janis Joplin' work?"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')
```

## 4. assertEqual() Method - Value Comparison

**Definition**: A method that verifies that a value you expect matches the value the function returns.

```python
formatted_name = get_formatted_name('janis', 'joplin')
self.assertEqual(formatted_name, 'Janis Joplin')
```

## 5. unittest Module - Testing Framework

**Definition**: A Python module that provides tools for testing your code.

```python
import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    def test_first_last_name(self):
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')
```

## 6. setUp() Method - Test Preparation

**Definition**: A method that runs before each test method, allowing you to create objects once and use them in all your test methods.

```python
def setUp(self):
    """Create a survey and a set of responses for use in all test methods."""
    question = "What language did you first learn to speak?"
    self.my_survey = AnonymousSurvey(question)
    self.responses = ['English', 'Spanish', 'Mandarin']
```

## 7. Test Function - Individual Test

**Definition**: A function that tests a specific aspect of your code.

```python
# Function to be tested
def get_formatted_name(first, last, middle=''):
    """Generate a neatly formatter full name"""
    if middle:
        full_name = f"{first} {middle} {last}"
    else:
        full_name = f"{first} {last}"
    return full_name.title()
```

## 8. assertIn() Method - Membership Test

**Definition**: A method that verifies that an item is in a list.

```python
def test_store_single_response(self):
    """Test that a single response is stored properly."""
    self.my_survey.store_response(self.responses[0])
    self.assertIn(self.responses[0], self.my_survey.responses)
```

## 9. assertNotIn() Method - Non-Membership Test

**Definition**: A method that verifies that an item is not in a list.

```python
def test_duplicate_responses(self):
    """Test that duplicate responses are not stored."""
    self.my_survey.store_response(self.responses[0])
    self.my_survey.store_response(self.responses[0])
    self.assertEqual(len(self.my_survey.responses), 1)
```

## 10. Test Runner - Test Execution

**Definition**: A tool that runs your tests and reports the results.

```python
if __name__ == '__main__':
    unittest.main()
```

## 11. Failing Test - Bug Detection

**Definition**: A test that fails, indicating that there's a problem with the code being tested.

```python
def test_first_last_middle_name(self):
    """Do names like 'Wolfgang Amadeus Mozart' work?"""
    formatted_name = get_formatted_name('wolfgang', 'mozart', 'amadeus')
    self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')
```

## 12. Passing Test - Success Verification

**Definition**: A test that passes, indicating that the code being tested works correctly.

```python
def test_first_last_name(self):
    """Do names like 'Janis Joplin' work?"""
    formatted_name = get_formatted_name('janis', 'joplin')
    self.assertEqual(formatted_name, 'Janis Joplin')
```

## 13. Test Coverage - Code Verification

**Definition**: The percentage of your code that's covered by tests.

```python
# Test different scenarios
def test_empty_string(self):
    """Test with empty strings."""
    result = get_formatted_name('', '')
    self.assertEqual(result, ' ')

def test_single_name(self):
    """Test with single name."""
    result = get_formatted_name('john', '')
    self.assertEqual(result, 'John ')
```

## 14. Integration Test - System Testing

**Definition**: A test that verifies that multiple parts of your system work together correctly.

```python
# Integration testing with user input
from survey import AnonymousSurvey

# Define a question and make a survey
question = "What language did you first learn to speak?"
my_survey = AnonymousSurvey(question)

# Show the question and store responses to the question
my_survey.show_question()
print("Enter 'q' at any time to quit.\n")

while True:
    response = input("Language: ")
    if response == 'q':
        break
    my_survey.store_response(response)

# Show the survey results
print("\nThank you to everyone who participated in the survey!")
my_survey.show_results()
```

## Practical Examples from Chapter 11

### Working with Testing

Chapter 11 introduces testing and test-driven development. Here are the key files:

**Function to be Tested:**
```python
# Chapter11/name_function.py
def get_formatted_name(first, last, middle=''):
    """Generate a neatly formatter full name"""
    if middle:
        full_name = f"{first} {middle} {last}"
    else:
        full_name = f"{first} {last}"
    return full_name.title()
```

**Unit Tests:**
```python
# Chapter11/test_name_function.py
import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """Test for 'name_function.py'."""

    def test_first_last_name(self):
        """Do names like 'Janis Joplin' work?"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

    def test_first_last_middle_name(self):
        """Do names like 'Wolfgang Amadeus Mozart' work?"""
        formatted_name = get_formatted_name('wolfgang', 'mozart', 'amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')

if __name__ == '__main__':
    unittest.main()
```

**Survey Class for Testing:**
```python
# Chapter11/survey.py
class AnonymousSurvey:
    """Collect anomymous answers to a surcey question."""

    def __init__(self, question):
        """Store a question, and prepare to store responses."""
        self.question = question
        self.responses = []

    def show_question(self):
        """Show the survey question."""
        print(self.question)

    def store_response(self, new_response):
        """Store a single response to the survey."""
        self.responses.append(new_response)

    def show_results(self):
        """Show all the responses that have been given."""
        print("Survey results:")
        for response in self.responses:
            print(f"- {response}")
```

**Test Survey Class:**
```python
# Chapter11/test_survey.py
import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """Tests for the class AnonymousSurvey."""

    def setUp(self):
        """Create a survey and a set of responses for use in all test methods."""
        question = "What language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English', 'Spanish', 'Mandarin']

    def test_store_single_response(self):
        """Test that a single response is stored properly."""
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)

    def test_store_three_responses(self):
        """Test that three individual responses are stored properly."""
        for response in self.responses:
            self.my_survey.store_response(response)

        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)

if __name__ == '__main__':
    unittest.main()
```

**Integration Testing:**
```python
# Chapter11/language_survey.py
from survey import AnonymousSurvey

# Define a question and make a survey
question = "What language did you first learn to speak?"
my_survey = AnonymousSurvey(question)

# Show the question and store responses to the question
my_survey.show_question()
print("Enter 'q' at any time to quit.\n")

while True:
    response = input("Language: ")
    if response == 'q':
        break
    my_survey.store_response(response)

# Show the survey results
print("\nThank you to everyone who participated in the survey!")
my_survey.show_results()
```

## Key Takeaways

- Tests verify code works correctly
- Unit tests check individual functions
- Test cases group related tests
- `assertEqual()` compares expected and actual values
- `unittest` provides testing framework
- `setUp()` prepares test data
- `assertIn()` checks list membership
- `assertNotIn()` checks non-membership
- Test runners execute tests
- Failing tests indicate bugs
- Passing tests verify correctness
- Test coverage measures completeness
- Integration tests check system parts
- Write tests before fixing bugs
- Tests help prevent regressions 