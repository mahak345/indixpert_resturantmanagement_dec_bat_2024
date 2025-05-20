def log_event(event: str):
    with open("Src/Logs1/restaurant.log", 'a') as f:
        f.write(event + '\n')
