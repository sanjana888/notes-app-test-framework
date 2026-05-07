# Configure framework logging.
# Save logs for debugging purpose.

import logging

logging.basicConfig(
    filename="reports/test.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger()