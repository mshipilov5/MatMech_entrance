# **Even Numbers Sorter**  

**Sorts even numbers in-place while keeping odd numbers in their original positions**  

This Python script takes an array of integers, sorts only the **even numbers** in ascending order using **insertion sort**, and leaves the odd numbers unchanged in their original positions.  

## **Features**  
- ✅ **In-place sorting** (modifies the original list)  
- ✅ **Preserves odd numbers** at their initial indices  
- ✅ **Efficient for small to medium datasets** (insertion sort is O(n²) but simple)  
- ✅ **Interactive input** (enter numbers line by line)  

## **Installation & Usage**  

### **1. Clone the Repository**  
```bash
git clone https://github.com/your-username/even-numbers-sorter.git
cd even-numbers-sorter
```

### **2. Run the Script**  
```bash
python main.py
```

### **3. Input Numbers**  
Enter numbers **one per line**. Press `Enter` on an empty line to sort.  

**Example:**  
```text
Enter numbers one by one (press Enter after each number):
When finished, press Enter on an empty line to process the sorting.
5
2
8
3
4

Original array: [5, 2, 8, 3, 4]
Array with even numbers sorted (odds remain in place): [5, 2, 4, 3, 8]
```

## **Dependencies**  
- Python 3.6+  

## **Possible Improvements**  
- [ ] Add support for file input (`input.txt` → `output.txt`)  
- [ ] Optimize sorting with a different algorithm (e.g., quicksort for evens)   

## **License**  
MIT © 2024 
