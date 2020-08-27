class ResponseObject:
    def __init__(self, attrs):
        for attr, value in attrs.items():
            setattr(self, attr, value)