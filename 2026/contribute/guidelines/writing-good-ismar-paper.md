---
layout: 2026/contribute-page-2026
title: Writing a Good ISMAR Paper
permalink: /2026/guidelines/writing-good-ismar-paper
---
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-FQFFZGXF3Y"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'G-FQFFZGXF3Y');
</script>

A good ISMAR submission will result in both a respectable document for the proceedings and a good conference talk. As an author, you should ask yourself the following questions while writing your paper. Submissions that do not provide good answers to these questions are unlikely to be accepted.

## What problem are you addressing?
The most common motivation for publishing a paper is to present a solution to a problem. When doing so, try to state all your constraints and assumptions. This is an area where it can be invaluable to have someone who is not intimately familiar with your work read the paper. Include a crisp description of the problem in the abstract and try to suggest it in the title. Note that the Paper Chairs depend almost completely on the abstract and title when they determine which Program Committee member to assign to the paper.

ISMAR papers often focus on specific aspects of Augmented Reality, Mixed Reality, or Virtual Reality systems. The following list includes some example topics, but does not represent an exhaustive list of all topics. We welcome any new idea beyond the usual range of areas.

- **Interaction Methods:** Does the paper propose a novel interaction method for Augmented Reality, Mixed Reality, or Virtual Reality? Does it present different use cases and applications? Can it demonstrate that the method performs better than other known ones?
- **User Interface & Human Factors:** Does the paper describe how Augmented Reality, Mixed Reality, or Virtual Reality is improving a user interface design, human task performance, or perception?
- **Tracking and Pose Estimation:** Does the paper describe a novel method that is more robust in difficult conditions such as lighting, outdoor environments, or fast motion? Is it a new or clever combination of different sensors? Does it provide more information for interaction and rendering?
- **Rendering and Visualization:** Does the paper describe a novel or improved method for realistic integration of virtual graphics into a mixed scene? Is it faster or more accurate than existing methods? Does it offer a novel way to present information about the real world?
- **Displays and Input Devices:** Does the paper describe a novel display, visual or aural? Does it describe a novel input device that provides different input modalities, is easier to use and deploy, or more precise?
- **Applications:** Is the paper proposing a new application of Augmented Reality, Mixed Reality, or Virtual Reality in a specific domain? Does it provide a new understanding of usage patterns and social behavior of a deployed application? An application must have a concrete use case in a target domain and not be only a software implementation.


## What were the previous approaches?

What are the relevant published works in your problem area? What deficiencies in their approaches are you trying to overcome? How does the new approach differ from previously published results? Do not expect the reviewers to know this information unless you tell them in the paper, as they are unlikely to remember the precise details of all the relevant literature. Make specific comparisons between your work and that described in the references; do not just compile a list of vaguely related papers. What are the limitations of your work, and is the future work still to be addressed?

## How well did you address your stated problem?
Based on your problem statement, what did you accomplish? You are responsible for arguing that the problem is sufficiently addressed. Include pictures, statistics, or whatever is required to make your case. If you find this part of the paper difficult to write, perhaps the work is not yet finished, and the paper should be deferred until next year. (And, perhaps, submitted as a poster this year).

The following describes some typical evaluation methods for different kinds of papers. This list is not exhaustive, but it provides some hints on how to present your contribution.

- **Interaction Methods:** Did you measure how usable the method or system is? What is the performance of users, such as completion time, error rate, or learning curve, compared to a previous interface developed for a similar task?
- **User Interface & Human Factors:** Is the improvement or effect well supported through evaluations? Was the experimental design appropriate for the proposed solution? Were the sample size, statistical evaluation, presentation, and conclusions appropriate? Were sample sizes diverse and representative of the intended user population?
- **Tracking and Pose Estimation:** What contribution does the method make to the Augmented, Mixed, or Virtual Reality domain? How does it compare to state of the art systems? Can the system maintain competitive robustness and reliability? Can it handle difficult input conditions such as varying lighting, fast motion, and occlusions? How fast is it and on which hardware? Were standard data sets used or are the test data sets made available for comparison?
- **Rendering and Visualization:** Is the output quality superior to previous methods? Is it fast enough to operate at real time rates? What hardware and sensors are required? For visualization, which use cases are supported and what level of data complexity can be handled?
- **Displays and Input Devices:** What are the performance specifications of the display? For visual displays, does it operate indoors and outdoors, under strong lighting conditions, what is the field of view, and is it multi user capable? What hardware and software are required to recreate it? What are the specifications of the input device and can it be used in mobile settings?
- **Applications:** How was the application designed? Which constraints from the application domain are essential? Was the system tested by representative end users? Did it affect relevant factors such as performance or safety? Did it create opportunities to improve work methods?

## What does this work contribute to the field?

What are your new ideas or results? If you do not have at least one new idea, you do not have a publishable paper. Can your results be applied anywhere outside of your project? If not, the paper is probably too narrowly purposed for ISMAR. On the other hand, beware of trying to write a paper with too large a scope.

## Is the paper complete?

The question that generates the most discussion within the Program Committee is whether a paper is complete. If the paper presents an algorithm or technique, an experienced practitioner in the field should be able to implement it using the paper and its references. If the paper claims to present a faster or more efficient way to implement an established technique, it must include enough detail to replicate the experiment on competing implementations. When you quote numbers, be sure that they are not misleading, state clearly whether they were measured, simulated, or derived, and how you did the measurements, simulations, or derivations. For example, CPU time measurements are meaningless unless the reader is told the machine and configuration on which they were obtained.

