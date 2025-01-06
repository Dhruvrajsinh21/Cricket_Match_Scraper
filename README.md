# Cricket Match Real-Time Monitoring System

This project implements a real-time cricket match monitoring system using web scraping, MongoDB, WebSocket notifications, and scheduling. The system is designed to scrape match schedules, detailed information, and provide real-time updates when matches are live. 

---

## **Project Features**

- **Scraping**: Periodic scraping of match schedules and detailed match data.
- **Database**: MongoDB is used for storing match schedules and real-time updates.
- **WebSocket Notifications**: Sends real-time updates to connected clients when a match goes live.
- **Scheduling**: Automated tasks using APScheduler to monitor matches and trigger real-time updates.

---

## **Project Structure**

```
project/
├── scrapers/
│   ├── match_list_scraper.py       # Scrapes match schedules
│   ├── match_detail_scraper.py     # Scrapes detailed match information
├── scheduler/
│   ├── monitor.py                  # Scheduler for periodic tasks
│   ├── trigger_jobs.py             # Real-time updates for live matches
├── database/
│   ├── db_connection.py            # MongoDB connection setup
│   ├── queries.py                  # Database operations
├── websocket/
│   ├── server.py                   # WebSocket server implementation
│   ├── notify.py                   # Handles WebSocket notifications
├── main.py                         # Entry point to run the system
├── requirements.txt                # Python dependencies
├── README.md                       # Documentation
```

---

## **Setup and Installation**

### **1. Prerequisites**
- Python 3.8+
- MongoDB installed and running on `localhost:27017`

### **2. Install Required Dependencies**

Run the following command to install dependencies:
```bash
pip install -r requirements.txt
```

### **3. Start MongoDB**
Ensure MongoDB is running:
```bash
mongod
```

---

## **How to Run the Program**

### **1. Activate Virtual Environment**
If you are using a virtual environment, activate it first:
```bash
# On Windowsenv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

### **2. Install Dependencies**
Ensure all dependencies are installed:
```bash
pip install -r requirements.txt
```

### **3. Start the Main Program**
Run the main entry point to integrate all components:
```bash
python main.py
```
This will:
- Start the WebSocket server
- Initialize the match scheduler
- Begin monitoring and updating matches in real time

---

## **Functionalities**

### **1. Match List Scraping**
- Scrapes match schedules from the URL: `https://crex.live/fixtures/match-list`.
- Stores match data (e.g., match ID, start time, URL) in MongoDB.

### **2. Match Detail Scraping**
- Scrapes detailed match data such as match info, squads, and more.
- Updates MongoDB with real-time data during live matches.

### **3. Real-Time Updates**
- Periodically checks for matches starting soon.
- Scrapes real-time data for live matches and updates MongoDB.
- Sends updates to connected WebSocket clients.

### **4. WebSocket Notifications**
- WebSocket server listens on `ws://localhost:6789`.
- Sends real-time match updates to all connected clients.

---

## **How to Test**

### **1. Verify MongoDB Data**
Use a MongoDB client like Compass to check the `match_database`:
- `matches` collection contains scraped match data.

### **2. Test WebSocket Notifications**
Use a WebSocket client (e.g., Postman, or a custom script) to connect to `ws://localhost:6789` and receive real-time updates.

#### Example Client Script
```python
import asyncio
import websockets

async def connect():
    uri = "ws://localhost:6789"
    async with websockets.connect(uri) as websocket:
        async for message in websocket:
            print("Update received:", message)

asyncio.run(connect())
```

---

## **Modules Overview**

### **Database**
- **`db_connection.py`**: Sets up MongoDB connection.
- **`queries.py`**: Handles saving and querying match data.

### **Scrapers**
- **`match_list_scraper.py`**: Scrapes match schedules.
- **`match_detail_scraper.py`**: Scrapes detailed match info (e.g., match info, squads).

### **Scheduler**
- **`monitor.py`**: Schedules periodic scraping tasks using APScheduler.
- **`trigger_jobs.py`**: Monitors matches and triggers real-time updates.

### **WebSocket**
- **`server.py`**: Implements WebSocket server for real-time notifications.
- **`notify.py`**: Handles sending notifications to connected WebSocket clients.

### **Main Entry Point**
- **`main.py`**: Starts the WebSocket server, scheduler, and real-time monitoring threads.

---

## **Questions to Address**

### **Why this Approach?**
- Web scraping ensures up-to-date data.
- MongoDB is ideal for handling semi-structured data.
- WebSocket allows real-time communication with minimal latency.

### **Optimizations**
- Scraping intervals are optimized to reduce unnecessary resource usage.
- Real-time updates are event-driven for efficiency.

### **Future Enhancements**
- Add error handling and retry logic for scrapers.
- Implement rate-limiting and caching to avoid overloading the source.
- Extend WebSocket notifications to support filtering by match ID.

---

## **License**
This project is licensed under the MIT License.
