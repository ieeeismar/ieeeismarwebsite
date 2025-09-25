---
layout: 2025/page
title: Overview
---

<div class="schedule-container">
  <h2 class="schedule-title">Overview</h2>
  
  <!-- Day Filter Controls -->
  <div class="day-filter-container">
    <div class="day-buttons">
      <button class="day-btn active" data-day="oct8" onclick="filterByDay('oct8')">
        Oct 8<br><small>Wednesday</small>
      </button>
      <button class="day-btn" data-day="oct9" onclick="filterByDay('oct9')">
        Oct 9<br><small>Thursday</small>
      </button>
      <button class="day-btn" data-day="oct10" onclick="filterByDay('oct10')">
        Oct 10<br><small>Friday</small>
      </button>
      <button class="day-btn" data-day="oct11" onclick="filterByDay('oct11')">
        Oct 11<br><small>Saturday</small>
      </button>
      <button class="day-btn" data-day="oct12" onclick="filterByDay('oct12')">
        Oct 12<br><small>Sunday</small>
      </button>
    </div>
  </div>


  <div id="sheetWrapper" class="sheet-wrapper day-view day-oct8">
    <!-- Wednesday View (Default) -->
     <iframe 
       id="scheduleIframeOct8"
       src="https://docs.google.com/spreadsheets/d/e/2PACX-1vQLAYxqi2N2MTBVbLWYeZk4A-2maDFJaKOePPVqgjoFYPpFGPFR4MWZZhEH4AqDHVScOKdw5KzqgmVf/pubhtml?gid=867229992&widget=true&headers=false&chrome=false" 
       class="responsive-schedule schedule-view day-oct8 active"
       style="border: none;">
     </iframe>
    
    <!-- Thursday View -->
    <iframe 
      id="scheduleIframeOct9"
      src="https://docs.google.com/spreadsheets/d/e/2PACX-1vQLAYxqi2N2MTBVbLWYeZk4A-2maDFJaKOePPVqgjoFYPpFGPFR4MWZZhEH4AqDHVScOKdw5KzqgmVf/pubhtml?gid=1496491388&single=true&widget=false&headers=false&chrome=false&rm=minimal&range=A10:I22" 
      class="responsive-schedule schedule-view day-oct9"
      style="border: none;">
    </iframe>
    
    <!-- Friday View -->
    <iframe 
      id="scheduleIframeOct10"
      src="https://docs.google.com/spreadsheets/d/e/2PACX-1vQLAYxqi2N2MTBVbLWYeZk4A-2maDFJaKOePPVqgjoFYPpFGPFR4MWZZhEH4AqDHVScOKdw5KzqgmVf/pubhtml?gid=1496491388&single=true&widget=false&headers=false&chrome=false&rm=minimal&range=A24:I35" 
      class="responsive-schedule schedule-view day-oct10"
      style="border: none;">
    </iframe>
    
    <!-- Saturday View -->
    <iframe 
      id="scheduleIframeOct11"
      src="https://docs.google.com/spreadsheets/d/e/2PACX-1vQLAYxqi2N2MTBVbLWYeZk4A-2maDFJaKOePPVqgjoFYPpFGPFR4MWZZhEH4AqDHVScOKdw5KzqgmVf/pubhtml?gid=1496491388&single=true&widget=false&headers=false&chrome=false&rm=minimal&range=A37:I47" 
      class="responsive-schedule schedule-view day-oct11"
      style="border: none;">
    </iframe>
    
    <!-- Sunday View -->
    <iframe 
      id="scheduleIframeOct12"
      src="https://docs.google.com/spreadsheets/d/e/2PACX-1vQLAYxqi2N2MTBVbLWYeZk4A-2maDFJaKOePPVqgjoFYPpFGPFR4MWZZhEH4AqDHVScOKdw5KzqgmVf/pubhtml?gid=1496491388&single=true&widget=false&headers=false&chrome=false&rm=minimal&range=A49:I52" 
      class="responsive-schedule schedule-view day-oct12"
      style="border: none;">
    </iframe>
  </div>
</div>

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
  color: #333;
}

/* Day Filter Styling */
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
  justify-content: center;
  gap: 8px;
  flex-wrap: wrap;
  margin-bottom: 10px;
}

.day-btn {
  background: #f8f9fa;
  color: #495057;
  border: 2px solid #dee2e6;
  padding: 12px 16px;
  border-radius: 8px;
  cursor: pointer;
  font-size: 14px;
  font-weight: 500;
  transition: all 0.3s ease;
  min-width: 100px;
  text-align: center;
  line-height: 1.3;
}

