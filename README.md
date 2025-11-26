# gwmp-mux

GWMP is a **G**ate**W**ay **M**essaging **P**rotocol used by LoRa packet
forwarders to typically talk to a LoRaWAN Network Server (LNS).

On the ThingsIX Network, the GWMP can be used to send packets to the ThingsIX [forwarder](https://github.com/ThingsIXFoundation/packet-handling). 

On the Helium's Network, the GWMP is used to send packets to a Helium [gateway
rs](https://github.com/helium/gateway-rs).

This program, gwmp-mux, allows for a single packet forwarder connection to
be multiplexed out to one or more potential hosts. As such, a single gateway
can connect to multiple LNSs. For example the above gateway-rs and forwarder
can be used on the same gateway.

## Configuration

`gwmp-mux` can be configured via Docker environment variables that control how
the startup script builds its command line:

- `GWMP_MUX_HOST` – optional port to run the multiplexer on (passed to
  `--host`).
- `GWMP_MUX_CLIENTS` – comma-separated list of packet forwarder endpoints to
  forward traffic to (each passed to `--client`). If not provided, the default
  target is `helium-miner:1680`.

When the container runs in a Balena fleet whose name ends with `-c` and the
`/var/thix/config.yaml` file exists, the ThingsIX forwarder
`thix-forwarder:1680` is automatically added to the client list.
