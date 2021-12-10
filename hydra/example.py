"""hydra/common.yaml
# @package hydra

run:
  dir: ${LOGS_ROOT}/hydra/${RUN_NAME}/${now:%y%m%d_%H%M%S}
job_logging:
  formatters:
    file:
      format: "[%(levelname)s] %(asctime)s - %(name)s \n %(message)s"
    console:
      format: "%(message)s"
  handlers:
    console:
      class: logging.StreamHandler
      level: INFO
      formatter: console
      stream: ext://sys.stdout
    file:
      class: logging.FileHandler
      level: NOTSET
      formatter: file
  loggers:
    root:
      level: NOTSET
      handlers:
        - console
        - file
    PIL:
      level: INFO
      handlers:
        - console
        - file
    matplotlib:
      level: INFO
      handlers:
        - console
        - file
    git:
      level: INFO
      handlers:
        - console
        - file
"""

from dataclasses import dataclass
from logging import getLogger

import hydra
from hydra.core.config_store import ConfigStore
from rul_prediction import PROJECT_ROOT

logger = getLogger(__file__)


@dataclass
class ConfigTrain:
    LOGS_ROOT: str = "logs"
    RUN_NAME: str = "noname"


cs = ConfigStore.instance()
cs.store(name="train_store", node=ConfigTrain)
hydra_dir = PROJECT_ROOT / "config" / "ml"

EXP_NAME: str = "debug"


@hydra.main(config_path=hydra_dir, config_name="train")
def main(cfg: ConfigTrain):
    print(cfg)
    print("helo")


if __name__ == '__main__':
    main()