.day-btn:hover {
  background: #e9ecef;
  border-color: #adb5bd;
  transform: translateY(-2px);
  box-shadow: 0 4px 8px rgba(0,0,0,0.1);
}

.day-btn.active {
  background: #007bff;
  color: white;
  border-color: #007bff;
  box-shadow: 0 4px 12px rgba(0,123,255,0.3);
}

.day-btn small {
  display: block;
  font-size: 11px;
  opacity: 0.8;
  margin-top: 2px;
}


/* Sheet Wrapper */
.sheet-wrapper {
  position: relative;
  border: 2px solid #e0e0e0;
  border-radius: 8px;
  overflow: hidden;
  background: white;
  box-shadow: 0 2px 10px rgba(0,0,0,0.1);
}

.responsive-schedule {
  width: 100%;
  height: auto; 
  min-height: 400px;
  max-height: none;
  transition: transform 0.3s ease;
}

/* Schedule View Control */
.schedule-view {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  opacity: 0;
  visibility: hidden;
  transition: opacity 0.3s ease, visibility 0.3s ease;
}

.schedule-view.active {
  opacity: 1;
  visibility: visible;
}

/* Dynamic height for day-specific views */
.sheet-wrapper.day-view .responsive-schedule {
  width: 100%;
  height: auto;
  min-height: 350px;
  max-height: 600px;
}

/* Custom heights and scaling for each day to show full table */
.sheet-wrapper.day-view.day-oct8 .responsive-schedule {
  height: 500px;
  min-height: 500px;
  max-height: 500px;
  transform: scale(0.85);
  transform-origin: top left;
  width: 100%;
  height: 117.65%;
}

.sheet-wrapper.day-view.day-oct9 .responsive-schedule {
  height: 600px;
  min-height: 600px;
  max-height: 600px;
  transform: scale(0.85);
  transform-origin: top left;
  width: 100%;
  height: 117.65%;
}

.sheet-wrapper.day-view.day-oct10 .responsive-schedule {
  height: 600px;
  min-height: 600px;
  max-height: 600px;
  transform: scale(0.85);
  transform-origin: top left;
  width: 100%;
  height: 117.65%;
}

.sheet-wrapper.day-view.day-oct11 .responsive-schedule {
  height: 600px;
  min-height: 600px;
  max-height: 600px;
  transform: scale(0.85);
  transform-origin: top left;
  width: 100%;
  height: 117.65%;
}

.sheet-wrapper.day-view.day-oct12 .responsive-schedule {
  height: 500px;
  min-height: 500px;
  max-height: 500px;
  transform: scale(0.85);
  transform-origin: top left;
  width: 100%;
  height: 117.65%;
}

/* Remove the white space overlay for day views */
.sheet-wrapper.day-view::after {
  display: none;
}

/* Adjust container height for day views */
.sheet-wrapper.day-view {
  width: 100vw;
  height: auto;
  min-height: 400px;
  max-height: 600px;
  overflow: hidden;
  margin: 0;
  margin-left: 0;
  border: none;
  border-radius: 0;
  box-shadow: none;
}

/* Very small mobile devices */
@media (max-width: 480px) {
  .sheet-wrapper.day-view {
    max-height: 70vh;
  }
  
  .sheet-wrapper.day-view.day-oct9 .responsive-schedule,
  .sheet-wrapper.day-view.day-oct10 .responsive-schedule,
  .sheet-wrapper.day-view.day-oct11 .responsive-schedule {
    min-height: 500px;
  }
}


.schedule-container::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  height: 30px;
  background: white;
  z-index: 1;
  pointer-events: none;
}

/* Mobile devices */
@media (max-width: 768px) {
  .schedule-container {
    width: 100vw; 
    margin-left: calc(50% - 50vw); 
  }
  
  .responsive-schedule {
    height: auto;
    min-height: 400px;
  }
  
  .schedule-title {
    font-size: 1.3em;
    margin-bottom: 10px;
  }
  
  .day-buttons {
    flex-direction: column;
    align-items: center;
    gap: 8px;
  }
  
  .day-btn {
    width: 200px;
    padding: 15px 20px;
    font-size: 16px;
    min-width: 200px;
  }
  
  .day-btn small {
    font-size: 12px;
  }
  
  /* Fix scrolling for day views on mobile */
  .sheet-wrapper.day-view {
    width: 100%;
    margin-left: 0;
    overflow: auto;
    max-height: 80vh;
  }
  
  .sheet-wrapper.day-view.day-oct9 .responsive-schedule,
  .sheet-wrapper.day-view.day-oct10 .responsive-schedule,
  .sheet-wrapper.day-view.day-oct11 .responsive-schedule {
    height: auto;
    min-height: 600px;
    max-height: none;
    transform: none;
    width: 100%;
  }
  
  .sheet-wrapper.day-view.day-oct8 .responsive-schedule,
  .sheet-wrapper.day-view.day-oct12 .responsive-schedule {
    height: auto;
    min-height: 400px;
    max-height: none;
    transform: none;
    width: 100%;
  }
}

