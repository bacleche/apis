from channels.generic.websocket import AsyncWebsocketConsumer
import json

class GamificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.group_name = "gamification_global"
        await self.channel_layer.group_add(self.group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.group_name, self.channel_name)

    async def receive(self, text_data):
        data = json.loads(text_data)
        event = data.get('event', '')
        await self.channel_layer.group_send(
            self.group_name,
            {"type": "gamification_event", "event": event}
        )

    async def gamification_event(self, event):
        await self.send(text_data=json.dumps({"event": event["event"]}))
