---
layout: 2025/page-full-width
title: Overview
---

{% assign idx = site.data["2025"].program.schedule.json.schedule_index.days %}
{% assign all_paper_sessions = site.data["2025"]["program"]["papers"] %}
{% assign all_workshops = site.data["2025"].workshops %}
{% assign papers_page_url = "/2025/program/papers" | relative_url %}
{% assign keynote_page_url = "/2025/program/keynote-speakers/" | relative_url %}
{% assign posters_page_url = "/2025/program/posters/" | relative_url %}
{% assign demos_page_url = "/2025/program/demos/" | relative_url %}
{% assign tutorials_page_url = "/2025/program/tutorials/" | relative_url %}
{% assign pitch_page_url = "/2025/program/pitch-your-lab/" | relative_url %}
{% assign future_faculty_page_url = "/2025/program/Future-Faculty-Forum/" | relative_url %}
{% capture demo_poster_markup %}
<a href="{{ demos_page_url }}">Demo</a> &amp; <a href="{{ posters_page_url }}">Poster</a> Presentation
{% endcapture %}
{% assign demo_poster_markup = demo_poster_markup | strip %}

<div class="schedule_outer">
<div class="schedule" id="schedule-ismar" data-scope="ismar">

  <!-- Tabs -->
  <div class="schedule_tabs" role="tablist" aria-label="Conference days">
    {% for d in idx %}
      <button class="schedule_tab"
              role="tab"
              aria-selected="{% if forloop.first %}true{% else %}false{% endif %}"
              data-day-index="{{ forloop.index0 }}">
        {{ d.label }}
      </button>
    {% endfor %}
  </div>

  <!-- Panels -->
  {% for d in idx %}
    {% assign base = d.file | split: '.json' | first %}
    {% assign day = site.data["2025"].program.schedule.json[base] %}

    {% comment %}
      Build expanded data column labels, one per physical data column to the right of Time.
    {% endcomment %}
    {% capture _data_labels %}
      {% assign seen_time = false %}
      {% for h in day.headers %}
        {% if h.render %}
          {% assign label = h.text %}
          {% assign times = h.colspan | default: 1 %}
          {% for i in (1..times) %}
            {% if forloop.parentloop.index0 > 0 or i > 1 or seen_time %}
              {{ label }}||
            {% else %}
              {% assign seen_time = true %}
              {% comment %} skip pushing Time into data labels {% endcomment %}
            {% endif %}
          {% endfor %}
        {% endif %}
      {% endfor %}
    {% endcapture %}
    {% assign data_labels = _data_labels | split: "||" | reject: "" %}

    <section class="schedule_panel"
             role="tabpanel"
             aria-hidden="{% if forloop.first %}false{% else %}true{% endif %}">

      <!-- Table view -->
      <div class="schedule_table_outer view_table">
        <div class="schedule_table_scroll schedule_table_wrap">
        <table class="schedule_table">
          <thead>
            <tr>
              {% for h in day.headers %}
                {% if h.render %}
                  <th{% if h.colspan > 1 %} colspan="{{ h.colspan }}"{% endif %}>{{ h.text }}</th>
                {% endif %}
              {% endfor %}
            </tr>
          </thead>
          <tbody>
            {% for row in day.rows %}
              <tr>
                <td class="timecell">{{ row.time }}</td>
                {% for cell in row.cells %}
                  {% if cell.render %}
                    {% assign text_clean = cell.text | strip | strip_newlines %}
                    {% assign cell_display_html = cell.text %}
                    {% assign cell_link_url = "" %}
                    {% if text_clean != "" %}
                      {% unless cell.text contains '<a' %}
                        {% assign text_norm = text_clean | downcase %}
                        {% if text_norm == 'demo & poster presentation' %}
                          {% assign cell_display_html = demo_poster_markup %}
                        {% else %}
                          {% assign first_word = text_norm | split: ' ' | first %}
                          {% if first_word == 'keynote' %}
                            {% assign cell_link_url = keynote_page_url %}
                          {% elsif text_norm == 'future faculty forum' %}
                            {% assign cell_link_url = future_faculty_page_url %}
                          {% elsif text_norm == 'pitch your lab' %}
                            {% assign cell_link_url = pitch_page_url %}
                          {% elsif first_word == 'tutorial:' %}
                            {% assign cell_link_url = tutorials_page_url %}
                          {% endif %}
                          {% if cell_link_url == "" %}
                            {% for paper_session in all_paper_sessions %}
                              {% assign session_title = paper_session["Session Title"] | strip %}
                              {% assign session_title_norm = session_title | downcase %}
                              {% if session_title_norm == text_norm %}
                                {% assign anchor_raw = paper_session["Session Day"] | append: '-' | append: paper_session["Session Start Time"] | append: '-' | append: paper_session["Session End Time"] | append: '-' | append: paper_session["Session Location"] | append: '-' | append: session_title %}
                                {% assign anchor_slug = anchor_raw | slugify %}
                                {% assign cell_link_url = papers_page_url | append: '#' | append: anchor_slug %}
                                {% break %}
                              {% endif %}
                            {% endfor %}
                          {% endif %}
                          {% if cell_link_url == "" and text_clean contains "Workshop:" %}
                            {% assign session_suffix = text_clean | replace_first: "Workshop:", "" | strip %}
                            {% assign suffix_norm = session_suffix | downcase | replace: "’", "" | replace: "‘", "" | replace: "'", "" %}
                            {% if suffix_norm != "" %}
                              {% for workshop in all_workshops %}
                                {% if cell_link_url == "" %}
                                  {% assign title_prefix = workshop.Title | split: ":" | first | strip %}
                                  {% assign title_prefix_norm = title_prefix | downcase | replace: "’", "" | replace: "‘", "" | replace: "'", "" %}
                                  {% assign title_full_norm = workshop.Title | downcase | replace: "’", "" | replace: "‘", "" | replace: "'", "" %}
                                  {% if title_prefix_norm != "" %}
                                    {% if suffix_norm contains title_prefix_norm or title_prefix_norm contains suffix_norm %}
                                      {% if workshop.Website and workshop.Website != "" %}
                                        {% assign cell_link_url = workshop.Website %}
                                      {% endif %}
                                    {% endif %}
                                  {% endif %}
                                  {% if cell_link_url == "" and title_full_norm != "" %}
                                    {% if suffix_norm contains title_full_norm or title_full_norm contains suffix_norm %}
                                      {% if workshop.Website and workshop.Website != "" %}
                                        {% assign cell_link_url = workshop.Website %}
                                      {% endif %}
                                    {% endif %}
                                  {% endif %}
                                {% endif %}
                              {% endfor %}
                            {% endif %}
                          {% endif %}
                          {% if cell_link_url != "" %}
                            {% capture tmp_cell_link %}<a href="{{ cell_link_url }}">{{ cell.text }}</a>{% endcapture %}
                            {% assign cell_display_html = tmp_cell_link | strip %}
                          {% endif %}
                        {% endif %}
                      {% endunless %}
                    {% endif %}
                    <td{% if cell.rowspan > 1 %} rowspan="{{ cell.rowspan }}"{% endif %}
                        {% if cell.colspan > 1 %} colspan="{{ cell.colspan }}"{% endif %}
                        data-text="{{ text_clean }}">
                      {{ cell_display_html }}
                    </td>
                  {% endif %}
                {% endfor %}
              </tr>
            {% endfor %}
          </tbody>
        </table>
        </div>
      </div>

      <!-- Cards view -->
      <div class="schedule_cards_wrap view_cards">
        {% for row in day.rows %}
          {% assign r_index = forloop.index0 %}
          {% comment %}
            Collect all anchor cells active at this time slot.
          {% endcomment %}
          {% assign active_keys = "" %}
          {% for rr in (0..r_index) %}
            {% assign dist = r_index | minus: rr | plus: 1 %}
            {% assign prow = day.rows[rr] %}
            {% for cell in prow.cells %}
              {% assign cj = forloop.index0 %}
              {% if cell.render and cell.text and cell.text != "" and cell.rowspan >= dist %}
                {% capture active_keys %}{{ active_keys }}{{ rr }}|{{ cj }}||{% endcapture %}
              {% endif %}
            {% endfor %}
          {% endfor %}
          {% assign key_list = active_keys | split: "||" | reject: "" %}

          {% if key_list.size > 0 %}
            <div class="slot">
              <div class="slot_time">{{ row.time }}</div>
              <div class="slot_cards">
                {% assign printed = "" %}
                {%- comment -%} Reorder keys so that any card whose title contains "Exhibition" is rendered last {%- endcomment -%}
                {% assign non_exhibition = "" %}
                {% assign exhibition_keys = "" %}
                {% for key in key_list %}
                  {% assign parts = key | split: "|" %}
                  {% assign rr_tmp = parts[0] | plus: 0 %}
                  {% assign cj_tmp = parts[1] | plus: 0 %}
                  {% assign acell_tmp = day.rows[rr_tmp].cells[cj_tmp] %}
                  {% assign txt_tmp = acell_tmp.text | strip | strip_newlines %}
                  {% if txt_tmp contains "Exhibition" %}
                    {% capture exhibition_keys %}{{ exhibition_keys }}{{ key }}||{% endcapture %}
                  {% else %}
                    {% capture non_exhibition %}{{ non_exhibition }}{{ key }}||{% endcapture %}
                  {% endif %}
                {% endfor %}
                {% assign key_list_ordered = non_exhibition | append: exhibition_keys | split: "||" | reject: "" %}
                {% for key in key_list_ordered %}
                  {% assign parts = key | split: "|" %}
                  {% assign rr = parts[0] | plus: 0 %}
                  {% assign cj = parts[1] | plus: 0 %}
                  {% assign acell = day.rows[rr].cells[cj] %}
                  {% assign span = acell.colspan | default: 1 %}
                  {% assign text_clean = acell.text | strip | strip_newlines %}
                  {% assign card_title_html = acell.text %}
                  {% assign card_link_url = "" %}
                  {% if text_clean != "" %}
                    {% unless acell.text contains '<a' %}
                      {% assign text_norm = text_clean | downcase %}
                      {% if text_norm == 'demo & poster presentation' %}
                        {% assign card_title_html = demo_poster_markup %}
                      {% else %}
                        {% assign first_word = text_norm | split: ' ' | first %}
                        {% if first_word == 'keynote' %}
                          {% assign card_link_url = keynote_page_url %}
                        {% elsif text_norm == 'future faculty forum' %}
                          {% assign card_link_url = future_faculty_page_url %}
                        {% elsif text_norm == 'pitch your lab' %}
                          {% assign card_link_url = pitch_page_url %}
                        {% elsif first_word == 'tutorial:' %}
                          {% assign card_link_url = tutorials_page_url %}
                        {% endif %}
                        {% if card_link_url == "" %}
                          {% for paper_session in all_paper_sessions %}
                            {% assign session_title = paper_session["Session Title"] | strip %}
                            {% assign session_title_norm = session_title | downcase %}
                            {% if session_title_norm == text_norm %}
                              {% assign anchor_raw = paper_session["Session Day"] | append: '-' | append: paper_session["Session Start Time"] | append: '-' | append: paper_session["Session End Time"] | append: '-' | append: paper_session["Session Location"] | append: '-' | append: session_title %}
                              {% assign anchor_slug = anchor_raw | slugify %}
                              {% assign card_link_url = papers_page_url | append: '#' | append: anchor_slug %}
                              {% break %}
                            {% endif %}
                          {% endfor %}
                        {% endif %}
                        {% if card_link_url == "" and text_clean contains "Workshop:" %}
                          {% assign session_suffix = text_clean | replace_first: "Workshop:", "" | strip %}
                          {% assign suffix_norm = session_suffix | downcase | replace: "’", "" | replace: "‘", "" | replace: "'", "" %}
                          {% if suffix_norm != "" %}
                            {% for workshop in all_workshops %}
                              {% if card_link_url == "" %}
                                {% assign title_prefix = workshop.Title | split: ":" | first | strip %}
                                {% assign title_prefix_norm = title_prefix | downcase | replace: "’", "" | replace: "‘", "" | replace: "'", "" %}
                                {% assign title_full_norm = workshop.Title | downcase | replace: "’", "" | replace: "‘", "" | replace: "'", "" %}
                                {% if title_prefix_norm != "" %}
                                  {% if suffix_norm contains title_prefix_norm or title_prefix_norm contains suffix_norm %}
                                    {% if workshop.Website and workshop.Website != "" %}
                                      {% assign card_link_url = workshop.Website %}
                                    {% endif %}
                                  {% endif %}
                                {% endif %}
                                {% if card_link_url == "" and title_full_norm != "" %}
                                  {% if suffix_norm contains title_full_norm or title_full_norm contains suffix_norm %}
                                    {% if workshop.Website and workshop.Website != "" %}
                                      {% assign card_link_url = workshop.Website %}
                                    {% endif %}
                                  {% endif %}
                                {% endif %}
                              {% endif %}
                            {% endfor %}
                          {% endif %}
                        {% endif %}
                        {% if card_link_url != "" %}
                          {% capture tmp_card_link %}<a href="{{ card_link_url }}">{{ acell.text }}</a>{% endcapture %}
                          {% assign card_title_html = tmp_card_link | strip %}
                        {% endif %}
                      {% endif %}
                    {% endunless %}
                  {% endif %}

                  {% comment %} Deduplicate this anchor {% endcomment %}
                  {% assign uniq_id = rr | append: "-" | append: cj %}
                  {% if printed contains uniq_id %}
                    {% continue %}
                  {% endif %}
                  {% capture printed %}{{ printed }} {{ uniq_id }} {% endcapture %}

                  {% comment %} Full session time from start row to end row covered by rowspan {% endcomment %}
                  {% assign start_slot = day.rows[rr].time %}
                  {% assign start_time = start_slot | split: "~" | first | strip %}
                  {% assign rowspan_val = acell.rowspan | default: 1 %}
                  {% assign rowspan_val = rowspan_val | plus: 0 %}
                  {% assign end_index = rr | plus: rowspan_val | minus: 1 %}
                  {% assign end_slot = day.rows[end_index].time %}
                  {% assign end_time = end_slot | split: "~" | last | strip %}
                  {% assign full_time = start_time | append: "~" | append: end_time %}

                  {% comment %} Suppress room label for Coffee Break and Lunch {% endcomment %}
                  {% assign show_room = true %}
                  {% if text_clean == "Coffee Break" or text_clean == "Lunch" %}
                    {% assign show_room = false %}
                  {% endif %}

                  {% comment %}
                    Special case: Welcome Reception — take room label from parentheses
                  {% endcomment %}
                  {% assign override_room = "" %}
                  {% if show_room and text_clean contains "Welcome Reception" and text_clean contains "(" and text_clean contains ")" %}
                    {% assign after_open = text_clean | split: "(" | last %}
                    {% assign inside_paren = after_open | split: ")" | first | strip %}
                    {% assign override_room = inside_paren %}
                  {% endif %}

                  {% comment %}
                    Default room labels from header slice [cj .. cj+span-1] if not overridden.
                  {% endcomment %}
                  {% assign room_display = "" %}
                  {% if show_room %}
                    {% if override_room != "" %}
                      {% assign room_display = override_room %}
                    {% else %}
                      {% assign rooms_concat = "" %}
                      {% for label in data_labels limit: span offset: cj %}
                        {% if label != "" %}
                          {% capture rooms_concat %}{{ rooms_concat }}{{ label }}||{% endcapture %}
                        {% endif %}
                      {% endfor %}
                      {% assign room_names = rooms_concat | split: "||" | reject: "" | uniq %}
                      {% assign room_display = room_names | join: ", " %}
                    {% endif %}
                  {% endif %}

                  <div class="card" data-text="{{ text_clean }}">
                    <div class="card_title">{{ card_title_html }}</div>
                    <div class="card_meta">
                      <span class="card_time">{{ full_time }}</span>
                      {% if show_room and room_display != "" %}
                        <span class="card_room">{{ room_display }}</span>
                      {% endif %}
                    </div>
                  </div>
                {% endfor %}
              </div>
            </div>
          {% endif %}
        {% endfor %}
      </div>
    </section>
  {% endfor %}
 </div>
