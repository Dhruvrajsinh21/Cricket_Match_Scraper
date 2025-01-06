import threading
from scheduler.monitor import run_scheduler
from scheduler.trigger_jobs import trigger_real_time_updates
from websock.server import run_server  # Import run_websocket_server instead of start_websocket_server

def main():
    # Start threads for each module
    scheduler_thread = threading.Thread(target=run_scheduler, daemon=True, name="SchedulerThread")
    updates_thread = threading.Thread(target=trigger_real_time_updates, daemon=True, name="UpdatesThread")
    websocket_thread = threading.Thread(target=run_server, daemon=True, name="WebSocketThread")  # Run WebSocket server here
    
    # Start all threads
    scheduler_thread.start()
    updates_thread.start()
    websocket_thread.start()

    # Join threads to keep the main program alive
    scheduler_thread.join()
    updates_thread.join()
    websocket_thread.join()

if __name__ == "__main__":
    main()
 