# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

# from protos2 import data_pb2 as protos2_dot_data__pb2
import data_pb2 as protos2_dot_data__pb2

class FormatDataStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.DoFormat = channel.unary_unary(
        '/example.FormatData/DoFormat',
        request_serializer=protos2_dot_data__pb2.actionrequest.SerializeToString,
        response_deserializer=protos2_dot_data__pb2.actionresponse.FromString,
        )


class FormatDataServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def DoFormat(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_FormatDataServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'DoFormat': grpc.unary_unary_rpc_method_handler(
          servicer.DoFormat,
          request_deserializer=protos2_dot_data__pb2.actionrequest.FromString,
          response_serializer=protos2_dot_data__pb2.actionresponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'example.FormatData', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
