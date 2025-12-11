---
layout: 2026/attend-page-2026
title: About Visual Identity
permalink: /2026/visual-identity/
---

## Logo Concept

Puglia's ceramic tradition forms the conceptual foundation of the logo, drawing on the visual language of handcrafted plates decorated with flowing lines, geometric patterns, and warm earthy tones. These elements translate the region’s craftsmanship and vitality into a contemporary graphic identity that expresses continuity, authenticity, and a deep connection to place.


<div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%;">
  <img src="{{ 'assets/2026/img/inspiration.png' | relative_url }}" alt="Puglia's ceramics inspiration"
       style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; object-fit: cover;">
</div>

At the heart of this visual system stands the **Rooster**, a recurring motif in Puglia's ceramics and a symbol of good fortune and renewal, reinterpreted in a modern form aligned with the event’s visual language. The logo also incorporates a human figure with open arms.

1) **Color Palette** – The color palette is directly drawn from the primary tones used in traditional ceramic decoration, especially those used in Rooster ceramics. Yellow, orange, red, and blue echo the vivid pigments of hand–painted plates, while the dark brown stroke represents the painterly brush line typical of ceramic craftsmanship

2) **ISMAR Logo** – The ISMAR logo is inspired by the Japanese Kanji **“合”** turned upside down, symbolizing the merger of the original ISAR (International Symposium on Augmented Reality) and ISMR (International Symposium on Mixed Reality) conferences. Its stylized human figure with open arms reflects a welcoming, inclusive spirit, while its form echoes motifs from Apulian ceramics, reinterpreted in a modern, minimal design.


<div style="position: relative;">
  <img id="interactive-image" src="{{ 'assets/2026/img/VisualIdentity.png' | relative_url }}" usemap="#image-map" width="100%" height="auto"/>
  <div style="text-align: center; margin-top: 10px; font-weight: bold;">
    ↑ Hover over the visual elements on the banner to explore more about each landmark. ↑ 
  </div>
  <map name="image-map">

    <area shape="rect" coords="200,40,0,200"
      alt="ISMAR with open arms"
      data-preview="{{ 'assets/2026/img/banner elements/customlogo.png' | relative_url }}"
      href="#"
      onmouseover="highlightArea(this)" onmouseout="resetArea(this)" onmousemove="moveHoverText(event)">

    <area shape="rect" coords="1200,40,700,200"
      alt="Puglia's Rooster Figure"
      data-preview="{{ 'assets/2026/img/banner elements/rooster.jpg' | relative_url }}"
      href="#"
      onmouseover="highlightArea(this)" onmouseout="resetArea(this)" onmousemove="moveHoverText(event)">

    <area shape="rect" coords="200,400,0,300"
      alt="Adriatic Sea"
      data-preview="{{ 'assets/2026/img/banner elements/sea.jpg' | relative_url }}"
      href="#"
      onmouseover="highlightArea(this)" onmouseout="resetArea(this)" onmousemove="moveHoverText(event)">

    <area shape="rect" coords="260,400,0,300"
      alt="Lighthouse"
      data-preview="{{ 'assets/2026/img/banner elements/faro.jpg' | relative_url }}"
      href="#"
      onmouseover="highlightArea(this)" onmouseout="resetArea(this)" onmousemove="moveHoverText(event)">

    <area shape="rect" coords="400,400,0,300"
      alt="Castello Svevo"
      data-preview="{{ 'assets/2026/img/banner elements/castello.jpg' | relative_url }}"
      href="#"
      onmouseover="highlightArea(this)" onmouseout="resetArea(this)" onmousemove="moveHoverText(event)">

    <area shape="rect" coords="500,400,0,300"
      alt="Basilica of San Nicola"
      data-preview="{{ 'assets/2026/img/banner elements/basilica.JPG' | relative_url }}"
      href="#"
      onmouseover="highlightArea(this)" onmouseout="resetArea(this)" onmousemove="moveHoverText(event)">

    <area shape="rect" coords="600,400,0,300"
      alt="Cathedral of San Sabino"
      data-preview="{{ 'assets/2026/img/banner elements/cattedrale.JPG' | relative_url }}"
      href="#"
      onmouseover="highlightArea(this)" onmouseout="resetArea(this)" onmousemove="moveHoverText(event)">

    <area shape="rect" coords="720,400,0,300"
      alt="Teatro Margherita"
      data-preview="{{ 'assets/2026/img/banner elements/margherita.jpg' | relative_url }}"
      href="#"
      onmouseover="highlightArea(this)" onmouseout="resetArea(this)" onmousemove="moveHoverText(event)">

    <area shape="rect" coords="830,400,0,300"
      alt="Teatro Petruzzelli"
      data-preview="{{ 'assets/2026/img/banner elements/petruzzelli.JPG' | relative_url }}"
      href="#"
      onmouseover="highlightArea(this)" onmouseout="resetArea(this)" onmousemove="moveHoverText(event)">

    <area shape="rect" coords="1000,400,0,300"
      alt="Seafront Streetlights"
      data-preview="{{ 'assets/2026/img/banner elements/light.jpg' | relative_url }}"
      href="#"
      onmouseover="highlightArea(this)" onmouseout="resetArea(this)" onmousemove="moveHoverText(event)">

  </map>

  <div id="hover-text"
       style="position: absolute; visibility: hidden; background: rgba(0,0,0,0.8); color: white; padding: 10px 15px; border-radius: 8px; font-size: 14px; max-width: 250px; z-index: 10;">
    Hover over a section
  </div>

  <img id="hover-preview" class="preview-thumb" src="" alt="">
