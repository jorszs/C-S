import napsterServer

SERVER_PORT = "8011"

s = napsterServer.zerorpc.Server(napsterServer.napsterServer())
s.bind("tcp://*:"+SERVER_PORT)
s.run()
