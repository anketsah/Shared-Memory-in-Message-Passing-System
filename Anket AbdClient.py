import grpc
import time
import os
import abd_pb2
import abd_pb2_grpc
import sys

global register_n
global Register

#Initializations
#Getting the agruments to later parse it
D = sys.argv
#Getting the Ports
p = D[1]
All_timestamp = []
Response = []
All_value = []
#Holds Different channel values
Ports = p.split(",")

#Read function
def read(register_n):
 #Read1 Operation with value and timestamp as Response
 for i in Ports:
  print("II",Ports)
  print("opening channel...")
  with grpc.insecure_channel(i) as channel:
    print("creating stub...")
    stub = abd_pb2_grpc.ABDServiceStub(channel)
    print("making read1 request...")
    response = stub.read1(abd_pb2.Read1Request(register=register_n))
    Response.append(response)
    All_value.append(response.value)
    All_timestamp.append(response.timestamp)
 #Calculating maximal of the values from each Server
 max1 = max(All_timestamp)
 d = All_timestamp.index(max1)
 value_1 = All_value[d]
 max_response = max(All_timestamp)
 Response.clear()

#Read2 containg max value ytand it receives Ack(void) as Response
 for i in Ports:
  print("creating stub...")
  with grpc.insecure_channel(i) as channel:
    stub = abd_pb2_grpc.ABDServiceStub(channel)
    print("making read2 request... ")
    response = stub.read2(abd_pb2.Read2Request(register=register_n,timestamp=int(max1),value = value_1))
    Response.append(response)

#If more than half of the servers respond, then print the value of register and version else fail.
 if len(Response) >> int(len(Ports)/2):
     print("Value of Register and Version number:")
     print("Register Name: ",register_n)
     print("Value: ",value_1,"Timestamp: ",max1)
     Response.clear()
 else:
     print("Failed")
     Response.clear()

#Write function with Register name and new value as arguments
def write(register_n,new_value):
 for i in Ports:
  print("opening channel...")
  with grpc.insecure_channel(i) as channel:
    print("creating stub...")
    stub = abd_pb2_grpc.ABDServiceStub(channel)
    print("making write request...")
    #Since new value is given as an argument , no need of calcuating it
    #new_value = val + 1
    response = stub.write(abd_pb2.WriteRequest(register=register_n,timestampe=int(time.time()),value =new_value))
    Response.append(response)

#If more than half of the servers respond, then success else failed
 if len(Response) >> int(len(Ports)/2):
    print("Register Name:",register_n," Value:",new_value,"Timestamp:",int(time.time()))
    print("Success")
    Response.clear()
 else:
    print("Failed")
    Response.clear()

if len(D) == 5:
    if D[2] == 'write':
     register_n = str(sys.argv[3])
     new_value = str(sys.argv[4])
     write(register_n,new_value)
    else:
     print("Invalid syntax for write")

elif len(D) == 4:
    if D[2] == 'read':
     register_n = str(sys.argv[3])
     read(register_n)
    else:
     print("Invalid syntax for read")
else:
    print("Invalid syntax")
