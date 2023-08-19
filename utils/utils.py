import datetime

import pytz


class DateTimeUtils:
    """
    A utility class for handling date and time operations.
    """

    @staticmethod
    def get_current_utc_time() -> datetime.datetime:
        """
        Returns the current time in UTC.

        Returns:
            datetime.datetime: The current time in UTC.
        """
        local_now = datetime.datetime.now(pytz.timezone("UTC"))
        return DateTimeUtils.format_time(local_now)

    @staticmethod
    def format_time(date_time: datetime.datetime) -> datetime.datetime:
        """
        Formats a datetime object to the format '%Y-%m-%d %H:%M:%S'.

        Args:
            date_time (datetime.datetime): The datetime object to format.

        Returns:
            datetime.datetime: The formatted datetime object.
        """

        formatted_time = date_time.strftime("%Y-%m-%d %H:%M:%S %z")
        return datetime.datetime.strptime(formatted_time, "%Y-%m-%d %H:%M:%S %z")


class _CustomHTTPHandler:
    @staticmethod
    def get_client_ip_address(request):
        req_headers = request.META
        return (
            x_forwarded_for_value.split(",")[-1].strip()
            if (x_forwarded_for_value := req_headers.get("HTTP_X_FORWARDED_FOR"))
            else req_headers.get("REMOTE_ADDR")
        )




