from concurrent import futures

import grpc

import abd_pb2
import abd_pb2_grpc

import time

class ABDServer(abd_pb2_grpc.ABDServiceServicer):
    def read1(self, read1_req, context):
        print("got: {}".format(read1_req))
        return abd_pb2.Read1Response(value="what? python")

server = grpc.server(futures.ThreadPoolExecutor())
abd_pb2_grpc.add_ABDServiceServicer_to_server(ABDServer(), server)
server.add_insecure_port("127.0.0.1:2222")
server.start()
while True:
    time.sleep(60)


    def read2(self, read2_req, context):
        print("got: {}".format(read2_req))
        return abd_pb2.AckResponse(value="read2")


    def write(self, write_req, context):
        print("got: {}".format(write_req))
        return abd_pb2.AckResponse(value="Written")

