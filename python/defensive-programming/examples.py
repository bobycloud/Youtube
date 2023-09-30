# EAFP: Easier to Ask Forgiveness Than Permission
# LBYL: Look Before You Leap


# Example 1: Input Validation
user_input = input("Enter a number: ")
try:
    num = int(user_input)
except ValueError:
    print("Invalid input: Please enter a valid number.")


# Example 2: Index checking
my_list = [1, 2, 3]
index = 5
if 0 <= index < len(my_list):
    item = my_list[index]
else:
    print("Index out of range.")


# Example 3: File Existence
import os

file_path = "data.txt"
if os.path.exists(file_path):
    with open(file_path, "r") as file:
        data = file.read()
else:
    print("File not found.")


# Example 4: Key Existence in Dictionary
my_dict = {"key1": "value1", "key2": "value2"}
key = "key3"
if key in my_dict:
    value = my_dict[key]
else:
    print(f"Key '{key}' not found.")


# Example 5: Attribute Existence
class MyClass:
    def __init__(self, value):
        self.value = value


my_instance = MyClass(42)
if hasattr(my_instance, "value"):
    print(my_instance.value)
else:
    print("Attribute 'value' not found.")


# Example 6: Error Handling with try and except
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Error: {e}")
else:
    print("Execute if no exception")
finally:
    print("Always executed.")


# Example 7: Timeouts
import urllib.request
import socket

try:
    response = urllib.request.urlopen("http://example.com", timeout=5)
except (urllib.error.URLError, socket.timeout) as e:
    print(f"Error: {e}")


# Example 8: Concurrency Issues
import threading

lock = threading.Lock()

def update_shared_variable():
    with lock:
        # Code to update shared variable
        pass


# Example 9: Recursion depth check to avoid stack overflow / maximum recursion depth exceeded
import sys

def factorial(n):
    if n < sys.getrecursionlimit():
        return n * factorial(n - 1)
    else:
        print("Recursion limit exceeded.")


# Example 10: Database connection / context manager
import sqlite3

conn = sqlite3.connect("mydb.db")
try:
    cursor = conn.cursor()
    # Database operations
finally:
    conn.close()


# Example 11: Graceful Degradation / Fallback
import requests

try:
    response = requests.get("https://api.example.com/data")
    data = response.json()
except (requests.ConnectionError, requests.Timeout):
    # Use cached data or provide a default response.
    pass


# Example 12: Memory Leak Detection
import tracemalloc

tracemalloc.start()
# Code with potential memory leaks
snapshot = tracemalloc.take_snapshot()
# Analyze snapshot for memory leaks
