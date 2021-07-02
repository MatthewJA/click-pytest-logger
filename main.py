import logging, click

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

@click.command()
@click.argument('value')
def main(value):
    logger.info(value)
    raise RuntimeError()
