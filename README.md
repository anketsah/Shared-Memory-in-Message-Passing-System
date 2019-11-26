# Shared-Memory-in-Message-Passing-System
CS 249-Distributed Computing by Prof. Benjamin Reed

Implementation of ABD protocol

Step 1:

Use this command on terminal to generate the gRPC client and server interfaces from your .proto service definition

$ python3 -m grpc_tools.protoc -I . --python_out=. --grpc_python_out=. AnketAbdProto.proto

The generated code files are called AnketAbdProto_pb2.py and AnketAbdProto_pb2_grpc.py and contain:

-classes for the messages defined in AnketAbdProto.proto
-classes for the service defined in AnketAbdProto.proto
  -AnketAbdProtoStub, which can be used by clients to invoke AnketAbdProto RPCs
  -AnketAbdProtoServicer, which defines the interface for implementations of the AnketAbdProto service
-a function for the service defined in AnketAbdProto.proto
  -add_AnketAbdProto_to_server, which adds a AnketAbdProtoServicer to a grpc.Server 


Step 2:

Run the server, which will listen on port 2222:

$ python AnketAbdServer.py

Run the client (in a different terminal):

$ python AnketAbdClient.py 
