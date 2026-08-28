---
layout: 2026/program-page-2026
title: Workshops
permalink: /2026/workshops/
---
---
*Last updated: 2026-07-31 01:00PM CET*

---


<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-FQFFZGXF3Y"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'G-FQFFZGXF3Y');
</script>

## Workshops

{% assign all_workshops = site.data["2026"].workshops %}
{% assign allday_workshops = all_workshops | where_exp: "w", "w['Day/Time'] contains 'All Day'" | sort: "Day/Time" %}
{% assign morning_workshops = all_workshops | where_exp: "w", "w['Day/Time'] contains 'Morning'" | sort: "Day/Time" %}
{% assign afternoon_workshops = all_workshops | where_exp: "w", "w['Day/Time'] contains 'Afternoon'" | sort: "Day/Time" %}
{% assign sorted_workshops = allday_workshops | concat: morning_workshops | concat: afternoon_workshops %}
{% for workshop in sorted_workshops %}
### {{ workshop["Title"] }}
{: #{{ workshop["Title"] | slugify }} }

{% assign contact_name = workshop["Main Contact Person"] | default: "" | strip %}
{% assign contact_email = workshop["Main Contact Email"] | default: "" | strip %}
{% assign workshop_website = workshop["Website"] | default: "" | strip %}
{% assign workshop_cfp = workshop["CFP"] | default: "" | strip %}
{% assign day_time = workshop["Day/Time"] | default: "" | strip %}
{% assign room = workshop["Room"] | default: "" | strip %}

{%- if day_time != '' %}
**Day/Time:** {{ day_time }}<br>
{%- endif -%}
{%- if room != '' %}
**Room:** {{ room }}<br>
{%- endif -%}
{%- if contact_name != '' and contact_email != '' %}
**Main Contact Person:** [{{ contact_name }}](mailto:{{ contact_email }})
{%- elsif contact_name != '' %}
**Main Contact Person:** {{ contact_name }}
{%- endif %}

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