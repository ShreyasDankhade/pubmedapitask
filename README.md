# **PubMed Research Paper Fetcher**

Fetch research papers from PubMed API and filter authors affiliated with pharmaceutical/biotech companies.

---

## **📌 Features**
✅ Fetches research papers using **PubMed API**  
✅ Filters authors affiliated with **pharma/biotech companies**  
✅ Saves results as **CSV file**  
✅ Supports **CLI arguments** for flexibility  
✅ Uses **Poetry for dependency management**  

---

## **📦 Project Structure**
```
pubmedapitask/
│── researchpapers/
│   ├── __init__.py
│   ├── main.py              # CLI script for fetching and processing papers
│   ├── pubmedapi.py         # Fetches data from PubMed API
│   ├── data_processing.py   # Extracts and filters authors from XML data
│── .gitignore
│── pyproject.toml           # Poetry dependencies and setup
│── README.md                # Documentation
```

---

## **🛠 Installation & Setup**
### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/ShreyasDankhade/pubmedapitask.git
cd pubmedapitask
```

### **2️⃣ Install Poetry (If Not Installed)**
```bash
pip install poetry
```

### **3️⃣ Install Dependencies**
```bash
poetry install
```



## **🚀 Usage**
Run the script via **Poetry**:

### **Fetch papers and print output**
```bash
poetry run get-papers-list "cancer immunotherapy"
```

### **Fetch papers and save as CSV**
```bash
poetry run get-papers-list "diabetes research" -f research_results.csv
```

### **Enable Debug Mode**
```bash
poetry run get-papers-list "genetic engineering" -d
```

---

## **🔧 Command-Line Arguments**
| Option | Description |
|--------|-------------|
| `query` | **(Required)** Search term for fetching research papers |
| `-f`, `--file` | Specify filename to save results as a CSV |
| `-d`, `--debug` | Enable debug mode for detailed logs |

---

## **⚙️ Running Inside Poetry Shell**
If `poetry run` doesn't work, enter the **Poetry virtual environment** first:
```bash
poetry shell
get-papers-list "cancer immunotherapy" -f output.csv
```

---

## **📜 Example Output**
```csv
PubmedID,Title,Publication Date,Authors with Pharma/Biotech Affiliations
123456, "Breakthrough in Cancer Research", 2024-03, "Dr. John Doe, Dr. Emily Smith"
789101, "Genetic Engineering in Medicine", 2023-11, "Dr. Alex Brown"
```

---

## **🔄 Updating the Project**
To update dependencies:
```bash
poetry update
```

To pull latest changes from GitHub:
```bash
git pull origin main
poetry install
```

---

## **🔍 Troubleshooting**
### **1️⃣ "ModuleNotFoundError"**
If Poetry cannot find modules:
```bash
poetry install
poetry run get-papers-list "cancer research"
```

### **2️⃣ "No API Key Found"**
Ensure the **API_KEY** is set in `.env` or exported in the terminal.

### **3️⃣ "get-papers-list: command not found"**
Manually run the script:
```bash
poetry run python researchpapers/main.py "cancer research"
```

---

## **📌 Technologies Used**
- **Python 3.9+**
- **Poetry** (Dependency Management)
- **Requests** (HTTP Requests)
- **Pandas** (Data Processing)
- **XML Parsing** (PubMed Data Extraction)

---

## **🌟 Contributing**
1. Fork the repository
2. Create a feature branch (`git checkout -b feature-name`)
3. Commit changes (`git commit -m "Added feature X"`)
4. Push to GitHub (`git push origin feature-name`)
5. Submit a Pull Request 🚀

---

## **📜 License**
This project is licensed under the **MIT License**.

---

## **📧 Contact**
For questions or support, contact **[Your Name]** at **your.email@example.com**.

---

This README **fully documents** your project. Let me know if you'd like any changes! 🚀
