# 📢 Post on LinkedIn via Python

This project demonstrates how to create a **LinkedIn post using Python** and the LinkedIn API.

## ⚙️ Setup
1. Install dependencies:
   ```bash
   pip install requests
   ```

2. Update `env.example.txt` with your LinkedIn API credentials.  
   - `LINKEDIN_ACCESS_TOKEN` → Generated via LinkedIn Developer App.  
   - `LINKEDIN_AUTHOR_URN` → Your LinkedIn profile URN (`urn:li:person:<id>`).  

3. Load environment variables:
   ```bash
   source load_env.sh
   ```

4. Run the script:
   ```bash
   python3 post_linkedin.py
   ```

## 📌 Notes
- The script posts a simple text message to your LinkedIn profile.  
- You can modify the script to include images, links, or rich media content.
