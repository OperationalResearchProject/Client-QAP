# Client-QAP

## Re-compile proto files
    ```
    python -m grpc_tools.protoc -I=./protos --python_out=./protoGenerated --grpc_python_out=./protoGenerated protos/messages.proto protos/hcfi.proto protos/tabousearch.proto
    ```