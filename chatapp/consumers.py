from channels.generic.websocket import AsyncWebsocketConsumer
from urllib.parse import urlparse, parse_qs
import json
from.models import ChatMessages
from channels.db import database_sync_to_async
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync


# chat consumer
class PersonalChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        query_params = dict(parse_qs(self.scope['query_string'].decode()))

        # Extract user_id and receiver_id from the query parameters
        if query_params.get('receiver_id', [None])[0] == "null":
             self.room_group_name = None
        else:
            user_id = int(query_params.get('user_id', [None])[0])
            receiver_id = int(query_params.get('receiver_id', [None])[0])
            if user_id > receiver_id:
                self.room_name = f'{user_id}_{receiver_id}'
            else:
                self.room_name = f'{receiver_id}_{user_id}'
            self.room_group_name = 'chat_%s' % self.room_name

            await self.channel_layer.group_add(
                    self.room_group_name,
                    self.channel_name
                )
            await self.accept()
            await self.send(text_data=self.room_group_name)

    async def disconnect(self, close_code):
            if self.room_group_name is not None:
                await self.channel_layer.group_discard(
                    self.room_group_name,
                    self.channel_layer
                )
            else:
                 print("no users")



    async def receive(self, text_data=None, bytes_data=None):
        text_data_json = json.loads(text_data)
        message = text_data_json['content']
        userId = text_data_json['sender']
        reciever_id = text_data_json['receiver']
        await self.save_message(userId,reciever_id,message,self.room_group_name)
        await self.channel_layer.group_send(
              self.room_group_name,
            {
                'type': 'chat_message',
                'content': message,
                "sender":userId,
                "receiver":reciever_id
            }
        )

    async def chat_message(self, event):
        content = event['content']
        sender = event['sender']
        receiver = event['receiver']
        await self.send(text_data=json.dumps({
            'content': content,
            "sender":sender,
            "receiver":receiver
        }))



    @database_sync_to_async
    def save_message(self,sender,reciever,message_content,thread):
         ChatMessages.objects.create(sender = sender,receiver = reciever,content = message_content,thread_name= thread) 





# notification consumer
class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        query_params = dict(parse_qs(self.scope['query_string'].decode()))
        user_id = int(query_params.get('user_id', [None])[0])
        self.room_name = f'{user_id}_room'
        self.room_group_name = f'notification_{user_id}'
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        print("socket connected")
        await self.accept()
    
    async def disconnect(self,close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )



    async def receive(self, text_data=None, bytes_data=None):
         pass
    
    async def send_notification(self, event):
        notification = event['notification']
        await self.send(text_data=json.dumps({
            'notification': notification
        }))

def send_notification_to_user(user_id,notification_message):
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        f'notification_{user_id}',
        {
            'type': 'send_notification',
            'notification': notification_message,
        }
    )
