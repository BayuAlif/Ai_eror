# vtuber_api.py
import json
import websockets

class VTubeAPI:
    def __init__(self, vtube_ws_url):
        self.vtube_ws_url = vtube_ws_url

    async def authenticate(self, plugin_name, developer_name):
        async with websockets.connect(self.vtube_ws_url) as websocket:
            # Request token
            token_request = {
                "apiName": "VTubeStudioPublicAPI",
                "apiVersion": "1.0",
                "requestID": "requestToken",
                "messageType": "AuthenticationTokenRequest",
                "data": {
                    "pluginName": plugin_name,
                    "pluginDeveloper": developer_name
                }
            }
            await websocket.send(json.dumps(token_request))
            response = await websocket.recv()
            token = json.loads(response)["data"]["authenticationToken"]

            # Authenticate
            auth_request = {
                "apiName": "VTubeStudioPublicAPI",
                "apiVersion": "1.0",
                "requestID": "authenticate",
                "messageType": "AuthenticationRequest",
                "data": {
                    "pluginName": plugin_name,
                    "pluginDeveloper": developer_name,
                    "authenticationToken": token
                }
            }
            await websocket.send(json.dumps(auth_request))
            auth_response = await websocket.recv()
            return json.loads(auth_response)["data"]["authenticated"]

    async def send_expression(self, token, expression_name):
        async with websockets.connect(self.vtube_ws_url) as websocket:
            expression_request = {
                "apiName": "VTubeStudioPublicAPI",
                "apiVersion": "1.0",
                "requestID": "expression",
                "messageType": "ExpressionRequest",
                "data": {
                    "token": token,
                    "expressionID": expression_name
                }
            }
            await websocket.send(json.dumps(expression_request))
            response = await websocket.recv()
            return json.loads(response)
