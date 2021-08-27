import sys

from app.tracks import get_similar_tracks


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
    similar_tracks = get_similar_tracks(args["client_id"], args["client_secret"], args["playlist_id"])
    similar_tracks = sorted(similar_tracks, key=lambda k: k["name"])
    found_similarities = False
    for faixa in similar_tracks:
        if len(faixa["similarities"]) > 0:
            found_similarities = True
            print("{}".format(faixa["name"]))
            print(" :: Similaridades: ")
            print("    {}".format(faixa["similarities"]))
            print("===============================================================")

    if not found_similarities:
        print("Nenhuma Faixa Similar Encontrada")
