cd backend;
python3.10 -m venv venv;
. venv/bin/activate;
pip install -r req.txt;
cd ../frontend;
npm i --save;
cd ../;
deactivate;
