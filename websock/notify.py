from websock.server import notify_clients
import json

async def send_match_update():
    update = {"match_id": 1, "data": "hi"}
    await notify_clients(json.dumps(update))
