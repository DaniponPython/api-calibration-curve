from pythonjsonlogger import jsonlogger
from django.utils import timezone


class LogstashJSONFormatter(jsonlogger.JsonFormatter):
    def add_fields(self, log_record, record, message_dict):
        super(LogstashJSONFormatter, self).add_fields(
            log_record, record, message_dict
        )
        if not log_record.get("tztime"):
            tztime = timezone.now().strftime("%Y-%m-%dT%H:%M:%S.%fZ")
            log_record["tztime"] = tztime
