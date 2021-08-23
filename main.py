import sys

from app.tracks import get_repeated_tracks


def handle_args(passed_args: [str]) -> dict:
    if len(passed_args) < 4:
        print("wrong number of arguments")
        print("usage: ... <client_id> <client_secret> <playlist_id>")
        exit(1)

    return {
        "client_id": passed_args[1],
        "client_secret": passed_args[2],
        "playlist_id": passed_args[3]
    }


if __name__ == '__main__':
    args = handle_args(sys.argv)
    repeated_tracks = get_repeated_tracks(args["client_id"], args["client_secret"], args["playlist_id"])
    repeated_tracks.sort()
    print("Faixas Repetidas")
    for faixa in repeated_tracks:
        print(" :: {}".format(faixa))
