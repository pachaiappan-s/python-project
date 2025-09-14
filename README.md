
# BMI Calculator

## 📌 Purpose
This project is a simple **BMI (Body Mass Index) Calculator** written in Python.  
It takes the user's **height (in cm)** and **weight (in kg)**, then calculates the BMI and classifies the result.

---

## ⚙️ How It Works
1. **User Input**  
   - Height in centimeters  
   - Weight in kilograms  

2. **Conversion**  
   - Height is converted to meters (`height_m = height_cm / 100`).  

3. **BMI Formula**  
   ```
   BMI = weight / (height_m ** 2)
   ```

4. **Output**  
   - Prints the BMI rounded to **two decimal places**.  
   - Displays the corresponding **weight category**.  

---

## 📊 BMI Categories
| BMI Range | Category               |
|-----------|------------------------|
| ≤ 16      | Severely underweight   |
| 16 – 18.5 | Underweight            |
| 18.5 – 25 | Normal weight          |
| 25 – 30   | Overweight             |
| > 30      | Obese                  |

---

## 💻 Example Run
**Input:**  
```
Enter your height in centimeters: 170
Enter your weight in kg: 65
```

**Output:**  
```
Your Body Mass Index is: 22.49
You are normal weight
```

---

## 📝 Notes
- If BMI is less than or equal to 0, the program asks the user to enter valid details.  
- This is a simple console-based program and can be extended with GUI or web app features.

---
