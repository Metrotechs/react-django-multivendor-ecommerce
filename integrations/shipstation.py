from shipstation import ShipStationAPI

class ShipStationIntegration:
    def __init__(self, api_key, api_secret):
        self.api = ShipStationAPI(api_key, api_secret)

    def create_shipment(self, order_data):
        shipment = self.api.create_shipment(order_data)
        return shipment

    def get_shipment_status(self, shipment_id):
        status = self.api.get_shipment_status(shipment_id)
        return status

    def list_shipments(self, params=None):
        shipments = self.api.list_shipments(params)
        return shipments

    def update_shipment(self, shipment_id, update_data):
        updated_shipment = self.api.update_shipment(shipment_id, update_data)
        return updated_shipment

    def delete_shipment(self, shipment_id):
        response = self.api.delete_shipment(shipment_id)
        return response