## Does the paper present too much information?
Many large, poorly written papers contain a good paper trying to get out. It is the author’s responsibility, not the reviewer’s, to discover this paper and turn it into the submission. If you have addressed a single, practical problem, do not try to generalize it for the purposes of publication. If you have a formal theory or elaborate architecture, do not include all the vagaries of the implementation unless they are critical to the utility of the theory. Do not include the contents of your user’s manual; instead, describe the model or functionality achieved. You should assume your audience has a working knowledge of user-interface development and access to the major journals in computer science, electrical engineering, and psychology. A short conference paper can only present a few concise ideas well.


## Can this paper be presented well?
While ISMAR papers are judged primarily as technical papers, some consideration is given to how suitable the topic is for a conference presentation. Think of how you would present your ideas, and how big the audience is likely to be. Papers that have a small number of concisely stated new ideas and that are visually interesting tend to appeal to a large audience and be easy to present. As recent conferences clearly show, these criteria do not eliminate papers that have taxonomies or strong theoretical content, or appeal to a specialized audience, if they contain significant new ideas.


## Should a video also be included?
A video can be very helpful for communicating technical results, especially when the paper discusses an interaction technique. However, do not try to save space in the paper by putting essential information into the video. The paper must stand on its own.


##  Is the paper accessible?
All information, including information in figures, charts, tables, etc., should be available to readers who consume it in different ways. For example, some of us cannot see color, some read papers as a monochrome printout, some use low-contrast displays, and some listen to the content instead of seeing it. SIGCHI has useful information on making a paper accessible.


## Is the paper using gender-neutral language?
Use “he” when referring to men or boys. Use “she” when referring to women or girls. Avoid phrases such as “he/she” or “he or she” when a gender is not clearly known. Instead, use “they” as a gender-neutral pronoun. When referencing a profession, use the gender-neutral form. For example, use firefighter, police officer, or worker instead of fireman, policeman, or workman. See this excerpt of the Chicago Style for more information about gender-neutral pronouns.


## Are participant demographics reported correctly?
If your submission included experiments with humans, it is important to consider whether they represent your target audience and what effect the background of the participants could have on the results. A good ISMAR paper should include information about the participants’ age range and background, and discuss the effect this could have had on the findings and generalization of the results.

## Does the submission follow the author guidelines?
Even the best submission may end up desk-rejected, e.g., if it is formatted incorrectly, is too long, or violates the anonymity requirement. To avoid such an outcome ensure that you follow the <a href="/2026/guidelines/author-guidelines">Author Guidelines</a>. 


## Further Examples:
You can also find the full list of papers previously published at ISMAR in the IEEE Digital Library (IEEE Xplore). Furthermore, the ismar.net website lists past best paper award winners, which are excellent examples of great ISMAR papers. Note that the ISMAR proceedings from previous years include TVCG journal publications and conference proceedings. 

Best regards,

**ISMAR 2026 Scientific Program Chairs**
- Mariko Isogawa
- Kangsoo Kim
- Alejandro Martin-Gomez
- Alexander Plopski
- Missie Smith
- Florian Weidner

Inquiries: <a href="mailto:papers2026@ieeeismar.net">papers2026@ieeeismar.net</a>

### Document History:

This document was updated and extended by the ISMAR 2026 Program Chairs: Mariko Isogawa, Kangsoo Kim, Alejandro Martin-Gomez, Alexander Plopski, Missie Smith, and Florian Weidner. It was adopted following the work of the ISMAR 2025 Program Chairs: Ulrich Eck, Gun Lee, Alexander Plopski, Missie Smith, Qi Sun, Markus Tatzgern, the 2024 Program Chairs:  Ulrich Eck, Misha Sra, Jeanine Stefanucci, Maki Sugimoto, Markus Tatzgern, Ian Williams, the 2023 Conference Paper Chairs: Jens Grubert, Andrew Cunningham, Evan Y. Peng, Gerd Bruder, Anne-Hélène Olivier, and Ian Williams, the 2021 Journal Paper Chairs: Daisuke Iwai, Denis Kalkofen, Guillaume Moreau, and Tabitha Peck as well as the 2021 Conference Paper Chairs: Maud Marchal, Anne-Hélène Olivier, Rafael Radkowski, Jonathan Ventura, and Lily Wang. The document was obtained from Shimin Hu and Stefanie Zollmann, Wolfgang Broll, Holger Regenbrecht, and J. Edward Swan II, who inherited it from Wolfgang Broll, Hideo Saito, and J. Edward Swan II, based on Walterio Mayol, Christian Sandor, and Rob Lindeman, based on significant materials created by Ron Azuma on how to write a successful ISMAR paper and how to be a successful Program Chair, also based on the 2011 UIST Author Guidelines edited by Maneesh Agrawala and Scott Klemmer (using material provided by Saul Greenberg), who inherited it from François Guimbretière, who inherited it from Michel Beaudouin Lafon, who inherited it from Ravin Balakrishnan and Chia Shen, who inherited it from Ken Hinckley and Pierre Wellner, who inherited it from Dan Olsen, who inherited it from Steve Feiner, who inherited it from Joe Konstan, who inherited it from Michel Beaudouin Lafon, who inherited it from Ari Rapkin, who inherited it from Beth Mynatt, who inherited it from George Robertson, who inherited it from Marc H. Brown, who inherited it from George Robertson, who got lots of help on it from Steve Feiner, Brad Myers, Jock Mackinlay, Mark Green, Randy Pausch, Pierre Wellner, and Beth Mynatt.
