import sys

from .eval import run_eval


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python eval.py results_folder gt_folder seqmap")
        sys.exit(1)
   
    results_folder = sys.argv[1]
    gt_folder = sys.argv[2]
    seqmap_filename = sys.argv[3]
   
    run_eval(results_folder, gt_folder, seqmap_filename)

