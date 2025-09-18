---
layout: 2025/page
title: Demos

---
*Last updated: 2025-09-18 03:20AM GMT*

# Demos

{% for demo in site.data.2025.demos %}
## {{ demo.id }}: {{ demo.title }}

**Authors:**<br>
{% for author in demo.authors %}{{ author }}{% if forloop.last == false %}, {% endif %}{% endfor %}

**Abstract:**
{{ demo.abstract }}

---

{% endfor %}

