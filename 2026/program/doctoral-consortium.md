---
layout: 2026/program-page-2026
title: Doctoral Consortium
permalink: /2026/doctoral-consortium/
---

<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-FQFFZGXF3Y"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'G-FQFFZGXF3Y');
</script>

## Doctoral Consortium Presentations

**Room:** Glasshaus

{% for dc in site.data["2026"]["program"].doctoral_consortium %}
### {{ dc["Submission title"] }}
{: #{{ dc["Submission title"] | slugify }} }

**ID:** {{ dc["ID"] }}<br>
**Presenter:** {{ dc["Name"] }}

#### Abstract
{{ dc["Abstract"] }}

---

{% endfor %}