/* Tablets and small desktops */
@media (min-width: 769px) and (max-width: 1199px) {
  .schedule-container {
    width: 95vw; 
    margin-left: calc(50% - 47.5vw); 
  }
}

/* Large desktops */
@media (min-width: 1200px) {
  .schedule-container {
    width: 90vw; 
    margin-left: calc(50% - 40vw); 
    max-width: 1400px; /* Add max-width for better centering on very large screens */
  }
  
  .schedule-title {
    font-size: 1.6em;
    text-align: left;
    margin-left: 0;
    margin-right: 0;
  }
  
  .day-filter-container {
    text-align: left;
    margin-left: 0;
    margin-right: 0;
  }
  
  .day-buttons {
    justify-content: flex-start;
  }
  
  .responsive-schedule {
    height: auto;
    max-height: none;
  }
}

/* Extra large screens */
@media (min-width: 1600px) {
  .schedule-container {
    width: 85vw; 
    margin-left: calc(50% - 37.5vw); 
    max-width: 1600px; /* Constrain width for better table centering */
  }
  
  .schedule-title {
    font-size: 1.7em;
    text-align: left;
    margin-left: 0;
    margin-right: 0;
  }
  
  .day-filter-container {
    text-align: left;
    margin-left: 0;
    margin-right: 0;
  }
  
  .day-buttons {
    justify-content: flex-start;
  }
  
  .responsive-schedule {
    height: auto;
    max-height: none;
  }
}

/* Ultra-wide screens */
@media (min-width: 2000px) {
  .schedule-container {
    width: 80vw; 
    margin-left: calc(50% - 35vw); 
    max-width: 1800px; /* Constrain width for optimal table centering on ultra-wide screens */
  }
  
  .schedule-title {
    font-size: 1.8em;
    text-align: left;
    margin-left: 0;
    margin-right: 0;
  }
  
  .day-filter-container {
    text-align: left;
    margin-left: 0;
    margin-right: 0;
  }
  
  .day-buttons {
    justify-content: flex-start;
  }
  
  .responsive-schedule {
    height: auto;
    max-height: none;
  }
}

/* Very large desktop monitors (32-inch+ and 4K displays) */
@media (min-width: 2560px) {
  .schedule-container {
    width: 70vw; 
    margin-left: calc(50% - 30vw); 
    max-width: 2000px; /* Optimal width for very large displays */
  }
  
  .schedule-title {
    font-size: 2em;
    text-align: left;
    margin-left: 0;
    margin-right: 0;
  }
  
  .day-filter-container {
    text-align: left;
    margin-left: 0;
    margin-right: 0;
  }
  
  .day-buttons {
    justify-content: flex-start;
  }
  
  .responsive-schedule {
    height: auto;
    max-height: none;
  }
  
  .day-btn {
    padding: 16px 20px;
    font-size: 16px;
    min-width: 120px;
  }
}

/* Additional centering for tables on large screens */
@media (min-width: 1200px) {
  .sheet-wrapper {
    display: flex;
    justify-content: center;
    align-items: flex-start;
  }
  
  .responsive-schedule {
    display: block;
    margin: 0 auto;
  }
}
</style>

<script>
let currentDay = 'oct8'; // Current selected day (default: Wednesday)

// Day filtering functionality
function filterByDay(day) {
  currentDay = day;
  
  // Update active button
  document.querySelectorAll('.day-btn').forEach(btn => {
    btn.classList.remove('active');
  });
  document.querySelector(`[data-day="${day}"]`).classList.add('active');
  
  // Hide all schedule views
  document.querySelectorAll('.schedule-view').forEach(view => {
    view.classList.remove('active');
  });
  
  // Show the selected schedule view
  document.getElementById(`scheduleIframe${day.charAt(0).toUpperCase() + day.slice(1)}`).classList.add('active');
  
  // Remove all day classes first, then add the correct ones
  const wrapper = document.getElementById('sheetWrapper');
  wrapper.classList.remove('day-oct8', 'day-oct9', 'day-oct10', 'day-oct11', 'day-oct12');
  wrapper.classList.add('day-view', `day-${day}`);
}



// Initialize on page load
document.addEventListener('DOMContentLoaded', function() {
  // Page initialization complete
});
</script>

