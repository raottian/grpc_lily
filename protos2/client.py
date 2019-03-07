import grpc
import data_pb2
import data_pb2_grpc


_HOST = 'localhost'
_PORT = '8080'

def run():
    conn = grpc.insecure_channel(_HOST + ':' + _PORT)
    print(conn)
    client = data_pb2_grpc.FormatDataStub(channel=conn)
    print(client)
    response = client.DoFormat(data_pb2.actionrequest(text='izhaohu!'))
    print("received: " + response.text)
if __name__=='__main__':
    run()