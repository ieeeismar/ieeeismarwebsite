---
layout: 2025/page
title: Overview
---

<div class="schedule-container">
  <h2 class="schedule-title">Overview</h2>
  <iframe 
    src="https://docs.google.com/spreadsheets/d/e/2PACX-1vS_Ead4Dr0LYAhjLdhVS8FGvg2SRaQvEEWGnfXl2YrGV0vTXZj8eD4NtyJKgTk7iK4K2_zEQlXCrkSV/pubhtml?gid=1392480741&single=true&widget=true&headers=false&chrome=false" 
    class="responsive-schedule"
    style="border: none;">
  </iframe>
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

.responsive-schedule {
  width: 100%;
  height: 70vh; 
  min-height: 500px;
  max-height: 800px;
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
    height: 60vh;
    min-height: 400px;
  }
  
  .schedule-title {
    font-size: 1.3em;
    margin-bottom: 10px;
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
    margin-left: calc(50% - 45vw); 
  }
  
  .responsive-schedule {
    height: 75vh;
    max-height: 900px;
  }
  
  .schedule-title {
    font-size: 1.6em;
  }
}

/* Extra large screens */
@media (min-width: 1600px) {
  .schedule-container {
    width: 85vw; 
    margin-left: calc(50% - 42.5vw); 
  }
  
  .responsive-schedule {
    height: 80vh;
    max-height: 1000px;
  }
  
  .schedule-title {
    font-size: 1.7em;
  }
}

/* Ultra-wide screens */
@media (min-width: 2000px) {
  .schedule-container {
    width: 80vw; 
    margin-left: calc(50% - 40vw); 
  }
  
  .responsive-schedule {
    height: 85vh;
    max-height: 1100px;
  }
  
  .schedule-title {
    font-size: 1.8em;
  }
}
</style>

