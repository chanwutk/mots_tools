import sys
from functools import partial
from multiprocessing import Pool

from .visualize_mots import process_sequence
from ..mots_common.io import load_seqmap


def main():
    if len(sys.argv) != 5:
        print("Usage: python visualize_mots.py tracks_folder(gt or tracker results) img_folder output_folder seqmap")
        sys.exit(1)
   
    tracks_folder = sys.argv[1]
    img_folder = sys.argv[2]
    output_folder = sys.argv[3]
    seqmap_filename = sys.argv[4]
   
    seqmap, max_frames = load_seqmap(seqmap_filename)
    process_sequence_part = partial(
        process_sequence,
        max_frames=max_frames,
        tracks_folder=tracks_folder,
        img_folder=img_folder,
        output_folder=output_folder,
    )
   
    with Pool(10) as pool:
        pool.map(process_sequence_part, seqmap)
    # for seq in seqmap:
    #     process_sequence_part(seq)


if __name__ == "__main__":
  main()
