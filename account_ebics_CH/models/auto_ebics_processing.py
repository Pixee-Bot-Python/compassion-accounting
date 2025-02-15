import datetime
import logging

from odoo import api, models

_logger = logging.getLogger(__name__)


class AutoEBICSProcessing(models.AbstractModel):
    _description = "Automatic EBICS Processing"
    _name = "auto.ebics.processing"

    @api.model
    def process(self, n_days_ago=None):
        """Fetch 'new' EBICS files (by setting no dates to the ebics.xfer)
        After getting them, process them.
        n_days_ago: (mainly for debug purposes)
        if an integer is specified retrieve the EBICS from n days ago
        instead of the new ones
        """
        _logger.info("Starting")
        d = {}
        if n_days_ago is not None:
            n_days_ago = datetime.date.today() - datetime.timedelta(days=n_days_ago)
            d.update({"date_from": n_days_ago, "date_to": n_days_ago})
        for conf in self.env["ebics.config"].search([("state", "=", "confirm")]):
            d.update(
                {
                    "ebics_config_id": conf.id,
                    "ebics_userid_id": conf.ebics_userid_ids[0].id,
                }
            )
            xfer = self.env["ebics.xfer"].create(d)
            try:
                output = xfer.ebics_download()
                ebics_retrieved = self.env["ebics.file"].browse(
                    output["context"]["ebics_file_ids"]
                )
            except Exception:
                _logger.error("Failed", exc_info=True)
                return False

            for ebics in ebics_retrieved:
                try:
                    res = ebics.process()
                    if res is None:
                        raise Exception
                except Exception:
                    _logger.warning(
                        f"EBICS file {ebics.display_name} could not be processed",
                        exc_info=True,
                    )
            xfer.unlink()
        _logger.info("Finished")
        return True
