---
layout: 2025/page
title: Overview
---

<div class="schedule-container">
  <h2 class="schedule-title">Overview</h2>
  
  <!-- Day Filter Controls -->
  <div class="day-filter-container" role="region" aria-label="Select day">
    <div class="day-buttons" role="tablist" aria-label="Days">
      <button class="day-btn active" role="tab" aria-selected="true" data-day="oct8" onclick="filterByDay('oct8')">
        Oct 8<br><small>Wednesday</small>
      </button>
      <button class="day-btn" role="tab" aria-selected="false" data-day="oct9" onclick="filterByDay('oct9')">
        Oct 9<br><small>Thursday</small>
      </button>
      <button class="day-btn" role="tab" aria-selected="false" data-day="oct10" onclick="filterByDay('oct10')">
        Oct 10<br><small>Friday</small>
      </button>
      <button class="day-btn" role="tab" aria-selected="false" data-day="oct11" onclick="filterByDay('oct11')">
        Oct 11<br><small>Saturday</small>
      </button>
      <button class="day-btn" role="tab" aria-selected="false" data-day="oct12" onclick="filterByDay('oct12')">
        Oct 12<br><small>Sunday</small>
      </button>
    </div>
  </div>


   <div id="sheetWrapper" class="sheet-wrapper day-view day-oct8">
    <!-- Wednesday View (Default) -->
     <iframe 
       id="scheduleIframeOct8"
       src="https://docs.google.com/spreadsheets/d/e/2PACX-1vQrmgHgmh-sZFvt8d_Wz2Ma69b1l4xsuwLbSiNrNKH2BgJmTFTEPLN7fw6HqHWjLKJK7i48kBKjE-K9/pubhtml?gid=801352381&single=true&widget=false&headers=false&chrome=false&range=A1:K7" 
       class="responsive-schedule schedule-view day-oct8 active"
       style="border: none;">
     </iframe>
    
    <!-- Thursday View -->
    <iframe 
      id="scheduleIframeOct9"
       src="https://docs.google.com/spreadsheets/d/e/2PACX-1vQrmgHgmh-sZFvt8d_Wz2Ma69b1l4xsuwLbSiNrNKH2BgJmTFTEPLN7fw6HqHWjLKJK7i48kBKjE-K9/pubhtml?gid=801352381&single=true&widget=false&headers=false&chrome=false&range=A10:I22"
      class="responsive-schedule schedule-view day-oct9"
      style="border: none;">
    </iframe>
    
    <!-- Friday View -->
    <iframe 
      id="scheduleIframeOct10"
       src="https://docs.google.com/spreadsheets/d/e/2PACX-1vQrmgHgmh-sZFvt8d_Wz2Ma69b1l4xsuwLbSiNrNKH2BgJmTFTEPLN7fw6HqHWjLKJK7i48kBKjE-K9/pubhtml?gid=801352381&single=true&widget=false&headers=false&chrome=false&range=A24:I35"
      class="responsive-schedule schedule-view day-oct10"
      style="border: none;">
    </iframe>

    <!-- Saturday View -->
    <iframe 
      id="scheduleIframeOct11"
       src="https://docs.google.com/spreadsheets/d/e/2PACX-1vQrmgHgmh-sZFvt8d_Wz2Ma69b1l4xsuwLbSiNrNKH2BgJmTFTEPLN7fw6HqHWjLKJK7i48kBKjE-K9/pubhtml?gid=801352381&single=true&widget=false&headers=false&chrome=false&range=A37:I47"
      class="responsive-schedule schedule-view day-oct11"
      style="border: none;">
    </iframe>
    
    <!-- Sunday View -->
    <iframe 
      id="scheduleIframeOct12"
       src="https://docs.google.com/spreadsheets/d/e/2PACX-1vQrmgHgmh-sZFvt8d_Wz2Ma69b1l4xsuwLbSiNrNKH2BgJmTFTEPLN7fw6HqHWjLKJK7i48kBKjE-K9/pubhtml?gid=801352381&single=true&widget=false&headers=false&chrome=false&range=A49:I52"
      class="responsive-schedule schedule-view day-oct12"
      style="border: none;">
    </iframe>

  <!-- ===== Program: Oct 9 ===== -->
  <div id="programOct9" class="program-view schedule-view day-oct9">
    <h2 class="schedule-title">Papers per Session</h2>
    {% assign rows = site.data["2025"]["program"]["ProgramISMAR_with_sessions"] %}
    {% assign day_rows = rows | where: "Session Day", "October 9 2025" %}

    {% assign time_keys_str = "" %}
    {% for r in day_rows %}
      {% assign tkey = r["Session Start Time"] | append: "||" | append: r["Session End Time"] %}
      {% unless time_keys_str contains tkey %}{% assign time_keys_str = time_keys_str | append: tkey | append: "~~" %}{% endunless %}
    {% endfor %}
    {% assign time_keys = time_keys_str | split: "~~" | sort %}

    {% for time_key in time_keys %}
      {% if time_key != "" %}
        {% assign parts = time_key | split: "||" %}
        <h2>{{ parts[0] }} - {{ parts[1] }}</h2>

        {% assign session_keys_str = "" %}
        {% for r in day_rows %}
          {% if r["Session Start Time"] == parts[0] and r["Session End Time"] == parts[1] %}
            {% assign skey = r["Session Location"] | append: "||" | append: r["Session Title"] %}
            {% unless session_keys_str contains skey %}{% assign session_keys_str = session_keys_str | append: skey | append: "~~" %}{% endunless %}
          {% endif %}
        {% endfor %}
        {% assign session_keys = session_keys_str | split: "~~" | sort %}

        {% for session_key in session_keys %}
          {% if session_key != "" %}
            {% assign sess = session_key | split: "||" %}
            <h3>{{ sess[1] }} ({{ sess[0] }})</h3>
            <ul class="paper-list">
              {% for r in day_rows %}
                {% if r["Session Start Time"] == parts[0] and r["Session End Time"] == parts[1] and r["Session Title"] == sess[1] and r["Session Location"] == sess[0] %}
                  <li>{{ r["Paper ID"] }}: {{ r["Paper Title"] }}</li>
                {% endif %}
              {% endfor %}
            </ul>
          {% endif %}
        {% endfor %}
      {% endif %}
    {% endfor %}
  </div>

  <!-- ===== Program: Oct 10 ===== -->
  <div id="programOct10" class="program-view schedule-view day-oct10">
    <h2 class="schedule-title">Papers per Session</h2>
    {% assign rows = site.data["2025"]["program"]["ProgramISMAR_with_sessions"] %}
    {% assign day_rows = rows | where: "Session Day", "October 10 2025" %}

    {% assign time_keys_str = "" %}
    {% for r in day_rows %}
      {% assign tkey = r["Session Start Time"] | append: "||" | append: r["Session End Time"] %}
      {% unless time_keys_str contains tkey %}{% assign time_keys_str = time_keys_str | append: tkey | append: "~~" %}{% endunless %}
    {% endfor %}
    {% assign time_keys = time_keys_str | split: "~~" | sort %}

    {% for time_key in time_keys %}
      {% if time_key != "" %}
        {% assign parts = time_key | split: "||" %}
        <h2>{{ parts[0] }} - {{ parts[1] }}</h2>

        {% assign session_keys_str = "" %}
        {% for r in day_rows %}
          {% if r["Session Start Time"] == parts[0] and r["Session End Time"] == parts[1] %}
            {% assign skey = r["Session Location"] | append: "||" | append: r["Session Title"] %}
            {% unless session_keys_str contains skey %}{% assign session_keys_str = session_keys_str | append: skey | append: "~~" %}{% endunless %}
          {% endif %}
        {% endfor %}
        {% assign session_keys = session_keys_str | split: "~~" | sort %}

        {% for session_key in session_keys %}
          {% if session_key != "" %}
            {% assign sess = session_key | split: "||" %}
            <h3>{{ sess[1] }} ({{ sess[0] }})</h3>
            <ul class="paper-list">
              {% for r in day_rows %}
                {% if r["Session Start Time"] == parts[0] and r["Session End Time"] == parts[1] and r["Session Title"] == sess[1] and r["Session Location"] == sess[0] %}
                  <li>{{ r["Paper ID"] }}: {{ r["Paper Title"] }}</li>
                {% endif %}
              {% endfor %}
            </ul>
          {% endif %}
        {% endfor %}
      {% endif %}
    {% endfor %}
  </div>

  <!-- ===== Program: Oct 11 ===== -->
  <div id="programOct11" class="program-view schedule-view day-oct11">
    <h2 class="schedule-title">Papers per Session</h2>
    {% assign rows = site.data["2025"]["program"]["ProgramISMAR_with_sessions"] %}
    {% assign day_rows = rows | where: "Session Day", "October 11 2025" %}

    {% assign time_keys_str = "" %}
    {% for r in day_rows %}
      {% assign tkey = r["Session Start Time"] | append: "||" | append: r["Session End Time"] %}
      {% unless time_keys_str contains tkey %}{% assign time_keys_str = time_keys_str | append: tkey | append: "~~" %}{% endunless %}
    {% endfor %}
    {% assign time_keys = time_keys_str | split: "~~" | sort %}

    {% for time_key in time_keys %}
      {% if time_key != "" %}
        {% assign parts = time_key | split: "||" %}
        <h2>{{ parts[0] }} - {{ parts[1] }}</h2>

        {% assign session_keys_str = "" %}
        {% for r in day_rows %}
          {% if r["Session Start Time"] == parts[0] and r["Session End Time"] == parts[1] %}
            {% assign skey = r["Session Location"] | append: "||" | append: r["Session Title"] %}
            {% unless session_keys_str contains skey %}{% assign session_keys_str = session_keys_str | append: skey | append: "~~" %}{% endunless %}
          {% endif %}
        {% endfor %}
        {% assign session_keys = session_keys_str | split: "~~" | sort %}

        {% for session_key in session_keys %}
          {% if session_key != "" %}
            {% assign sess = session_key | split: "||" %}
            <h3>{{ sess[1] }} ({{ sess[0] }})</h3>
            <ul class="paper-list">
              {% for r in day_rows %}
                {% if r["Session Start Time"] == parts[0] and r["Session End Time"] == parts[1] and r["Session Title"] == sess[1] and r["Session Location"] == sess[0] %}
                  <li>{{ r["Paper ID"] }}: {{ r["Paper Title"] }}</li>
                {% endif %}
              {% endfor %}
            </ul>
          {% endif %}
        {% endfor %}
      {% endif %}
    {% endfor %}
  </div>

  </div> <!-- end #sheetWrapper -->
