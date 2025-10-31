# Zootopia-with-API

This project generates a beautiful HTML page displaying detailed information about animals, fetched dynamically from the [API Ninjas Animals API](https://api-ninjas.com/api/animals).  
You can filter animals by skin type and automatically create a web page containing the results.

---

##  Installation

1. **Clone the repository**
```bash
   git clone https://github.com/yourusername/animals-web-generator.git
   cd animals-web-generator
```
2. **Create a virtual environment (optional but recommended)**
```bash 
  python -m venv venv
  source venv/bin/activate    # on macOS/Linux
  venv\Scripts\activate       # on Windows
```

3. **Install dependencies**
```bash
    pip install -r requirements.txt
```
4. **Set up your environment variables**
Create a .env file in the project root and add your API Ninjas API key:
```bash
    API_KEY=your_api_key_here
```
        
## Usage
Run the following command in your terminal:
```bash
python animals_web_generator.py
```
