---
layout: 2026/program-page-2026
title: Workshops
permalink: /2026/workshops/
---
---
*Last updated: 2026-06-29 03:00PM CET*

---

## Overview

This page contains information about the call for workshop papers for ISMAR 2026 for all accepted workshops. Each workshop has its own submission deadline and requirements, so please refer to the specific workshop pages for details.

## Workshops

{% for workshop in site.data["2026"].workshops %}
### {{ workshop["Title"] }}

{% assign contact_name = workshop["Main Contact Person"] | default: "" | strip %}
{% assign contact_email = workshop["Main Contact Email"] | default: "" | strip %}
{% assign workshop_website = workshop["Website"] | default: "" | strip %}
{% assign workshop_cfp = workshop["CFP"] | default: "" | strip %}

{% if contact_name != '' and contact_email != '' %}
**Main Contact Person:** [{{ contact_name }}](mailto:{{ contact_email }})
{% elsif contact_name != '' %}
**Main Contact Person:** {{ contact_name }}
{% endif %}

{% if workshop_website != '' %}
<p>
  <strong>
    <a href="{{ workshop_website }}" target="_blank" rel="noopener">
      &gt; Workshop Website
    </a>
  </strong>
</p>
{% elsif workshop_cfp != '' %}
<p>
  <strong>
    <a href="{{ workshop_cfp }}" download>
      &gt; Download CfP
    </a>
  </strong>
</p>
{% endif %}

#### Abstract  
{{ workshop["Abstract"] }}

---

{% endfor %}