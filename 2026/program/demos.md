---
layout: 2026/program-page-2026
title: Demos
permalink: /2026/demos/
---

<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-FQFFZGXF3Y"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'G-FQFFZGXF3Y');
</script>

## Demos

**Room:** Sala Expositiva

{% for demo in site.data["2026"]["program"].demos %}
### {{ demo["Title"] }}
{: #{{ demo["Title"] | slugify }} }

**Demo ID:** {{ demo["Demo ID"] }}<br>
**Session:** {{ demo["Session"] }}<br>
**Authors:** {{ demo["Authors"] }}

{% if demo["Affiliations"] and demo["Affiliations"] != "" %}
#### Affiliations
{{ demo["Affiliations"] | newline_to_br }}
{% endif %}

#### Abstract
{{ demo["Abstract"] }}

---

{% endfor %}
