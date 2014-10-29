<?xml version="1.0" encoding="UTF-8"?>
<XRD xmlns="http://docs.oasis-open.org/ns/xri/xrd-1.0">
  {%  for link in links %}
  <Link rel="{{ link.rel }}"
        type="application/xrd+xml"
        template="{{ link.template | replace("jrd", "xrd")}}" />
  {% endfor %}
</XRD>
