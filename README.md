

---

# **Supply Chain Optimization**

A comprehensive project to optimize supply chain logistics using data-driven methods. This repository includes a Flask-based API, a Power BI dashboard for visualizing cleaned data, and a Jupyter Notebook for detailed data exploration and preprocessing.

---

## **Features**
- **Flask App:** API for running optimization models, processing data, and interacting programmatically with supply chain datasets.
- **Jupyter Notebook:** Data cleaning, exploration, and preprocessing steps with Python and Pandas.
- **Power BI Dashboard:** An interactive visualization showcasing key metrics and insights from the cleaned data.
- **Docker Support:** Simplified deployment with a pre-configured Dockerfile.

---

## **Directory Structure**

```
SupplyChainOptimization/
├── app.py                     # Flask application for the backend API
├── Dockerfile                 # Docker configuration for containerized deployment
├── requirements.txt           # Python dependencies
├── data/
│   └── train.csv              # Raw dataset used in the project
├── dashboards/
│   └── supply_chain_dashboard.pbix  # Power BI dashboard file
├── notebooks/
│   └── Supply_Chain_Optimization.ipynb  # Jupyter Notebook for data cleaning and analysis
├── utils/
│   └── data_processing.py     # Utility functions for data preprocessing
├── optimization/
│   └── optimizer.py           # Core optimization logic using linear programming
```

---

## **Project Workflow**
1. **Data Cleaning and Exploration:**
   - Conducted in the Jupyter Notebook (`Supply_Chain_Optimization.ipynb`).
   - Cleaned missing values, standardized date formats, and calculated additional metrics such as shipping duration.

2. **Interactive Dashboard:**
   - Built using Power BI (`supply_chain_dashboard.pbix`) to provide insights into:
     - Order performance.
     - Shipping duration distribution.
     - Profit and sales trends.

3. **Optimization Logic:**
   - Implemented in `optimizer.py` using the `scipy.optimize` library to solve supply chain transportation problems.

4. **Flask API:**
   - API endpoints to:
     - Process data.
     - Solve optimization problems using input cost matrices, demand, and supply.

---

## **How to Run the Project**

### **1. Clone the Repository**
```bash
git clone https://github.com/YourUsername/SupplyChainOptimization.git
cd SupplyChainOptimization
```

### **2. Set Up the Environment**
#### **Install Dependencies**
Use `pip` to install Python dependencies:
```bash
pip install -r requirements.txt
```

#### **Run the Flask App**
```bash
python app.py
```
The app will be available at `http://127.0.0.1:5000`.

### **3. Explore the Notebook**
Open the Jupyter Notebook in a Jupyter-compatible environment:
```bash
jupyter notebook notebooks/Supply_Chain_Optimization.ipynb
```

### **4. View the Dashboard**
- Open `dashboards/supply_chain_dashboard.pbix` in Power BI Desktop.
- Interact with the visualizations to explore insights.

---

## **Docker Deployment**

1. **Build the Docker Image**
```bash
docker build -t supply-chain-optimization .
```

2. **Run the Docker Container**
```bash
docker run -p 5000:5000 supply-chain-optimization
```

---

## **API Endpoints**

### **1. Process Data**
**URL:** `/process_data`  
**Method:** `GET`  
**Description:** Processes and validates the dataset.  
**Response:** Column names of the processed dataset.

### **2. Optimize Transportation**
**URL:** `/optimize`  
**Method:** `POST`  
**Request Payload:** 
```json
{
  "costs": [[...], [...], [...]],
  "demand": [...],
  "supply": [...]
}
```
**Response:** Optimization solution with the allocation and cost details.

---

## **Technologies Used**
- **Backend:** Flask
- **Data Processing:** Python (Pandas, NumPy)
- **Optimization:** Scipy
- **Visualization:** Power BI
- **Deployment:** Docker

---

## **Screenshots**

### **Power BI Dashboard**
_(Add a screenshot of your Power BI dashboard for visual impact.)_

### **Flask API in Action**
_(Add sample API requests/responses screenshots or logs.)_

---

## **Future Enhancements**
- Add advanced optimization models (e.g., mixed-integer programming).
- Automate updates to the Power BI dashboard using APIs.
- Extend Flask API to include analytics endpoints.

---

## **Contributing**
Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch: `git checkout -b feature-name`.
3. Commit changes: `git commit -m "Added new feature"`.
4. Push to the branch: `git push origin feature-name`.
5. Submit a pull request.

---
