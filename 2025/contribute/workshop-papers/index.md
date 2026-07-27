---
layout: 2025/page
title: Call for Workshop Papers
---
*Last updated: 2025-06-22 1:02AM GMT*

## Overview

This page contains information about the call for workshop papers for ISMAR 2025 for all accepted workshops. Each workshop has its own submission deadline and requirements, so please refer to the specific workshop pages for details.

## Workshops

{% for workshop in site.data["2025"].workshops %}
### {{ workshop.Title }}

{% if workshop.Organizers and workshop.Organizers != '' %}
**Organizers:** {{ workshop.Organizers }}
{% endif %}

{% if workshop.Website %}
**[> Workshop Website]({{ workshop.Website }})**
{% endif %}

#### Abstract  
{{ workshop.Abstract }}

---

{% endfor %}
