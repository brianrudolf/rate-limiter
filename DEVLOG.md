Goal: Add distributed datastore for storing request data.
Motivation: 
    The inital work for implementing the `sliding window` rate limiting algorithm led to issues using the same Python dictionary with Flask's multi-threaded model. This was expected to arrive as the algorithm became more complex to support more clients