</div>

<style>
:root {
  --c-white: rgb(255, 255, 255);
  --c-text-dark: rgb(0, 0, 0);
  --c-nonempty: rgb(235, 244, 250);
  --c-tutorial: rgb(236, 244, 229);
  --c-doccons: rgba(244, 229, 229, 1);
  --c-keynote: rgba(241, 241, 220, 1);
  --c-ceremony: rgb(249, 239, 229);
  --c-demo-poster: rgb(228, 242, 229);
  --c-future-faculty-forum: rgba(206, 212, 243, 1);
  --c-exhibition-bg: rgb(110, 135, 95);
  --c-exhibition-fg: rgb(255, 255, 255);
  --c-pitch-your-lab: rgba(224, 224, 224, 1);
}


/* Layout container for full-width page */
.schedule_outer { max-width: 1300px; margin: 0 auto; padding: 2.5rem 1.25rem 3.5rem; }
.schedule_outer:before { content: ""; display: block; }

/* Tabs */
/* Tabs (day selector) */
.schedule_tabs { position: relative; display: flex; gap: .5rem; margin-bottom: 1.1rem; flex-wrap: nowrap; overflow-x: auto; -webkit-overflow-scrolling: touch; scroll-snap-type: x mandatory; padding: 0 0 .35rem; }
.schedule_tabs:before, .schedule_tabs:after { content: ""; position: sticky; top: 0; width: 34px; flex: 0 0 34px; pointer-events: none; }
.schedule_tabs:before { left: 0; margin-left: -34px; background: linear-gradient(to right, var(--c-white, #fff), rgba(255,255,255,0)); opacity: 0; transition: opacity .25s; }
.schedule_tabs:after { right: 0; margin-right: -34px; background: linear-gradient(to left, var(--c-white, #fff), rgba(255,255,255,0)); opacity: 0; transition: opacity .25s; }
.schedule_tabs.has-left:before { opacity: 1; }
.schedule_tabs.has-right:after { opacity: 1; }
.schedule_tabs::-webkit-scrollbar { height: 6px; }
.schedule_tab {
  scroll-snap-align: start; padding: .6rem .9rem; border: 1px solid #ccc; background: #f8f8f8;
  cursor: pointer; white-space: nowrap; flex: 0 0 auto; border-radius: .375rem;
}
.schedule_tab[aria-selected="true"] { background: #fff; border-bottom-color: #fff; font-weight: 600; }
.schedule_tabs::-webkit-scrollbar { height: 6px; }
.schedule_tabs::-webkit-scrollbar-track { background: transparent; }
.schedule_tabs::-webkit-scrollbar-thumb { background: rgba(0,0,0,.15); border-radius: 3px; }
@media (max-width: 900px) {
  .schedule_tabs { scrollbar-width: none; -ms-overflow-style: none; }
  .schedule_tabs::-webkit-scrollbar { display: none; }
}

/* Panels */
.schedule_panel { display: none; }
.schedule_panel[aria-hidden="false"] { display: block; }

/* Table */
.schedule_table_outer { position: relative; }
.schedule_table_scroll { display: none; overflow-x: auto; -webkit-overflow-scrolling: touch; }
/* Scroll affordance anchored to outer container */
.schedule_table_outer:after { content: ""; position: absolute; top: 0; right: 0; width: 54px; height: 100%; pointer-events: none; background: linear-gradient(to left, rgba(255,255,255,.97), rgba(255,255,255,0)); opacity: 0; transition: opacity .25s; }
.schedule_table_outer:before { content: "›"; position: absolute; top: 50%; transform: translateY(-50%); right: 14px; font-size: 1.55rem; line-height: 1; color: #555; opacity: 0; transition: opacity .25s; font-weight: 400; font-family: system-ui, sans-serif; text-shadow: 0 0 2px rgba(255,255,255,.55); }
.schedule_table_scroll.has-right ~ :is(:before,:after) {}
.schedule_table_scroll.has-right ~ * {}
.schedule_table_outer.has-right:after, .schedule_table_outer.has-right:before { opacity: 1; }
.schedule_table { border-collapse: collapse; width: 100%; table-layout: fixed; min-width: 1100px; font-size: .9rem; }
.schedule_table th, .schedule_table td {
  border: 1px solid #ddd; padding: .5rem; vertical-align: middle; text-align: center;
  word-break: break-word; overflow-wrap: anywhere;
}
.schedule_table th { background: #333; color: #fff; font-weight: 600; }
.schedule_table th:first-child { background: #fff; color: #000; }
.timecell { white-space: nowrap; }
@media (min-width: 900px) {
  .schedule_table th:first-child, .schedule_table td:first-child {
    position: sticky; left: 0; z-index: 2; background: #fff; border-right: 2px solid #ddd;
  }
}

/* Desktop cell colors */
.schedule_table tbody td[data-text] { background: var(--c-nonempty); }
.schedule_table tbody td[data-text=""],
.schedule_table tbody td[data-text="Coffee Break" i],
.schedule_table tbody td[data-text="Lunch" i] { background: var(--c-white); color: var(--c-text-dark); font-style: italic; }
.schedule_table tbody td[data-text^="Tutorial" i] { background: var(--c-tutorial); }
.schedule_table tbody td[data-text*="Doctoral Consortium" i] { background: var(--c-doccons); }
.schedule_table tbody td[data-text^="Keynote" i] { background: var(--c-keynote); }
.schedule_table tbody td[data-text$="Ceremony" i] { background: var(--c-ceremony); }
.schedule_table tbody td[data-text*="Demo & Poster Presentation" i] { background: var(--c-demo-poster); }
.schedule_table tbody td[data-text*="Exhibition" i] { background: var(--c-exhibition-bg); color: var(--c-exhibition-fg); }
.schedule_table tbody td[data-text*="Future Faculty Forum" i] { background: var(--c-future-faculty-forum); }
.schedule_table tbody td[data-text*="Pitch Your Lab" i] { background: var(--c-pitch-your-lab); }
.schedule_table tbody td[data-text*="Reception" i] { background: --var(--c-ceremony); }

/* Cards */
.schedule_cards_wrap { display: none; }
.slot { border: 1px solid #e6e6e6; border-radius: .5rem; margin-bottom: .8rem; background: #fff; overflow: hidden; }
.slot_time { font-weight: 600; padding: .6rem .75rem; border-bottom: 1px solid #eee; background: #fafafa; position: sticky; top: 0; }
.slot_cards { display: grid; grid-template-columns: 1fr; gap: .5rem; padding: .6rem .75rem; }
.card { border: 1px solid #e6e6e6; border-radius: .5rem; padding: .5rem .6rem; word-break: break-word; overflow-wrap: anywhere; background: var(--c-white) !important; }
.card_title { font-weight: 600; margin-bottom: .25rem; }
.card_meta { font-size: .9rem; color: #333; display: flex; gap: .5rem; flex-wrap: wrap; }
.card_time { background: #eef3ff; padding: .15rem .4rem; border-radius: .25rem; }
.card_room { background: #f2f2f2; padding: .15rem .4rem; border-radius: .25rem; }

/* Card colors */
.card[data-text^="Tutorial" i] { background: var(--c-tutorial) !important; }
.card[data-text*="Doctoral Consortium" i] { background: var(--c-doccons) !important; }
.card[data-text^="Keynote" i] { background: var(--c-keynote) !important; }
.card[data-text$="Ceremony" i] { background: var(--c-ceremony) !important; }
.card[data-text*="Demo & Poster Presentation" i] { background: var(--c-demo-poster) !important; }
.card[data-text*="Exhibition" i] { background: var(--c-exhibition-bg) !important; color: var(--c-exhibition-fg) !important; }
.card[data-text*="Future Faculty Forum" i] { background: var(--c-future-faculty-forum) !important; }
.card[data-text*="Pitch Your Lab" i] { background: var(--c-pitch-your-lab) !important; }
.card[data-text*="Reception" i] { background: var(--c-ceremony) !important; }

/* Responsive view selection (auto) */
@media (min-width: 800px) { .view_table { display: block; } .schedule_table_scroll { display: block; } }
@media (max-width: 799px) { .view_cards { display: block; } }
</style>

<script>
(function() {
  const root = document.getElementById('schedule-ismar');
  if (!root) return;

  // Tabs logic
  const tabs = root.querySelectorAll('.schedule_tab');
  const panels = root.querySelectorAll('.schedule_panel');
  function showPanel(i) {
    tabs.forEach((t, idx) => t.setAttribute('aria-selected', idx === i ? 'true' : 'false'));
    panels.forEach((p, idx) => p.setAttribute('aria-hidden', idx === i ? 'false' : 'true'));
    const active = tabs[i];
    if (active && active.scrollIntoView) active.scrollIntoView({ inline: 'nearest', block: 'nearest' });
  }
  tabs.forEach((btn, i) => btn.addEventListener('click', () => showPanel(i)));
  showPanel(0);

  // Swipe between panels on mobile
  let startX = null;
  panels.forEach((panel, i) => {
    panel.addEventListener('touchstart', e => { startX = e.touches[0].clientX; }, { passive: true });
    panel.addEventListener('touchend', e => {
      if (startX === null) return;
      const dx = e.changedTouches[0].clientX - startX;
      startX = null;
      const threshold = 50;
      if (dx > threshold && i > 0) showPanel(i - 1);
      if (dx < -threshold && i < panels.length - 1) showPanel(i + 1);
    }, { passive: true });
  });

  // Dynamic fade handling for scrollable areas (tabs + table wrappers)
  function applyFadeLogic(el) {
    if (!el) return;
    const atEnd = Math.ceil(el.scrollLeft + el.clientWidth) >= el.scrollWidth - 1; // small tolerance
    let atStart = el.scrollLeft <= 0;
    // Additional: treat as start if first child fully visible (accounts for internal offsets)
    const first = el.querySelector(':scope > *');
    if (!atStart && first) {
      const cr = el.getBoundingClientRect();
      const fr = first.getBoundingClientRect();
      if (fr.left >= cr.left - 1) atStart = true; // tolerance
    }
    el.classList.toggle('has-left', !atStart);
    el.classList.toggle('has-right', !atEnd);
  }
  const tabBar = root.querySelector('.schedule_tabs');
  tabBar && tabBar.addEventListener('scroll', () => applyFadeLogic(tabBar), { passive: true });
  const tableScrolls = root.querySelectorAll('.schedule_table_scroll');
  tableScrolls.forEach(w => w.addEventListener('scroll', () => {
    applyFadeLogic(w);
    const outer = w.closest('.schedule_table_outer');
    if (outer) {
      // Mirror right/left classes to outer for fade styling
      outer.classList.toggle('has-left', w.classList.contains('has-left'));
      outer.classList.toggle('has-right', w.classList.contains('has-right'));
    }
  }, { passive: true }));
  window.addEventListener('resize', () => {
    applyFadeLogic(tabBar);
  tableScrolls.forEach(w => { applyFadeLogic(w); const outer = w.closest('.schedule_table_outer'); if (outer) { outer.classList.toggle('has-left', w.classList.contains('has-left')); outer.classList.toggle('has-right', w.classList.contains('has-right')); } });
  });
  // Initial
  requestAnimationFrame(() => {
    applyFadeLogic(tabBar);
  tableScrolls.forEach(w => { applyFadeLogic(w); const outer = w.closest('.schedule_table_outer'); if (outer) { outer.classList.toggle('has-left', w.classList.contains('has-left')); outer.classList.toggle('has-right', w.classList.contains('has-right')); } });
  });
})();
</script>
