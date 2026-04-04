"""Downloadartifact fro wandb and perform basic cleaning."""

import argparse
import logging
import wandb
import pandas as pd


logging.basicConfig(level=logging.INFO, format="%(asctime)-15s %(message)s")
logger = logging.getLogger()


def go(args):
    """Remove price outside the range args.min_price, args.max_price."""
    run = wandb.init(entity = "rental_price", name = "data cleaning", job_type="basic_cleaning")
    run.config.update(args)

    logger.info("Download artifact.")
    artifact_local_path = run.use_artifact(args.input_artifact).file()
    data = pd.read_csv(artifact_local_path)
    df = data.copy()

    logger.info("Remove price outliers.")
    df = df[df["price"].between(args.min_price, args.max_price)]
    df.to_csv("clean_sample.csv", index=False)

    logger.info("Create output artifact.")
    artifact = wandb.Artifact(
        args.output_artifact,
        type=args.output_type,
        description=args.output_description,
    )

    logger.info("Adding preprocessed file to artifact.")
    artifact.add_file("clean_sample.csv")
    run.log_artifact(artifact)

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="A very basic data cleaning")

    parser.add_argument(
        "--input_artifact", 
        type=str,
        help="Path to the artifact to be cleaned",
        required=True
    )

    parser.add_argument(
        "--output_artifact", 
        type=str,
        help="Result file out of the basic cleaning",
        required=True
    )

    parser.add_argument(
        "--output_type", 
        type=str,
        help="name of output artifact.",
        required=True
    )

    parser.add_argument(
        "--output_description", 
        type=str,
        help="Description of output artifact",
        required=True
    )

    parser.add_argument(
        "--min_price", 
        type=float,
        help="minimum price",
        required=True
    )

    parser.add_argument(
        "--max_price", 
        type=float,
        help="maximum price",
        required=True
    )


    args = parser.parse_args()

    go(args)