</div> <!-- end .schedule-container -->

<style>
.schedule-container {
  width: 100%;
  max-width: none; 
  position: relative;
  overflow: hidden;
  margin: 0 auto;
}

.schedule-title {
  text-align: center;
  margin: 0 0 15px 0;
  padding: 0;
  font-size: 1.5em;
  font-weight: bold;
}

/* Day filter */
.day-filter-container {
  margin-bottom: 25px;
  text-align: center;
}

.day-filter-container h3 {
  margin: 0 0 15px 0;
  font-size: 1.2em;
  color: #333;
  font-weight: 600;
}

.day-buttons {
  display: flex;
  align-items: stretch;
  justify-content: center;
  flex-wrap: wrap;
  gap: 8px;
}

.day-btn {
  background: #f8f9fa;
  border: 1px solid #dee2e6;
  color: #333;
  padding: 12px 16px;
  border-radius: 8px;
  cursor: pointer;
  font-size: 14px;
  font-weight: 500;
  transition: all 0.3s ease;
  min-width: 100px;
  text-align: center;
  line-height: 1.3;
  /* prevent layout shift when scrolling */
  flex: 0 0 auto;
}

.day-btn:hover {
  background: #e9ecef;
  border-color: #adb5bd;
  transform: translateY(-1px);
}

