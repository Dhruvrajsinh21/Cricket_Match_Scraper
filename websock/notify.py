from websock.server import notify_clients
import json

async def send_match_update(match_id,matchinfo):
    update = {"match_id": match_id, "data": matchinfo}
    await notify_clients(json.dumps(update))
