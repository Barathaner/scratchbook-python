from channels.routing import ProtocolTypeRouter, URLRouter
import chat.routing

application = ProtocolTypeRouter({
    # Use the URLRouter to route WebSocket requests
    "websocket": URLRouter(
        chat.routing.websocket_urlpatterns
    ),
})