</div>


### Design Elements
- **Core marks**: Reworked ISMAR icon and wordmark.
- **Line style**: High-contrast outlines referencing ceramic brushwork.
- **Palette**: Primary red, yellow, blue with Puglia's blues.
- **Motifs**: Rooster and floral tiles.
- **Grid and usage**: Modular tiles that scale.


<style>
@keyframes pulse {
  0% { transform: scale(1); }
  50% { transform: scale(1.03); }
  100% { transform: scale(1); }
}

#interactive-image {
  animation: pulse 10s ease-in-out 3;
}

.preview-thumb {
  position: absolute;
  width: 120px;
  height: auto;
  opacity: 0;
  pointer-events: none;
  transition: opacity 0.15s;
  border: 1px solid #ccc;
  background: #fff;
  z-index: 20;
}
</style>

<script>
function highlightArea(area) {
  var img = document.getElementById("interactive-image");
  img.style.filter = "brightness(0.7)";

  var txt = document.getElementById("hover-text");
  txt.innerHTML = area.alt;
  txt.style.visibility = "visible";

  var preview = document.getElementById("hover-preview");
  preview.src = area.dataset.preview;
  preview.style.opacity = 1;
}

function resetArea() {
  var img = document.getElementById("interactive-image");
  img.style.filter = "none";

  var txt = document.getElementById("hover-text");
  txt.style.visibility = "hidden";

  var preview = document.getElementById("hover-preview");
  preview.style.opacity = 0;
}

function moveHoverText(event) {
  var txt = document.getElementById("hover-text");
  var preview = document.getElementById("hover-preview");
  var img = document.getElementById("interactive-image");

  var mouseX = event.clientX;
  var mouseY = event.clientY;

  var rect = img.getBoundingClientRect();
  var relX = mouseX - rect.left;
  var relY = mouseY - rect.top;

  var w = txt.offsetWidth;
  var h = txt.offsetHeight;

  var ox = 10;
  var oy = 10;

  var x = relX + ox;
  var y = relY + oy;

  if (x + w > window.innerWidth) x = relX - w - ox;
  if (y + h > window.innerHeight) y = relY - h - oy;

  txt.style.left = x + "px";
  txt.style.top = y + "px";

  preview.style.left = (x + w + 10) + "px";
  preview.style.top = y + "px";
}
</script>
