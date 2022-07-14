
# tmux new-session -s fastapi 'cd backend; source venv/bin/activate; uvicorn main:app --reload';  # open tmux session and run ruby script.
# tmux new-session -d 'cd backend; source venv/bin/activate; uvicorn main:app --reload' \; split-window -v \; select-pane -t 1 ;
# tmux new-session  \; split-window -v \; select-pane -t 1 \; venv/bin/activate \; uvicorn main:app --reload \; select-pane -t 2 \; cd frontend \; npm run start;
tmux new-session  \; split-window -v \; select-pane -t 1 \; send-keys -t $session:$window  'cd backend; . venv/bin/activate; uvicorn main:app --reload' ENTER \; select-pane -t 2 \; send-keys -t $session:$window 'cd frontend; npm run start' ENTER ; 
# gnome-terminal --window-with-profile=NAMEOFTHEPROFILE -e "bash -c 'cd ./backend; source venv/bin/activate;ls; uvicorn main:app --reload; sleep 3'"
# tmux new-session -d 'cd backend; source venv/bin/activate; uvicorn main:app --reload';  # open tmux session and run ruby script.
# tmux new-window 'cd frontend; npm run start';
# tmux -2 attach-session -d
# gnome-terminal --window-with-profile=NAMEOFTHEPROFILE -e "bash -c 'cd ./frontend; npm run start'"

# cd ./backend
# source venv/bin/activate
# uvicorn main:app --reload
# cd ../frontend
# npm run start
