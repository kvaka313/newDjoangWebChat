import os
import django
from sockjs.tornado import SockJSConnection

from MyWebChat.models import Messages, Credential

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rest.settings')
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
django.setup()


class SocketHandler(SockJSConnection):
    client_sock = {}

    def on_open(self, request):
        print('socket open')

    def on_close(self):
        print('socket close')

    def on_message(self, message):
        message_array = message.split(':')
        if message_array[0] == 'name':
            SocketHandler.client_sock[message_array[1]] = self
            messages = get_messages(message_array[1])
            print("before for")
            for mes in messages:
                user = Credential.objects.filter(id=mes.id_sender).first()
                output = user.login + ':' + mes.message
                self.send(output)
            print('after')
            Messages.objects.all().delete()
        elif message_array[0] == 'list_active':
            print('list_active')
            output = 'list_active:'
            for key in SocketHandler.client_sock.keys():
                output += key + '\n'
            self.send(output)
        elif message_array[0] == 'broadcast':
            output_message = message_array[0] + ':' + message_array[1]
            for client in SocketHandler.client_sock.values():
                client.send(output_message)
        else:
            receiver_name = message_array[0]
            sender_name = None
            for name, sock in SocketHandler.client_sock.items():
                if sock == self:
                    sender_name = name
                    break
            output_message = sender_name + ':' + message_array[1]
            if receiver_name in SocketHandler.client_sock.keys():
                SocketHandler.client_sock[receiver_name].send(output_message)
            else:
                credential_sender = Credential.objects.filter(login=sender_name).first()
                credential_receiver = Credential.objects.filter(login=receiver_name).first()
                mes = Messages(id_sender=credential_sender, id_receiver=credential_receiver, message=message_array[1])
                mes.save()


def get_messages(name):
        return Messages.objects.filter(id_receiver__login=name)
