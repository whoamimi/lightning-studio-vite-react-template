# Step 1. Build the frontend
cd react_templates/react-app
npm install
npm run build

# Step 2. Go back to root and start the Python server
cd ../../
pip install -r requirements.txt
python main.py