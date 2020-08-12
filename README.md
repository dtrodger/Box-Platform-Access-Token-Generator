## Box Platform Access Token Generator 
### Set up and Run  
1. From the project root folder, create a Python 3.6+ virtual environment  
`$ virtualenv --python=python3 env`  
2. Activate the virtual environment  
`$ source env/bin/activate`  
3. Install the project dependencies  
`$ pip install -r requirements.txt`  
4. Create a file at the project root folder called `box_jwt_keys.yml` and add your Box Platform JWT keys  
5. Run the app to output an access token in your terminal  
`python main.py`  