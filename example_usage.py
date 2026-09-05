from client import CrossChainBridgeInvariantAnomalyDetectorClient

def main():
    client = CrossChainBridgeInvariantAnomalyDetectorClient()
    res = client.detect_bridge_reserve_anomalies()
    print('Bridge Invariant Detector: ' + res['bridge_audit_id'] + ' (' + res['bridge_name'] + ')')
    print('Balanced: ' + str(res['reserve_invariant_balanced']) + ' | Delta USD: $' + str(res['balance_delta_usd']))
    print('Telemetry URL: ' + res['bridge_telemetry_url'])

if __name__ == '__main__':
    main()
