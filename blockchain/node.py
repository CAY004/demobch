class Node:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.peers = set()

    def connect_to_peer(self, peer_address):
        self.peers.add(peer_address)

    def broadcast_transaction(self, transaction):
        for peer in self.peers:
            self.send_transaction(peer, transaction)

    def send_transaction(self, peer, transaction):
        # Logic to send transaction to the peer
        pass

    def receive_transaction(self, transaction):
        # Logic to handle received transaction
        pass

    def get_peers(self):
        return list(self.peers)