.day-btn.active {
  background: #e7f1ff;
  border-color: #91c0ff;
  color: #0d47a1;
}

/* Sheet wrapper */
.sheet-wrapper {
  width: 100%;
  margin: 0 auto 10px auto;
  padding: 0;
}

/* Responsive iframe */
.responsive-schedule {
  width: 100%;
  height: 475px;
  min-height: 400px;
}

@media (max-width: 768px) {
  .responsive-schedule {
    height: 60vh;
  }

  /* Force single-row, horizontally scrollable day tabs on mobile */
  .day-buttons {
    justify-content: flex-start;
    gap: 6px;
    flex-wrap: nowrap;
    overflow-x: auto;
    overflow-y: hidden;
    padding: 4px 8px;
    margin: 0 auto;
    -webkit-overflow-scrolling: touch;
    scroll-snap-type: x mandatory;
    scrollbar-width: none;
    width: 100%;
  }
  .day-buttons::-webkit-scrollbar {
    display: none;
  }

  .day-btn {
    min-width: 84px;
    padding: 10px 12px;
    font-size: 13px;
    scroll-snap-align: center;
    flex: 0 0 auto;                 /* keep items from flexing and wrapping */
  }

  .day-filter-container {
    position: relative;
  }
  .day-filter-container::before,
  .day-filter-container::after {
    content: "";
    position: absolute;
    top: 0;
    bottom: 0;
    width: 18px;
    pointer-events: none;
  }
  .day-filter-container::before {
    left: 0;
    background: linear-gradient(to right, #fff 30%, rgba(255,255,255,0));
  }
  .day-filter-container::after {
    right: 0;
    background: linear-gradient(to left, #fff 30%, rgba(255,255,255,0));
  }
}


/* View toggling */
.schedule-view {
  display: none;
}

.schedule-view.active {
  display: block;
}

/* Day scoping classes for potential overrides */
.day-view.day-oct8 .schedule-view.day-oct8,
.day-view.day-oct9 .schedule-view.day-oct9,
.day-view.day-oct10 .schedule-view.day-oct10,
.day-view.day-oct11 .schedule-view.day-oct11,
.day-view.day-oct12 .schedule-view.day-oct12 {
  /* left available for day specific styling if needed */
}

/* Program list styles */
.program-view {
  position: relative;
  opacity: 0;
  visibility: hidden;
  transition: opacity 0.3s ease, visibility 0.3s ease;
  padding: 16px 12px 24px 12px;
  border-top: 1px solid #e9ecef;
}

.program-view.active {
  opacity: 1;
  visibility: visible;
}

.program-view h2 {
  font-size: 1.1em;
  margin: 14px 0 6px 0;;
}

.program-view h3 {
  font-size: 1.05em;
  margin: 0 0 8px 0;
  color: #333;
  font-weight: 600;
}

.program-view .paper-list {
  margin: 0 0 16px 0;
  padding-left: 18px;
}

.program-view .paper-list li {
  margin: 2px 0;
  line-height: 1.4;
}
</style>

<script>
let currentDay = 'oct8';

function filterByDay(day) {
  currentDay = day;

  document.querySelectorAll('.day-btn').forEach(btn => {
    btn.classList.remove('active');
    btn.setAttribute('aria-selected', 'false');
  });
  const btn = document.querySelector(`[data-day="${day}"]`);
  if (btn) {
    btn.classList.add('active');
    btn.setAttribute('aria-selected', 'true');
    // ensure the active tab is visible and centered on small screens
    btn.scrollIntoView({ behavior: 'smooth', inline: 'center', block: 'nearest' });
  }

  // Hide all iframe and program views
  document.querySelectorAll('.schedule-view').forEach(view => view.classList.remove('active'));

  // Show selected iframe and its program block
  const cap = day.charAt(0).toUpperCase() + day.slice(1);
  const iframe = document.getElementById(`scheduleIframe${cap}`);
  if (iframe) iframe.classList.add('active');
  const program = document.getElementById(`program${cap}`);
  if (program) program.classList.add('active');

  // Update wrapper day class to preserve existing styling behavior
  const wrapper = document.getElementById('sheetWrapper');
  if (wrapper) {
    wrapper.classList.remove('day-oct8', 'day-oct9', 'day-oct10', 'day-oct11', 'day-oct12');
    wrapper.classList.add('day-view', `day-${day}`);
  }
}

// Optional: allow horizontal wheel scroll on the tab strip for desktop trackpads
document.addEventListener('DOMContentLoaded', function() {
  const strip = document.querySelector('.day-buttons');
  if (strip) {
    strip.addEventListener('wheel', function(e) {
      if (Math.abs(e.deltaY) > Math.abs(e.deltaX)) {
        strip.scrollLeft += e.deltaY;
        e.preventDefault();
      }
    }, { passive: false });
  }
});
</script>
