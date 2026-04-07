

import requests
from typing import Union


def resolve_ip_location(ip_addr: str) -> Union[str, None]:
	try:
		ip_loc_response = requests.get(
			url=f"http://ip-api.com/json/{ip_addr}?fields=status,country,city",
			timeout=3
		)
		data = ip_loc_response.json()
		if data.get("status") == "success":
			return f"{data.get("city")}, {data.get("country")}"
		return None
	except Exception:
		return None