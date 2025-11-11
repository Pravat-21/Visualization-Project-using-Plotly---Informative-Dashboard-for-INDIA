# 📊 Data Visualization with Python

A comprehensive data visualization and analysis platform for India's Census Data, built with Python and Streamlit. This interactive dashboard provides insightful visualizations and analytics at national, state, and district levels.

![Python](https://img.shields.io/badge/Python-3.13+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.51.0-red.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

## ✨ Features

- **📈 Overall Analysis**: National-level demographic insights and trends
- **🗺️ Statewise Analysis**: Detailed statistics for individual states
- **🏘️ Districtwise Analysis**: Granular data visualization at the district level
- **📊 Interactive Visualizations**: Dynamic charts powered by Plotly and Seaborn
- **🎯 User-Friendly Interface**: Clean and intuitive Streamlit dashboard
- **📱 Responsive Design**: Works seamlessly across different screen sizes

## 🎯 Key Metrics Analyzed

- Population demographics (Male/Female distribution)
- Sex ratio calculations
- Literacy vs Illiteracy rates
- District-wise comparative analysis
- State-level trends and patterns

## 🚀 Quick Start

### Prerequisites

- Python 3.13 or higher
- pip or uv package manager

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd "Data Visualization with Python"
   ```

2. **Set up virtual environment** (optional but recommended)
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**
   
   Using pip:
   ```bash
   pip install -r requirements.txt
   ```
   
   Or using uv:
   ```bash
   uv pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   streamlit run app.py
   ```

5. **Open your browser**
   
   [click here](https://mc2eq7xzwjexex2qmfrznq.streamlit.app/) to view the dashboard

## 📁 Project Structure

```
Data Visualization with Python/
│
├── app.py                      # Main Streamlit application
├── overall.py                  # Overall analysis module
├── statewise.py               # State-level analysis module
├── distwise.py                # District-level analysis module
├── main.py                    # Additional main script
│
├── census_data/               # Census datasets
│   └── final_df.csv          # Processed census data
│
├── notebooks/                 # Jupyter notebooks for exploration
│   ├── 01_exp.ipynb
│   └── 02_exp.ipynb
│
├── messy_data/               # Raw/unprocessed data files
│
├── requirements.txt          # Project dependencies
├── pyproject.toml           # Project configuration
├── .gitignore               # Git ignore rules
├── .python-version          # Python version specification
└── README.md                # Project documentation (this file)
```

## 🛠️ Technologies Used

### Core Libraries
- **Streamlit** - Web application framework
- **Pandas** - Data manipulation and analysis
- **NumPy** - Numerical computing
- **Matplotlib** - Static visualizations
- **Seaborn** - Statistical data visualization
- **Plotly** - Interactive charts and graphs

### Development Tools
- **Git** - Version control
- **Jupyter Notebook** - Data exploration and prototyping
- **VS Code** - Development environment

## 📊 Usage

### Overall Analysis
Click on the **"Overall-Analysis"** button in the sidebar to view:
- National demographic overview
- Population distribution patterns
- Key statistical insights

### Statewise Analysis
1. Select **"Statewise-Analysis"** from the dropdown
2. Choose your desired state
3. Click **"Show analysis"** to view state-specific data

### Districtwise Analysis
1. Select **"Districtwise-Analysis"** from the dropdown
2. Choose a state (or select "All India")
3. Select a specific district
4. Click **"Show analysis"** to view detailed district data

## 🔍 Data Insights

The dashboard automatically calculates and displays:
- **Sex Ratio**: `(Female/Male) × 100`
- **Illiteracy Ratio**: `(Illiterate/Literate) × 100`
- District codes for easy identification
- Comparative visualizations across regions

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 🐛 Known Issues

- Working on optimizing large dataset loading times
- Enhancing mobile responsiveness for complex visualizations

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👤 Author

**Pravat Patra**

## 🙏 Acknowledgments

- Census data provided by the Government of India
- Streamlit community for excellent documentation
- Python data science community for amazing libraries

## 📧 Contact

For questions, suggestions, or feedback, please open an issue in the repository.

---

⭐ **Star this repository if you find it helpful!**

Made with ❤️ and Python
