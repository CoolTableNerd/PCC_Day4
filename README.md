# PCC Day 4

### Python Conditionals (Chapter 5)

---

#### **Summary**  
Conditional statements (`if`, `elif`, `else`) allow programs to make decisions based on Boolean logic (`True`/`False`). Key concepts include:  
- **Operators**: Equality (`==`), inequality (`!=`), and numerical comparisons (`<`, `>`, `<=`, `>=`).  
- **Logical Operators**: `and` (both conditions true), `or` (at least one condition true).  
- **Membership Checks**: `in` (value exists in a list), `not in` (value absent from a list).  
- **Case Sensitivity**: Strings are case-sensitive (use `.lower()` or `.upper()` for case-insensitive checks).  
- **Boolean Flags**: Track state with `True`/`False` values.  

---

### **Key Concepts**  
#### 1. **Basic `if` Statements**  
- Check equality with `==`:  
  ```python
  sneaker = "vomeros"
  if sneaker == "vomeros":
      print("Correct sneaker!")
  ```  
- **Case Sensitivity**:  
  ```python
  coat = "North Face"
  if coat.lower() == "north face":  # Case-insensitive check
      print("Match found.")
  ```

#### 2. **Inequality Checks**  
- Use `!=` for "not equal":  
  ```python
  banned_user = "Logan"
  if banned_user != "Tyson":
      print("Access granted.")
  ```

#### 3. **Numerical Comparisons**  
- Compare numbers with `<`, `>`, `<=`, `>=`:  
  ```python
  age = 18
  if age >= 21:
      print("Allowed.")
  else:
      print("Denied.")
  ```

#### 4. **Logical Operators**  
- `and` (both conditions must be true):  
  ```python
  if (age >= 13) and (age <= 19):
      print("Teenager.")
  ```  
- `or` (at least one condition true):  
  ```python
  if (day == "Saturday") or (day == "Sunday"):
      print("Weekend!")
  ```

#### 5. **List Membership**  
- Check if a value exists in a list with `in`/`not in`:  
  ```python
  usernames = ["CoolTableNerd", "PythonPro"]
  if "Guest" not in usernames:
      print("Username available.")
  ```

#### 6. **Boolean Flags**  
- Track program state:  
  ```python
  game_active = True
  if game_active:
      print("Game is running.")
  ```

#### 7. **`if-elif-else` Chains**  
- Test multiple conditions in order:  
  ```python
  score = 85
  if score >= 90:
      print("A")
  elif score >= 80:
      print("B")
  else:
      print("C")
  ```

---

### **Project: User Registration System**  
Build a program that validates user registrations using conditional checks.  

#### **Requirements**  
1. **Username Validation**:  
   - Check if a username is already taken (case-insensitive).  
   - Ensure it’s not in a banned list (e.g., `["admin", "root"]`).  

2. **Age Verification**:  
   - Deny registration if under 13.  
   - Flag users aged 13–18 as minors.  

3. **Admin Role**:  
   - Allow only users with a secret code (`"2024Admin"`) to register as admins.  

4. **Output**:  
   ```python
   Username: "CoolTableNerd" → "Username taken."
   Age: 12 → "Registration denied. Minimum age: 13."
   ```

#### **Steps**  
1. Define lists: `existing_users`, `banned_users`.  
2. Use `input()` to collect username, age, and admin code.  
3. Implement checks using `if`/`elif`/`else` and logical operators.  

---

### **Trivia Questions**  
1. What operator checks if two values are equal, and how is it written?  
2. Why does `"Python" == "python"` return `False`, and how can you fix it?  
3. What is the difference between `and` and `or` in a conditional statement?  
4. Write a condition to check if a number is between 10 and 20 (inclusive).  
5. How would you check if the name `"Alice"` is **not** in a list called `guests`?  
6. What keyword stops an `if-elif-else` chain once a condition is met?  
7. What does `if not game_over:` imply if `game_over` is a Boolean?  