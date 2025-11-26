#!/usr/bin/env python3
import os
import subprocess


DEFAULT_CLIENTS = ["helium-miner:1680"]
CLIENTS_ENV = "GWMP_MUX_CLIENTS"
HOST_ENV = "GWMP_MUX_HOST"


def parse_clients():
    env_clients = os.environ.get(CLIENTS_ENV)
    if env_clients:
        parsed = [client.strip() for client in env_clients.split(",") if client.strip()]
        if parsed:
            return parsed
    return list(DEFAULT_CLIENTS)


def unique_preserve_order(clients):
    seen = set()
    result = []
    for client in clients:
        if client not in seen:
            result.append(client)
            seen.add(client)
    return result


def build_command():
    bin_path = "/usr/local/bin/gwmp-mux"
    command = [bin_path]

    host = os.environ.get(HOST_ENV)
    if host:
        command.extend(["--host", host])

    clients = parse_clients()

    fleet_name = os.environ.get("BALENA_APP_NAME", "")
    if fleet_name.endswith("-c") and os.path.isfile("/var/thix/config.yaml"):
        clients.append("thix-forwarder:1680")

    for client in unique_preserve_order(clients):
        command.extend(["--client", client])

    return command


def main():
    command = build_command()
    subprocess.run(command, check=True)


if __name__ == "__main__":
    main()
